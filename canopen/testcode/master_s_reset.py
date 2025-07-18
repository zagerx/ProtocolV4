#!/usr/bin/env python3
"""
CANopen 复位广播指令脚本
功能：通过 CAN1 接口广播发送复位所有节点的 NMT 指令
作者：CANopen 专家
日期：2023-10-15
"""

import argparse
import can
import time

# CANopen NMT 指令定义
NMT_COMMANDS = {
    'start': 0x01,
    'stop': 0x02,
    'preop': 0x80,
    'reset_node': 0x81,
    'reset_com': 0x82
}

def send_reset_command(interface='can1', bitrate=1000000, reset_type='reset_node'):
    """
    广播发送 CANopen 复位指令
    
    参数:
        interface: CAN 接口名称 (默认 'can1')
        bitrate: CAN 波特率 (默认 1Mbps)
        reset_type: 复位类型 ('reset_node' 或 'reset_com')
    """
    # 验证复位类型
    if reset_type not in NMT_COMMANDS:
        raise ValueError(f"无效的复位类型: {reset_type}. 有效值: {list(NMT_COMMANDS.keys())}")
    
    # 获取复位命令代码
    command = NMT_COMMANDS[reset_type]
    
    try:
        # 创建 CAN 总线接口
        bus = can.Bus(
            interface='socketcan',
            channel=interface,
            bitrate=bitrate
        )
        
        # 构造 NMT 广播消息 (COB-ID = 0)
        # 数据格式: [命令, 节点ID] (节点ID=0 表示广播)
        msg = can.Message(
            arbitration_id=0x000,  # NMT COB-ID
            data=[command, 0x00],  # 命令 + 广播地址
            is_extended_id=False    # 标准帧 (11位标识符)
        )
        
        # 发送消息
        bus.send(msg)
        print(f"✅ 已广播发送 {reset_type} 指令 (命令字节: 0x{command:02X})")
        
        # 可选: 等待并接收响应 (演示用)
        print("\n监听响应 (3秒)...")
        start_time = time.time()
        while time.time() - start_time < 3:
            response = bus.recv(timeout=1.0)
            if response:
                cob_id = response.arbitration_id
                data_hex = ' '.join([f"{byte:02X}" for byte in response.data])
                print(f"  CAN ID: 0x{cob_id:03X} | 数据: {data_hex}")
    
    except can.CanError as e:
        print(f"❌ CAN 通信错误: {e}")
    except KeyboardInterrupt:
        print("\n操作已取消")
    finally:
        # 确保关闭总线
        if 'bus' in locals() and bus:
            bus.shutdown()
            print("CAN 总线已关闭")

if __name__ == "__main__":
    # 命令行参数解析
    parser = argparse.ArgumentParser(
        description="CANopen NMT 复位指令广播工具",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-i', '--interface', default='can1', 
                        help='CAN 接口名称')
    parser.add_argument('-b', '--bitrate', type=int, default=1000000,
                        help='CAN 总线波特率')
    parser.add_argument('-t', '--type', choices=list(NMT_COMMANDS.keys()), 
                        default='reset_node',
                        help='复位类型: reset_node(复位节点), reset_com(复位通信)')
    
    args = parser.parse_args()
    
    # 打印配置信息
    print(f"CANopen NMT 复位广播指令")
    print(f"------------------------------------")
    print(f"接口:      {args.interface}")
    print(f"波特率:    {args.bitrate} bps")
    print(f"复位类型:  {args.type}")
    print(f"------------------------------------")
    
    # 发送复位指令
    send_reset_command(
        interface=args.interface,
        bitrate=args.bitrate,
        reset_type=args.type
    )