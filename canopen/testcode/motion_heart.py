#!/usr/bin/env python3
"""
CANopen 心跳监听工具 - 监控节点ID=10的控制器
功能：监听特定CANopen节点的心跳报文，监控其状态和在线状态
作者：CANopen 专家
日期：2023-10-15
"""

import argparse
import can
import time
import sys
from datetime import datetime

class CANopenHeartbeatMonitor:
    def __init__(self, interface='can1', bitrate=1000000, node_id=10, timeout=3.0):
        """
        初始化CANopen心跳监视器
        
        参数:
            interface: CAN接口名称
            bitrate: CAN总线波特率
            node_id: 要监视的节点ID
            timeout: 心跳超时时间(秒)
        """
        self.interface = interface
        self.bitrate = bitrate
        self.node_id = node_id
        self.timeout = timeout
        self.bus = None
        self.last_heartbeat_time = None
        self.running = False
        
        # NMT状态定义
        self.nmt_states = {
            0: "初始化 (Initializing)",
            4: "停止 (Stopped)",
            5: "运行 (Operational)",
            127: "预运行 (Pre-operational)",
        }
    
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
    
    def parse_heartbeat(self, data):
        """解析心跳报文数据"""
        if not data or len(data) < 1:
            return None, "无效数据"
        
        state_byte = data[0]
        state_name = self.nmt_states.get(state_byte, f"未知状态 (0x{state_byte:02X})")
        return state_byte, state_name
    
    def monitor(self):
        """开始监视心跳"""
        if not self.bus:
            if not self.connect():
                return False
        
        target_cob_id = 0x700 + self.node_id
        print(f"🔍 开始监视节点 {self.node_id} 的心跳 (COB-ID: 0x{target_cob_id:03X})")
        print("按下 Ctrl+C 停止监视")
        print("-" * 60)
        
        self.running = True
        self.last_heartbeat_time = time.time()
        
        try:
            while self.running:
                # 检查超时
                current_time = time.time()
                time_since_last_heartbeat = current_time - self.last_heartbeat_time
                
                if time_since_last_heartbeat > self.timeout:
                    print(f"\r❌ 节点 {self.node_id} 心跳超时 ({time_since_last_heartbeat:.1f}秒) ", end="")
                    sys.stdout.flush()
                
                # 接收消息
                try:
                    msg = self.bus.recv(timeout=0.1)
                    
                    if msg and msg.arbitration_id == target_cob_id:
                        self.last_heartbeat_time = current_time
                        state_byte, state_name = self.parse_heartbeat(msg.data)
                        
                        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
                        print(f"\r[{timestamp}] 节点 {self.node_id}: {state_name} (0x{state_byte:02X})")
                
                except can.CanError as e:
                    print(f"\n❌ CAN接收错误: {e}")
                    break
                    
        except KeyboardInterrupt:
            print("\n\n监控已停止")
        finally:
            self.stop()
        
        return True
    
    def stop(self):
        """停止监视并清理资源"""
        self.running = False
        if self.bus:
            self.bus.shutdown()
            print("CAN总线连接已关闭")

def main():
    # 命令行参数解析
    parser = argparse.ArgumentParser(
        description="CANopen心跳监视工具 - 监控特定节点的心跳状态",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-i', '--interface', default='can1', 
                        help='CAN接口名称')
    parser.add_argument('-b', '--bitrate', type=int, default=1000000,
                        help='CAN总线波特率')
    parser.add_argument('-n', '--node', type=int, default=10,
                        help='要监视的节点ID')
    parser.add_argument('-t', '--timeout', type=float, default=3.0,
                        help='心跳超时时间(秒)')
    
    args = parser.parse_args()
    
    # 验证节点ID
    if args.node < 1 or args.node > 127:
        print("❌ 错误: 节点ID必须在 1-127 范围内")
        sys.exit(1)
    
    # 打印配置信息
    print("CANopen 心跳监视工具")
    print("=" * 40)
    print(f"接口:      {args.interface}")
    print(f"波特率:    {args.bitrate} bps")
    print(f"监视节点:  {args.node}")
    print(f"超时时间:  {args.timeout} 秒")
    print("=" * 40)
    
    # 创建并启动监视器
    monitor = CANopenHeartbeatMonitor(
        interface=args.interface,
        bitrate=args.bitrate,
        node_id=args.node,
        timeout=args.timeout
    )
    
    # 开始监视
    success = monitor.monitor()
    
    # 根据执行结果退出
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()