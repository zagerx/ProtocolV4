import asyncio
import logging
from typing import List
from MotorAsst.config.configdrivers import MonitorConfig
from MotorAsst.drivers.can.transport import CANNodeService
class MonitorThread:
    def __init__(self, node_service: CANNodeService, monitor_configs: List[MonitorConfig]):
        self.node_service = node_service
        self.monitor_configs = monitor_configs
        self.tasks = []

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
                    logging.getLogger(name).info(self._format_data(name, data))
        except asyncio.CancelledError:
            pass

    def _format_data(self, name: str, data: dict) -> str:
        """数据格式化（与原_format_data一致）"""
        if name == "Odometry":
            return (
                f"TS={data['timestamp']:.3f}ms | "
                f"Left: v={data['left_velocity']:.3f}m/s o={data['left_odometry']:.3f}m | "
                f"Right: v={data['right_velocity']:.3f}m/s o={data['right_odometry']:.3f}m"
            )
        return str(data)

    async def stop(self):
        """停止所有监控任务"""
        for task in self.tasks:
            task.cancel()
        await asyncio.gather(*self.tasks, return_exceptions=True)