import asyncio
import logging
from typing import List,Optional,Callable
from MotorAsst.config.configdrivers import MonitorConfig
from MotorAsst.drivers.can.transport import CANNodeService
class MonitorThread:
    def __init__(
        self, 
        node_service: CANNodeService, 
        monitor_configs: List[MonitorConfig],
        # ui_callback: Optional[Callable[[str, dict], None]] = None
    ):
        self.node_service = node_service
        self.monitor_configs = monitor_configs
        self.tasks = []
        # self.ui_callback = ui_callback  # UI回调函数
        self._logger = logging.getLogger(self.__class__.__name__)
    async def start(self):
        """启动所有监控任务"""
        for monitor_cfg in self.monitor_configs:
            if not monitor_cfg.enabled:
                continue
                
            subscriber = self.node_service.create_subscriber(
                monitor_cfg.data_type,
                monitor_cfg.port
            )
            if not subscriber:
                continue
            self.tasks.append(asyncio.create_task(
                self._run_monitor(
                    monitor_cfg.monitor_class(subscriber),
                    monitor_cfg.display_name
                )
            ))
    async def _run_monitor(self, monitor, name: str):
        """监控任务运行逻辑（与原run_monitor一致）"""
        try:
            while True:
                success, data = await monitor.monitor(1.0)
                if success:
                    # 1. 记录日志
                    self._logger.info(self._format_data(name, data))
                    # 2. 触发UI更新
                    # if self.ui_callback:
                    #     self.ui_callback(name, data)
        except asyncio.CancelledError:
            pass

    def _format_data(self, name: str, data: dict) -> str:
        """数据格式化（与原_format_data一致）"""
        msg, transfer = data        
        if name == "Odometry":
            # 处理里程计数据
            return (
                f"TS={transfer.timestamp.monotonic:.3f}ms | "
                f"Left: v={msg.current_velocity[0].meter_per_second:.3f}m/s "
                f"o={msg.odometry[0].meter:.3f}m | "
                f"Right: v={msg.current_velocity[1].meter_per_second:.3f}m/s "
                f"o={msg.odometry[1].meter:.3f}m"
            )
        if name == "heartbeat":
            return (
                f"node_id={transfer.source_node_id}, "
                f"mode={msg.mode.value}, "
                f"health={msg.health.value}, "
                f"uptime={msg.uptime}"
            )
        return str(data)

    async def stop(self):
        """停止所有监控任务"""
        for task in self.tasks:
            task.cancel()
        await asyncio.gather(*self.tasks, return_exceptions=True)