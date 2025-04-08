import asyncio
import logging
from PyQt6.QtCore import QThread
from can_service import CanBusService
from config import AppConfig

class CanThread(QThread):
    def __init__(self, config: AppConfig):
        super().__init__()
        self._config = config
        self._service = CanBusService(config)
        self._logger = logging.getLogger(self.__class__.__name__)

    def connect_signals(self, handlers: dict) -> None:
        for sig, handler in handlers.items():
            getattr(self._service, sig).connect(handler)

    def run(self) -> None:
        async def _main():
            if await self._service.start():
                self._logger.info("CAN服务已启动")
                while getattr(self._service, '_running', False):
                    await asyncio.sleep(1)
            await self._service.stop()

        asyncio.run(_main())

    def stop(self) -> None:
        self._service._running = False
        self.wait()