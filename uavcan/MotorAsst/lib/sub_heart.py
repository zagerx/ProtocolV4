#!/usr/bin/env python3
"""
订阅 CAN 总线上的节点心跳包（uavcan.node.Heartbeat）
需要先运行 compile_dsdl.py 生成 DSDL 定义
"""
import asyncio
import pycyphal
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Heartbeat_1_0, Version_1_0

class HeartbeatMonitor:
    def __init__(self, can_interface="can1", local_node_id=28):
        self.can_interface = can_interface
        self.local_node_id = local_node_id
        self.media = None
        self.transport = None
        self.node = None
        self.sub = None

    async def initialize(self):
        # 初始化 CAN 接口和传输层
        self.media = SocketCANMedia(self.can_interface, mtu=8)
        self.transport = CANTransport(self.media, local_node_id=self.local_node_id)
        
        # 创建节点（显式启动）
        self.node = make_node(
            transport=self.transport,
            info=NodeInfo(
                name="test_node",
                software_version=Version_1_0(major=1, minor=0),
                unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF01")
            )
        )
        self.node.start()  # 必须显式启动
        
        # 创建订阅者
        self.sub = self.node.make_subscriber(Heartbeat_1_0, 7509)
        print(f"正在监听 {self.can_interface} 上的心跳包...")

    async def monitor_heartbeat(self, timeout=2.0):
        if self.sub is None:
            print("错误: 订阅者未初始化")
            return

        try:
            # 计算超时时间（当前时间 + timeout 秒）
            deadline = asyncio.get_event_loop().time() + timeout
            
            # 接收消息（带超时）
            result = await asyncio.wait_for(self.sub.receive(monotonic_deadline=deadline), timeout=timeout)
            if result is not None:
                msg, transfer = result
                print(f"\n心跳包来自节点 {transfer.source_node_id}:")
                print(f"- 运行状态: {msg.mode}")
                print(f"- 健康状况: {msg.health}")
                print(f"- Uptime: {msg.uptime} 秒")
                return True
            else:
                print("错误: 未接收到心跳包")
                return False
        except asyncio.TimeoutError:
            print(f"错误: {timeout} 秒内未接收到心跳包")
            return False
        except Exception as e:
            print(f"错误: {e}")
            return False

    async def close(self):
        # 显式关闭所有资源（关键！）
        if self.sub:
            self.sub.close()
        if self.node:
            self.node.close()
        if self.transport:
            self.transport.close()
        if self.media:
            self.media.close()
        print("所有资源已关闭")

    async def __aenter__(self):
        await self.initialize()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

# # 示例用法
# async def main():
#     async with HeartbeatMonitor(can_interface="can1", local_node_id=28) as monitor:
#         await monitor.monitor_heartbeat(timeout=1.0)

# if __name__ == "__main__":
#     asyncio.run(main())