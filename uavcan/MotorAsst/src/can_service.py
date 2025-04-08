import asyncio
import logging
import importlib
import sys
from typing import Dict, Optional
from PyQt6.QtCore import QObject, pyqtSignal, Qt
from pycyphal.transport import Transport
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from config import AppConfig, MonitorType, MonitorConfig

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
        self._logger.setLevel(logging.DEBUG)

    async def start(self) -> bool:
        """启动服务"""
        try:
            self._logger.info(f"初始化CAN接口: {self._config.can.interface}")
            media = SocketCANMedia(self._config.can.interface, mtu=self._config.can.mtu)
            self._logger.debug(f"Media对象创建成功: {media}")
            
            self._transport = CANTransport(media, local_node_id=self._config.can.node_id)
            self._logger.debug(f"传输层对象创建成功 (ID: {id(self._transport)})")

            # 初始化监控器
            init_tasks = []
            for cfg in self._config.can.monitors:
                if cfg.enabled:
                    self._logger.debug(f"初始化监控器: {cfg.type.value} (port={cfg.port})")
                    monitor = self._create_monitor(cfg.type, cfg.port)
                    if monitor:
                        init_tasks.append(monitor.initialize())
                        self._monitors[cfg.type.value] = monitor
                    else:
                        self._logger.error(f"无法创建监控器: {cfg.type.value}")

            await asyncio.gather(*init_tasks)
            self._logger.info(f"已初始化 {len(self._monitors)} 个监控器")

            # 启动监控循环
            self._running = True
            for name, monitor in self._monitors.items():
                task = asyncio.create_task(self._monitor_loop(name, monitor))
                self._tasks.append(task)
                self._logger.debug(f"已启动 {name} 监控循环")
            
            return True
            
        except Exception as e:
            self._logger.critical(f"服务启动失败: {e}", exc_info=True)
            self.error_occurred.emit(f"启动失败: {str(e)}")
            return False

    def _create_monitor(self, m_type: MonitorType, port: int):
        """创建监控器实例（修正字典键问题）"""
        self._logger.debug(f"创建监控器 {m_type.value} (port={port})")
        
        # 修正：使用枚举值作为键
        module_map = {
            "heartbeat": "sub_heart",
            "odometry": "sub_odom"
        }
        
        try:
            module_name = f"MotorAsst.lib.{module_map[m_type.value]}"
            class_name = f"{m_type.name.capitalize()}Monitor"
            
            self._logger.debug(f"导入模块: {module_name}")
            module = importlib.import_module(module_name)
            monitor_class = getattr(module, class_name)
            
            self._logger.debug(f"成功获取类: {monitor_class}")
            
            # 创建实例
            monitor = monitor_class(self._transport, port)
            self._logger.debug(f"监控器实例创建成功: {monitor}")
            return monitor
            
        except Exception as e:
            self._logger.error(f"创建监控器失败: {type(e).__name__}: {e}", exc_info=True)
            return None

    async def _monitor_loop(self, name: str, monitor: object):
        """监控循环"""
        signal = getattr(self, f"{name}_received")
        self._logger.debug(f"开始 {name} 监控循环")
        
        while self._running:
            try:
                success, data = await monitor.monitor(self._config.can.timeout)
                if success:
                    self._logger.debug(f"准备发射 {name} 信号: {data}")
                    signal.emit(data)
                    self._logger.debug(f"{name} 信号已发射")
                else:
                    self._logger.debug(f"{name} 未收到数据")
            except asyncio.CancelledError:
                self._logger.debug(f"{name} 监控循环被取消")
                break
            except Exception as e:
                self._logger.error(f"{name}监控异常: {e}", exc_info=True)

    async def stop(self):
        """停止服务"""
        self._logger.info("开始停止CAN服务")
        self._running = False
        
        for task in self._tasks:
            task.cancel()
        await asyncio.gather(*self._tasks, return_exceptions=True)
        
        for name, monitor in self._monitors.items():
            try:
                await monitor.close()
                self._logger.debug(f"已关闭 {name} 监控器")
            except Exception as e:
                self._logger.error(f"关闭监控器 {name} 失败: {e}")
        
        if self._transport:
            self._transport.close()
            
        self._logger.info("CAN服务已完全停止")