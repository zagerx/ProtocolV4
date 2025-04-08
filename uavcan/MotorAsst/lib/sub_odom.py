#!/usr/bin/env python3
"""
订阅 CAN 总线上的里程计数据（dinosaurs.actuator.wheel_motor.OdometryAndVelocityPublish_1_0）
需要先运行 compile_dsdl.py 生成 DSDL 定义
"""
import asyncio
import time
import pycyphal
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Version_1_0
from dinosaurs.actuator.wheel_motor import OdometryAndVelocityPublish_1_0

class OdomMonitor:
    def __init__(self, can_interface="can1", local_node_id=28):
        self.can_interface = can_interface
        self.local_node_id = local_node_id
        self.media = None
        self.transport = None
        self.node = None
        self.sub = None
        self.start_time = time.monotonic()
        self.prev_odometry = None  # 存储前一时刻的里程计数据

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
        self.sub = self.node.make_subscriber(OdometryAndVelocityPublish_1_0, 1100)
        print(f"正在监听 {self.can_interface} 上的里程计数据...")

    def process_data(self, msg, transfer):
        ts = int((time.monotonic() - self.start_time) * 1000)

        # 提取数据
        l_vel = msg.current_velocity[0].meter_per_second  # 左轮速度
        r_vel = msg.current_velocity[1].meter_per_second  # 右轮速度
        l_odom = msg.odometry[0].meter                    # 左轮里程计
        r_odom = msg.odometry[1].meter                    # 右轮里程计

        # 打印当前数据
        print(f"\n[ODOM] Time: {ts}ms")
        print(f"Left - Velocity: {l_vel:.3f} m/s | Odom: {l_odom:.3f} m")
        print(f"Right - Velocity: {r_vel:.3f} m/s | Odom: {r_odom:.3f} m")

        # 增量检测逻辑
        if self.prev_odometry is not None:
            delta_l = l_odom - self.prev_odometry["l_odom"]
            delta_r = r_odom - self.prev_odometry["r_odom"]
            
            threshold = 0.05
            if abs(delta_l) > threshold or abs(delta_r) > threshold:
                print(f"WARNING: Large delta detected!")
                print(f"Left delta: {delta_l:.3f} m")
                print(f"Right delta: {delta_r:.3f} m")

        self.prev_odometry = {"l_odom": l_odom, "r_odom": r_odom}
        return {
            "timestamp": ts,
            "left_velocity": l_vel,
            "right_velocity": r_vel,
            "left_odometry": l_odom,
            "right_odometry": r_odom,
            "source_node_id": transfer.source_node_id
        }

    async def monitor_odom(self, timeout=2.0):
        try:
            deadline = asyncio.get_event_loop().time() + timeout
            result = await asyncio.wait_for(
                self.sub.receive(monotonic_deadline=deadline),
                timeout=timeout
            )
            if result:
                msg, transfer = result
                return True, self.process_data(msg, transfer)
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
        print("里程计监控资源已关闭")

    async def __aenter__(self):
        await self.initialize()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()