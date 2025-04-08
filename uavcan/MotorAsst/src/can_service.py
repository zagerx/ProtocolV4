import asyncio
import logging
from typing import Dict, Callable, Optional
from PyQt6.QtCore import QObject, pyqtSignal
from pycyphal.transport import Transport
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from config import AppConfig
from MotorAsst.lib.sub_heart import HeartbeatMonitor
from MotorAsst.lib.sub_odom import OdomMonitor
from pycyphal.application import make_node, NodeInfo

class CanBusService(QObject):
    heartbeat_received = pyqtSignal(dict)
    odometry_received = pyqtSignal(dict)
    error_occurred = pyqtSignal(str)

    def __init__(self, config: AppConfig):
        super().__init__()
        self._config = config
        self._running = False
        self._transport: Optional[Transport] = None
        self._monitors: Dict[str, object] = {}
        self._tasks: list[asyncio.Task] = []
        self._logger = logging.getLogger(self.__class__.__name__)

    async def start(self) -> bool:
        try:
            media = SocketCANMedia(self._config.can.interface, mtu=self._config.can.mtu)
            self._transport = CANTransport(media, local_node_id=self._config.can.node_id)
            
            self._monitors = {
                "heartbeat": HeartbeatMonitor(self._transport, self._config.can.heartbeat_port),
                "odometry": OdomMonitor(self._transport, self._config.can.odometry_port)
            }
            
            await asyncio.gather(*[m.initialize() for m in self._monitors.values()])
            
            self._running = True
            self._tasks = [
                asyncio.create_task(self._monitor_loop(
                    "heartbeat", 
                    self._config.can.timeout,
                    self.heartbeat_received
                )),
                asyncio.create_task(self._monitor_loop(
                    "odometry",
                    self._config.can.timeout,
                    self.odometry_received
                ))
            ]
            return True
        except Exception as e:
            self.error_occurred.emit(f"启动失败: {str(e)}")
            return False

    async def _monitor_loop(self, name: str, timeout: float, signal: pyqtSignal) -> None:
        while self._running:
            success, data = await self._monitors[name].monitor(timeout)
            if success:
                signal.emit(data)
            else:
                self._logger.debug("%s timeout", name)

    async def stop(self) -> None:
        self._running = False
        if self._tasks:
            await asyncio.gather(*self._tasks, return_exceptions=True)
        if self._monitors:
            await asyncio.gather(*[m.close() for m in self._monitors.values()], return_exceptions=True)
        if self._transport:
            self._transport.close()