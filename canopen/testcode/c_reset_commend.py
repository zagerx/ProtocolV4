#!/usr/bin/env python3
"""
CANopen 通信复位指令脚本
功能：通过 CAN 接口广播发送通信复位指令 (Reset Communication)
作者：CANopen 专家
日期：2023-10-15
"""

import argparse
import can
import time
import sys

def send_communication_reset(interface='can1', bitrate=1000000, node_id=0):
    """
    发送 CANopen 通信复位指令
    
    参数:
        interface: CAN 接口名称 (默认 'can1')
        bitrate: CAN 波特率 (默认 1Mbps)
        node_id: 目标节点ID (0 表示广播所有节点)
    """
    try:
        # 创建 CAN 总线接口
        bus = can.Bus(
            interface='socketcan',
            channel=interface,
            bitrate=bitrate
        )
        
        # 构造 NMT 通信复位消息 (COB-ID = 0)
        # 数据格式: [命令, 节点ID] 
        # 通信复位命令: 0x82
        # 节点ID=0 表示广播所有节点
        msg = can.Message(
            arbitration_id=0x000,  # NMT COB-ID
            data=[0x82, node_id],  # 通信复位命令 + 节点ID
            is_extended_id=False    # 标准帧 (11位标识符)
        )
        
        # 发送消息
        bus.send(msg)
        
        if node_id == 0:
            print(f"✅ 已广播发送通信复位指令 (Reset Communication) 到所有节点")
        else:
            print(f"✅ 已发送通信复位指令 (Reset Communication) 到节点 {node_id}")
        
        # 可选: 监听响应
        print(f"\n监听响应 (3秒)...")
        start_time = time.time()
        response_count = 0
        
        while time.time() - start_time < 3:
            response = bus.recv(timeout=1.0)
            if response:
                response_count += 1
                cob_id = response.arbitration_id
                data_hex = ' '.join([f"{byte:02X}" for byte in response.data])
                
                # 解析 NMT 状态消息 (COB-ID = 0x700 + Node-ID)
                if 0x700 <= cob_id <= 0x77F:
                    source_node = cob_id - 0x700
                    state_byte = response.data[0] if response.data else 0
                    
                    # 解析 NMT 状态
                    states = {
                        0: "初始化",
                        4: "停止",
                        5: "运行",
                        127: "预运行"
                    }
                    state = states.get(state_byte, f"未知({state_byte})")
                    
                    print(f"  节点 {source_node}: NMT 状态 = {state}")
                else:
                    print(f"  CAN ID: 0x{cob_id:03X} | 数据: {data_hex}")
        
        if response_count == 0:
            print("  未收到任何响应")
    
    except can.CanError as e:
        print(f"❌ CAN 通信错误: {e}")
        return False
    except KeyboardInterrupt:
        print("\n操作已取消")
        return False
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        return False
    finally:
        # 确保关闭总线
        if 'bus' in locals() and bus:
            bus.shutdown()
            print("CAN 总线已关闭")
    
    return True

def main():
    # 命令行参数解析
    parser = argparse.ArgumentParser(
        description="CANopen 通信复位指令工具",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-i', '--interface', default='can1', 
                        help='CAN 接口名称')
    parser.add_argument('-b', '--bitrate', type=int, default=1000000,
                        help='CAN 总线波特率')
    parser.add_argument('-n', '--node', type=int, default=0,
                        help='目标节点ID (0 表示广播所有节点)')
    
    args = parser.parse_args()
    
    # 验证节点ID
    if args.node < 0 or args.node > 127:
        print("❌ 错误: 节点ID必须在 0-127 范围内")
        sys.exit(1)
    
    # 打印配置信息
    print(f"CANopen 通信复位指令")
    print(f"------------------------------------")
    print(f"接口:      {args.interface}")
    print(f"波特率:    {args.bitrate} bps")
    if args.node == 0:
        print(f"目标:      所有节点 (广播)")
    else:
        print(f"目标:      节点 {args.node}")
    print(f"------------------------------------")
    
    # 发送通信复位指令
    success = send_communication_reset(
        interface=args.interface,
        bitrate=args.bitrate,
        node_id=args.node
    )
    
    # 根据执行结果退出
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()