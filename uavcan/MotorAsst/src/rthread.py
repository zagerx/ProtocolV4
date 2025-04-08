import asyncio
import logging
from PyQt6.QtCore import QThread, pyqtSignal, QMutex, QMutexLocker, Qt
from MotorAsst.src.can_service import CanBusService
from config import AppConfig

class DataRThread(QThread):
    started = pyqtSignal()
    stopped = pyqtSignal()
    data_received = pyqtSignal(str, dict)  # (type, data)

    def __init__(self, config: AppConfig):
        super().__init__()
        self._config = config
        self._service = CanBusService(config)
        self._loop = None
        self._mutex = QMutex()
        self._should_run = False
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(logging.DEBUG)

        # 信号转发
        self._service.heartbeat_received.connect(
            lambda d: self._safe_emit("heartbeat", d),
            Qt.ConnectionType.QueuedConnection
        )
        self._service.odometry_received.connect(
            lambda d: self._safe_emit("odometry", d),
            Qt.ConnectionType.QueuedConnection
        )
        self._service.error_occurred.connect(
            lambda m: self._safe_emit("error", {"message": m}),
            Qt.ConnectionType.QueuedConnection
        )

    def connect_signals(self, handlers: dict):
        """连接信号到处理函数"""
        self._logger.debug(f"连接信号处理器: {list(handlers.keys())}")
        
        if "heartbeat_received" in handlers:
            self.data_received.connect(
                lambda typ, data, h=handlers["heartbeat_received"]: h(data) if typ == "heartbeat" else None,
                Qt.ConnectionType.QueuedConnection
            )
        if "odometry_received" in handlers:
            self.data_received.connect(
                lambda typ, data, h=handlers["odometry_received"]: h(data) if typ == "odometry" else None,
                Qt.ConnectionType.QueuedConnection
            )
        if "error_occurred" in handlers:
            self.data_received.connect(
                lambda typ, data, h=handlers["error_occurred"]: h(data["message"]) if typ == "error" else None,
                Qt.ConnectionType.QueuedConnection
            )

    def _safe_emit(self, data_type: str, data: dict):
        """线程安全的信号发射"""
        with QMutexLocker(self._mutex):
            if self._should_run:
                self._logger.debug(f"发射信号: {data_type} - {data}")
                self.data_received.emit(data_type, data)

    def run(self):
        """线程主循环"""
        self._logger.info("CAN通信线程启动")
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)

        async def _run_service():
            try:
                if await self._service.start():
                    with QMutexLocker(self._mutex):
                        self._should_run = True
                    self.started.emit()
                    self._logger.info("CAN服务已启动")
                    
                    while self._is_running():
                        await asyncio.sleep(0.1)
                        
                else:
                    self._logger.error("CAN服务启动失败")
            except Exception as e:
                self._logger.error(f"服务运行异常: {e}", exc_info=True)
                self._safe_emit("error", {"message": str(e)})
            finally:
                await self._service.stop()
                self.stopped.emit()

        try:
            self._loop.run_until_complete(_run_service())
        except Exception as e:
            self._logger.error(f"事件循环异常: {e}", exc_info=True)
        finally:
            if self._loop.is_running():
                self._loop.close()
            self._logger.info("CAN线程已退出")

    def _is_running(self) -> bool:
        """线程安全的状态检查"""
        with QMutexLocker(self._mutex):
            return self._should_run

    def stop(self):
        """停止线程"""
        self._logger.info("请求停止CAN线程")
        with QMutexLocker(self._mutex):
            self._should_run = False
        
        if self._loop and self._loop.is_running():
            def _safe_stop():
                for task in asyncio.all_tasks(self._loop):
                    task.cancel()
                self._loop.stop()
            self._loop.call_soon_threadsafe(_safe_stop)
        
        self.wait(2000)