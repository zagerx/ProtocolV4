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

    async def initialize_with_transport(self, transport):
        # 初始化 CAN 接口和传输层
        self.transport = transport
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
        try:
            deadline = asyncio.get_event_loop().time() + timeout
            result = await asyncio.wait_for(
                self.sub.receive(monotonic_deadline=deadline),  # 添加必要参数
                timeout=timeout
            )
            if result:
                return True, result  # 返回元组 (success, data)
            return False, None
        except asyncio.TimeoutError:
            return False, None
        except Exception as e:
            print(f"接收错误: {e}")
            return False, None


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