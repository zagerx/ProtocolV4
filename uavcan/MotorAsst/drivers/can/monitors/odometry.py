import asyncio
import logging
from typing import Tuple, Optional
from dinosaurs.actuator.wheel_motor import OdometryAndVelocityPublish_1_0
from .base import BaseMonitor

class OdometryMonitor(BaseMonitor):
    """
    里程计监控器实现
    协议: dinosaurs.actuator.wheel_motor.OdometryAndVelocityPublish_1.0
    """
    def __init__(self, subscriber):
        super().__init__(transport=None, port=0)
        self._subscriber = subscriber
        self._logger = logging.getLogger(self.__class__.__name__)
        self._initialized = True

    async def initialize(self) -> bool:
        """实现抽象方法"""
        return True  # 实际初始化由服务层完成

    async def monitor(self, timeout: float) -> Tuple[bool, Optional[dict]]:
        try:
            result = await self._subscriber.receive(
                monotonic_deadline=asyncio.get_event_loop().time() + timeout
            )
            if result:
                msg, transfer = result
                return True, {
                    "timestamp": transfer.timestamp.monotonic,
                    "left_velocity": msg.current_velocity[0].meter_per_second,
                    "right_velocity": msg.current_velocity[1].meter_per_second,
                    "left_odometry": msg.odometry[0].meter,
                    "right_odometry": msg.odometry[1].meter
                }
            return False, None
        except Exception as e:
            self._logger.error(f"Monitor error: {e}")
            return False, None

    async def close(self):
        """同步关闭方法"""
        if hasattr(self, '_subscriber') and self._subscriber:
            try:
                self._subscriber.close()
            except Exception as e:
                logging.warning(f"Subscriber close error: {e}")
            finally:
                self._subscriber = None