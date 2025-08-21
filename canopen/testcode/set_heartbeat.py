#!/usr/bin/env python3
"""
CANopen 心跳时间修改工具 (修正版)
功能：通过SDO指令修改特定CANopen节点的心跳生产者时间（对象字典索引0x1017）
注意：心跳时间是16位无符号整数，不是32位
作者：CANopen 专家
日期：2023-10-15
"""

import argparse
import can
import time
import sys
from datetime import datetime

class CANopenHeartbeatConfigurator:
    def __init__(self, interface='can1', bitrate=1000000, node_id=10):
        """
        初始化CANopen心跳配置器
        
        参数:
            interface: CAN接口名称
            bitrate: CAN总线波特率
            node_id: 要配置的节点ID
        """
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
        except Exception as e:
            print(f"❌ 发生意外错误: {e}")
            return False
    
    def send_sdo_write_request_16bit(self, index, subindex, data):
        """
        发送16位SDO写请求
        
        参数:
            index: 对象字典索引
            subindex: 对象字典子索引
            data: 要写入的数据（16位整数）
        """
        # 将索引拆分为低字节和高字节
        index_low = index & 0xFF
        index_high = (index >> 8) & 0xFF
        
        # 构建SDO写请求报文
        # 命令字节: 0x2B 表示 expedited write, 2字节数据
        command_byte = 0x2B  # 0x2表示写请求, 0x1表示大小指示, 0x3表示数据大小=2字节
        
        # 将数据转换为小端格式的2字节
        data_bytes = data.to_bytes(2, byteorder='little')
        
        # 构建完整的数据帧
        sdo_data = [
            command_byte,  # 命令字节
            index_low,     # 索引低字节
            index_high,    # 索引高字节
            subindex,      # 子索引
            data_bytes[0], # 数据字节0 (最低有效字节)
            data_bytes[1], # 数据字节1
            0x00,          # 填充字节
            0x00           # 填充字节
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
            print(f"📤 已发送SDO写请求: 索引=0x{index:04X}, 子索引={subindex}, 值={data} (16位)")
            return True
        except can.CanError as e:
            print(f"❌ 发送SDO请求失败: {e}")
            return False
    
    def wait_for_sdo_response(self, timeout=1.0):
        """
        等待SDO响应
        
        参数:
            timeout: 超时时间(秒)
        
        返回:
            response_data: 响应数据，如果超时或错误则返回None
        """
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                msg = self.bus.recv(timeout=0.1)
                
                if msg and msg.arbitration_id == self.sdo_rx_cobid:
                    # 检查响应类型
                    if len(msg.data) >= 1:
                        command_byte = msg.data[0]
                        
                        # 成功的写响应应该是0x60
                        if command_byte == 0x60:
                            print("✅ SDO写操作成功")
                            return True
                        # 错误响应
                        elif command_byte & 0xE0 == 0x80:
                            error_code = int.from_bytes(msg.data[4:8], byteorder='little')
                            print(f"❌ SDO写操作失败，错误代码: 0x{error_code:08X}")
                            return False
            
            except can.CanError as e:
                print(f"❌ 接收SDO响应时发生错误: {e}")
                return False
        
        print("❌ 等待SDO响应超时")
        return False
    
    def set_heartbeat_time(self, heartbeat_time_ms):
        """
        设置心跳生产者时间
        
        参数:
            heartbeat_time_ms: 心跳时间(毫秒)
        """
        if not self.bus:
            if not self.connect():
                return False
        
        # 验证数据范围 (16位无符号整数)
        if heartbeat_time_ms < 0 or heartbeat_time_ms > 65535:
            print(f"❌ 错误: 心跳时间必须在 0-65535 范围内")
            return False
        
        # 发送SDO写请求到索引0x1017，子索引0x00
        success = self.send_sdo_write_request_16bit(0x1017, 0x00, heartbeat_time_ms)
        
        if success:
            # 等待响应
            return self.wait_for_sdo_response()
        
        return False
    
    def close(self):
        """关闭CAN连接"""
        if self.bus:
            self.bus.shutdown()
            print("CAN总线连接已关闭")

def main():
    # 命令行参数解析
    parser = argparse.ArgumentParser(
        description="CANopen心跳时间配置工具 - 修改特定节点的心跳生产者时间",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-i', '--interface', default='can1', 
                        help='CAN接口名称')
    parser.add_argument('-b', '--bitrate', type=int, default=1000000,
                        help='CAN总线波特率')
    parser.add_argument('-n', '--node', type=int, default=10,
                        help='要配置的节点ID')
    parser.add_argument('-t', '--time', type=int, default=2000,
                        help='要设置的心跳时间(毫秒)')
    
    args = parser.parse_args()
    
    # 验证节点ID
    if args.node < 1 or args.node > 127:
        print("❌ 错误: 节点ID必须在 1-127 范围内")
        sys.exit(1)
    
    # 验证心跳时间
    if args.time < 0 or args.time > 65535:
        print("❌ 错误: 心跳时间必须在 0-65535 范围内")
        sys.exit(1)
    
    # 打印配置信息
    print("CANopen 心跳时间配置工具 (修正版)")
    print("=" * 50)
    print(f"接口:      {args.interface}")
    print(f"波特率:    {args.bitrate} bps")
    print(f"目标节点:  {args.node}")
    print(f"新心跳时间: {args.time} 毫秒")
    print("=" * 50)
    print("注意: 心跳时间是16位无符号整数")
    print("=" * 50)
    
    # 创建配置器
    configurator = CANopenHeartbeatConfigurator(
        interface=args.interface,
        bitrate=args.bitrate,
        node_id=args.node
    )
    
    # 设置心跳时间
    success = configurator.set_heartbeat_time(args.time)
    
    # 关闭连接
    configurator.close()
    
    # 根据执行结果退出
    if success:
        print(f"🎉 成功将节点 {args.node} 的心跳时间设置为 {args.time} 毫秒")
        sys.exit(0)
    else:
        print(f"❌ 设置节点 {args.node} 的心跳时间失败")
        sys.exit(1)

if __name__ == "__main__":
    main()