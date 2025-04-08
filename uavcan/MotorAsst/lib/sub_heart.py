#!/usr/bin/env python3
import asyncio
import logging
from typing import Optional, Tuple
import pycyphal
from pycyphal.application import make_node, NodeInfo
from uavcan.node import Heartbeat_1_0, Version_1_0

class HeartbeatMonitor:
    def __init__(self, transport: pycyphal.transport.Transport, port: int):
        self._transport = transport
        self._port = port
        self._node: Optional[pycyphal.application.Node] = None
        self._sub: Optional[pycyphal.presentation.Subscriber] = None
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(logging.DEBUG)

    async def initialize(self) -> None:
        """初始化节点和订阅器"""
        try:
            self._logger.info(f"初始化心跳监控器, port={self._port}")
            
            self._node = make_node(
                transport=self._transport,
                info=NodeInfo(
                    name="heartbeat_monitor",
                    software_version=Version_1_0(major=1, minor=0),
                    unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF01")
                )
            )
            self._node.start()
            self._sub = self._node.make_subscriber(Heartbeat_1_0, self._port)
            self._logger.info(f"已创建订阅器, 端口: {self._port}")
        except Exception as e:
            self._logger.error(f"初始化失败: {e}", exc_info=True)
            raise
        
    async def monitor(self, timeout: float) -> Tuple[bool, Optional[dict]]:
        """监听心跳数据"""
        try:
            result = await asyncio.wait_for(
                self._sub.receive(monotonic_deadline=asyncio.get_event_loop().time() + timeout),
                timeout=timeout
            )
            
            if result:
                msg, transfer = result
                data = {
                    "node_id": transfer.source_node_id,
                    "mode": int(msg.mode.value),
                    "health": int(msg.health.value),
                    "uptime": msg.uptime
                }
                self._logger.info(f"解析到心跳数据: {data}")
                return True, data
                
        except asyncio.TimeoutError:
            self._logger.error("心跳监听超时")
        except Exception as e:
            self._logger.error(f"监听异常: {e}", exc_info=True)
            
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