#!/usr/bin/env python3
"""
CANopen 设备信息读取工具 (低级CAN消息版本)
功能：尝试读取多个可能的设备名称索引
作者：CANopen 专家
日期：2023-10-15
"""

import argparse
import can
import time
import sys

class CANopenDeviceInfoReader:
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

    def send_sdo_read_request(self, index, subindex=0):
        """
        发送SDO读请求并等待响应
        参数:
            index: 对象字典索引
            subindex: 对象字典子索引
        返回:
            读取到的数据值，如果失败返回None
        """
        # 将索引拆分为低字节和高字节
        index_low = index & 0xFF
        index_high = (index >> 8) & 0xFF
        
        # 构建SDO读请求报文
        sdo_data = [
            0x40,  # 命令字节: 读请求
            index_low,
            index_high,
            subindex,
            0, 0, 0, 0  # 填充字节
        ]
        
        # 创建CAN消息
        msg = can.Message(
            arbitration_id=self.sdo_tx_cobid,
            data=sdo_data,
            is_extended_id=False
        )
        
        # 发送消息
        try:
            self.bus.send(msg)
            print(f"📤 已发送SDO读请求: 索引=0x{index:04X}, 子索引={subindex}")
        except can.CanError as e:
            print(f"❌ 发送SDO读请求失败: {e}")
            return None
        
        # 等待响应
        start_time = time.time()
        timeout = 1.0  # 1秒超时
        
        while time.time() - start_time < timeout:
            try:
                msg = self.bus.recv(timeout=0.1)
                if msg and msg.arbitration_id == self.sdo_rx_cobid:
                    if len(msg.data) >= 8:
                        command_byte = msg.data[0]
                        if command_byte == 0x43:  # 成功的读响应
                            # 提取数据 (4字节)
                            data = int.from_bytes(msg.data[4:8], byteorder='little')
                            return data
                        elif command_byte & 0xE0 == 0x80:  # 错误响应
                            error_code = int.from_bytes(msg.data[4:8], byteorder='little')
                            print(f"❌ SDO读操作失败，错误代码: 0x{error_code:08X}")
                            return None
            except can.CanError as e:
                print(f"❌ 接收SDO响应时发生错误: {e}")
                return None
        
        print("❌ 等待SDO响应超时")
        return None

    def read_string(self, index, subindex=0):
        """
        读取字符串数据 (简化版本，假设字符串长度<=4字节)
        参数:
            index: 对象字典索引
            subindex: 对象字典子索引
        返回:
            读取到的字符串，如果失败返回None
        """
        data = self.send_sdo_read_request(index, subindex)
        if data is not None:
            try:
                # 将整数转换为字节并解码为字符串
                bytes_data = data.to_bytes(4, byteorder='little')
                return bytes_data.decode('ascii').rstrip('\x00')
            except:
                return f"无法解码: 0x{data:08X}"
        return None

    def get_device_name(self):
        """尝试读取多个可能的设备名称索引"""
        print("\n" + "="*60)
        print("尝试读取设备名称")
        print("="*60)
        
        # 尝试多个可能的设备名称索引
        device_name_indices = [
            0x1008,  # 标准设备名称索引
            0x1000,  # 设备类型（虽然不是名称，但可以验证通信）
            0x1009,  # 硬件版本（字符串）
            0x100A,  # 软件版本（字符串）
        ]
        
        for index in device_name_indices:
            print(f"尝试读取索引 0x{index:04X}...")
            result = self.read_string(index)
            if result and not result.startswith("无法解码"):
                print(f"成功读取索引 0x{index:04X}: {result}")
                return result
            else:
                print(f"索引 0x{index:04X} 读取失败")
        
        return None

    def close(self):
        """关闭CAN连接"""
        if self.bus:
            self.bus.shutdown()
            print("CAN总线连接已关闭")

def main():
    # 命令行参数解析
    parser = argparse.ArgumentParser(
        description="CANopen设备名称读取工具",
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
    print("CANopen 设备名称读取工具")
    print("="*50)
    print(f"接口: {args.interface}")
    print(f"波特率: {args.bitrate} bps")
    print(f"目标节点: {args.node}")
    print("="*50)
    
    # 创建读取器
    reader = CANopenDeviceInfoReader(
        interface=args.interface,
        bitrate=args.bitrate,
        node_id=args.node
    )
    
    # 连接到CAN总线
    if not reader.connect():
        sys.exit(1)
    
    # 获取设备名称
    device_name = reader.get_device_name()
    
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