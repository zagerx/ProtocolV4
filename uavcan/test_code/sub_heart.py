#!/usr/bin/env python3
"""
订阅CAN总线上的节点心跳包（uavcan.node.Heartbeat）
仅显示节点ID为16、25和28的心跳
"""
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(".pyFolder").resolve()))
import pycyphal
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Heartbeat_1_0, Version_1_0
import asyncio

# 目标节点ID列表
TARGET_NODE_IDS = {16, 25, 28}

# 健康状态和运行模式的文本映射
HEALTH_MAP = {
    0: "NOMINAL",
    1: "ADVISORY",
    2: "CAUTION",
    3: "WARNING"
}

MODE_MAP = {
    0: "OPERATIONAL",
    1: "INITIALIZATION",
    2: "MAINTENANCE",
    3: "SOFTWARE_UPDATE"
}

async def sub_heart_process() -> None:
    # 初始化 CAN 接口和传输层
    media = SocketCANMedia("can1", mtu=8)
    transport = CANTransport(media, local_node_id=100)
    
    # 创建节点
    node = make_node(
        transport=transport,
        info=NodeInfo(
            name="heartbeat_monitor",
            software_version=Version_1_0(major=1, minor=0),
            unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF01")
        )
    )
    node.start()  # 必须显式启动
    
    # 创建订阅者
    sub = node.make_subscriber(Heartbeat_1_0, 7509)
    
    print(f"监听目标节点心跳包: {TARGET_NODE_IDS}")
    print("按 Ctrl+C 退出")
    
    try:
        while True:
            # 接收消息（带超时）
            result = await sub.receive(asyncio.get_event_loop().time() + 1.0)
            
            if result is not None:
                msg, transfer = result
                node_id = transfer.source_node_id
                
                # 只显示目标节点
                if node_id in TARGET_NODE_IDS:
                    print(f"\n节点 {node_id} 心跳:")
                    print(f"- 运行状态: {MODE_MAP.get(msg.mode.value, '未知')} ({msg.mode.value})")
                    print(f"- 健康状况: {HEALTH_MAP.get(msg.health.value, '未知')} ({msg.health.value})")
                    print(f"- 运行时间: {msg.uptime}秒")
                    print(f"- 供应商状态码: {msg.vendor_specific_status_code}")
    except KeyboardInterrupt:
        print("\n停止监听...")
    finally:
        # 显式关闭所有资源
        sub.close()
        node.close()
        transport.close()
        media.close()

if __name__ == "__main__":
    asyncio.run(sub_heart_process())