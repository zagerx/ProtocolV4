#!/usr/bin/env python3
import asyncio
import time
import logging
from typing import Optional, Tuple
import pycyphal
from pycyphal.application import make_node, NodeInfo
from dinosaurs.actuator.wheel_motor import OdometryAndVelocityPublish_1_0
from uavcan.node import Version_1_0

class OdometryMonitor:
    def __init__(self, transport: pycyphal.transport.Transport, port: int):
        self._transport = transport
        self._port = port
        self._node: Optional[pycyphal.application.Node] = None
        self._sub: Optional[pycyphal.presentation.Subscriber] = None
        self._start_time = time.monotonic()
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(logging.DEBUG)

    async def initialize(self) -> None:
        """初始化"""
        self._logger.info(f"初始化里程计监控器, port={self._port}")
        self._node = make_node(
            transport=self._transport,
            info=NodeInfo(
                name="odom_monitor",
                software_version=Version_1_0(major=1, minor=0),
                unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF02")
            )
        )
        self._node.start()
        self._sub = self._node.make_subscriber(OdometryAndVelocityPublish_1_0, self._port)
        self._logger.info(f"已创建里程计订阅器, 端口: {self._port}")

    async def monitor(self, timeout: float) -> Tuple[bool, Optional[dict]]:
        """监听里程计数据"""
        try:
            result = await asyncio.wait_for(
                self._sub.receive(monotonic_deadline=asyncio.get_event_loop().time() + timeout),
                timeout=timeout
            )
            
            if result:
                msg, transfer = result
                ts = int((time.monotonic() - self._start_time) * 1000)
                data = {
                    "timestamp": ts,
                    "left_velocity": msg.current_velocity[0].meter_per_second,
                    "right_velocity": msg.current_velocity[1].meter_per_second,
                    "left_odometry": msg.odometry[0].meter,
                    "right_odometry": msg.odometry[1].meter,
                    "source_node_id": transfer.source_node_id
                }
                self._logger.info(f"解析到里程计数据: {data}")
                return True, data
        except asyncio.TimeoutError:
            self._logger.error("里程计监听超时")
        except Exception as e:
            self._logger.error(f"里程计监听异常: {e}", exc_info=True)
        return False, None

    async def close(self) -> None:
        """释放资源"""
        try:
            if self._sub:
                await self._sub.close()
            if self._node:
                await self._node.close()
        except Exception as e:
            self._logger.error(f"关闭异常: {e}")