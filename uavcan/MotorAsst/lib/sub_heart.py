#!/usr/bin/env python3
import asyncio
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

    async def initialize(self) -> None:
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

    async def monitor(self, timeout: float) -> Tuple[bool, Optional[dict]]:
        try:
            result = await asyncio.wait_for(
                self._sub.receive(monotonic_deadline=asyncio.get_event_loop().time() + timeout),
                timeout=timeout
            )
            if result:
                msg, transfer = result
                return True, {
                    "node_id": transfer.source_node_id,
                    "mode": int(msg.mode.value),
                    "health": int(msg.health.value),
                    "uptime": msg.uptime
                }
        except asyncio.TimeoutError:
            pass
        return False, None

    async def close(self) -> None:
        if self._sub: await self._sub.close()
        if self._node: await self._node.close()