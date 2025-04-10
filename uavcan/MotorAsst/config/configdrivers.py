from dataclasses import dataclass
from typing import Type, Any, List
from uavcan.node import Heartbeat_1_0
from dinosaurs.actuator.wheel_motor import OdometryAndVelocityPublish_1_0

@dataclass
class CanConfig:
    """CAN总线配置"""
    interface: str = "can1"
    node_id: int = 100
    mtu: int = 8
    bitrate: int = 500000

@dataclass
class MonitorConfig:
    """数据监控配置"""
    data_type: Type[Any]  # 协议数据类型类
    port: int             # 端口号
    enabled: bool = True

@dataclass 
class DriverConfig:
    """驱动层总配置"""
    can: CanConfig
    monitors: List[MonitorConfig]

    @classmethod
    def default(cls):
        return cls(
            can=CanConfig(),
            monitors=[
                MonitorConfig(Heartbeat_1_0, 7509),
                MonitorConfig(OdometryAndVelocityPublish_1_0, 1100)
            ]
        )