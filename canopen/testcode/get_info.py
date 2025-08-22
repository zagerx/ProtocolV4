#!/usr/bin/env python3
"""
CANopen 设备名称读取工具
功能：支持分段读取长设备名称（索引0x1008）
作者：CANopen 专家
日期：2023-10-15
"""

import argparse
import can
import time
import sys

class CANopenDeviceNameReader:
    def __init__(self, interface='can1', bitrate=1000000, node_id=10):
        self.interface = interface
        self.bitrate = bitrate
        self.node_id = node_id
        self.bus = None
        # SDO通信参数
        self.sdo_tx_cobid = 0x600 + self.node_id  # 发送到节点的SDO请求COB-ID
        self.sdo_rx_cobid = 0x580 + self.node_id  # 从节点接收的SDO响应COB-ID

    def connect(self):
        """连接到CAN总线"""
        try:
            self.bus = can.Bus(
                interface='socketcan',
                channel=self.interface,
                bitrate=self.bitrate
            )
            print(f"✅ 已连接到CAN接口 {self.interface}，波特率 {self.bitrate}")
            return True
        except can.CanError as e:
            print(f"❌ 连接CAN接口失败: {e}")
            return False

    def send_sdo_request(self, data):
        """发送SDO请求"""
        try:
            msg = can.Message(
                arbitration_id=self.sdo_tx_cobid,
                data=data,
                is_extended_id=False
            )
            self.bus.send(msg)
            return True
        except can.CanError as e:
            print(f"❌ 发送SDO请求失败: {e}")
            return False

    def wait_for_sdo_response(self, timeout=1.0):
        """
        等待SDO响应
        返回: (command_byte, full_data) 或 (None, None) 如果超时或错误
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                msg = self.bus.recv(timeout=0.1)
                if msg and msg.arbitration_id == self.sdo_rx_cobid:
                    if len(msg.data) >= 8:
                        print(f"📥 收到SDO响应: {msg.data.hex(' ')}")
                        return msg.data[0], msg.data  # 返回完整数据
            except can.CanError as e:
                print(f"❌ 接收SDO响应时发生错误: {e}")
                return None, None
        return None, None

    def read_string_segmented(self, index, subindex=0):
        """
        分段读取字符串数据（支持超过4字节）
        参数:
            index: 对象字典索引
            subindex: 对象字典子索引
        返回:
            读取到的字符串，如果失败返回None
        """
        # 发送初始化读取请求
        index_low = index & 0xFF
        index_high = (index >> 8) & 0xFF
        
        init_data = [
            0x40,  # 命令字节: 读请求
            index_low,
            index_high,
            subindex,
            0, 0, 0, 0
        ]
        
        if not self.send_sdo_request(init_data):
            return None
        
        print(f"📤 已发送SDO读请求: 索引=0x{index:04X}, 子索引={subindex}")
        
        # 等待初始化响应
        command_byte, full_data = self.wait_for_sdo_response()
        if command_byte is None:
            print("❌ 等待SDO响应超时")
            return None
        
        print(f"响应命令字节: 0x{command_byte:02X}")
        
        if command_byte == 0x43:  # 单次响应，数据长度<=4字节
            data_value = int.from_bytes(full_data[4:8], byteorder='little')
            try:
                bytes_data = data_value.to_bytes(4, byteorder='little')
                return bytes_data.decode('ascii').rstrip('\x00')
            except:
                return f"无法解码: 0x{data_value:08X}"
        
        elif command_byte == 0x41:  # 初始化分段响应
            # 解析数据长度
            total_size = int.from_bytes(full_data[4:8], byteorder='little')
            print(f"分段传输总大小: {total_size} 字节")
            
            # 开始分段传输
            result_bytes = bytearray()
            toggle = 0
            
            while len(result_bytes) < total_size:
                # 发送段请求
                segment_data = [
                    0x60 | (toggle << 4),  # 段请求命令字节
                    0, 0, 0, 0, 0, 0, 0
                ]
                
                if not self.send_sdo_request(segment_data):
                    return None
                
                print(f"📤 发送段请求, toggle={toggle}")
                
                # 等待段响应
                seg_command_byte, seg_full_data = self.wait_for_sdo_response()
                if seg_command_byte is None:
                    print("❌ 等待段响应超时")
                    return None
                
                print(f"段响应命令字节: 0x{seg_command_byte:02X}")
                
                if (seg_command_byte & 0xE0) == 0x00:  # 段响应
                    # 检查toggle位
                    seg_toggle = (seg_command_byte >> 4) & 0x01
                    if seg_toggle != toggle:
                        print(f"❌ toggle位不匹配: 期望{toggle}, 收到{seg_toggle}")
                        return None
                    
                    # 计算本段数据长度
                    seg_len = 7 - ((seg_command_byte >> 1) & 0x07)
                    if seg_len < 0 or seg_len > 7:
                        print(f"❌ 无效的段长度: {seg_len}")
                        return None
                    
                    print(f"段数据长度: {seg_len} 字节")
                    
                    # 添加数据 (从索引1开始，跳过命令字节)
                    result_bytes.extend(seg_full_data[1:1+seg_len])
                    
                    # 检查是否最后一段
                    if (seg_command_byte & 0x01) == 0x01:  # 最后一段
                        print("收到最后一段")
                        break
                    
                    # 切换toggle
                    toggle = 1 - toggle
                else:
                    print(f"❌ 意外的段响应: 0x{seg_command_byte:02X}")
                    return None
            
            try:
                return result_bytes.decode('ascii').rstrip('\x00')
            except:
                return f"无法解码分段数据: {result_bytes.hex()}"
        
        elif (command_byte & 0xE0) == 0x80:  # 错误响应
            error_code = int.from_bytes(full_data[4:8], byteorder='little')
            print(f"❌ SDO读操作失败，错误代码: 0x{error_code:08X}")
            return None
        else:
            print(f"❌ 未知的响应命令字节: 0x{command_byte:02X}")
            return None

    def read_device_name(self):
        """读取设备名称（索引0x1008），支持分段传输"""
        print("\n" + "="*60)
        print("设备名称读取")
        print("="*60)
        
        device_name = self.read_string_segmented(0x1008)
        if device_name:
            print(f"设备名称 (0x1008): {device_name}")
            return device_name
        else:
            print("❌ 设备名称读取失败")
            return None

    def close(self):
        """关闭CAN连接"""
        if self.bus:
            self.bus.shutdown()
            print("CAN总线连接已关闭")

def main():
    # 命令行参数解析
    parser = argparse.ArgumentParser(
        description="CANopen设备名称读取工具（支持分段传输）",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-i', '--interface', default='can1',
                        help='CAN接口名称')
    parser.add_argument('-b', '--bitrate', type=int, default=1000000,
                        help='CAN总线波特率')
    parser.add_argument('-n', '--node', type=int, default=10,
                        help='要读取的节点ID')
    
    args = parser.parse_args()
    
    # 验证节点ID
    if args.node < 1 or args.node > 127:
        print("❌ 错误: 节点ID必须在 1-127 范围内")
        sys.exit(1)
    
    # 打印配置信息
    print("CANopen 设备名称读取工具（支持分段传输）")
    print("="*50)
    print(f"接口: {args.interface}")
    print(f"波特率: {args.bitrate} bps")
    print(f"目标节点: {args.node}")
    print("="*50)
    
    # 创建读取器
    reader = CANopenDeviceNameReader(
        interface=args.interface,
        bitrate=args.bitrate,
        node_id=args.node
    )
    
    # 连接到CAN总线
    if not reader.connect():
        sys.exit(1)
    
    # 获取设备名称
    device_name = reader.read_device_name()
    
    # 关闭连接
    reader.close()
    
    # 根据执行结果退出
    if device_name:
        print("\n🎉 设备名称读取完成")
        sys.exit(0)
    else:
        print("\n❌ 设备名称读取失败")
        sys.exit(1)

if __name__ == "__main__":
    main()