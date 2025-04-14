from dataclasses import dataclass
from typing import Type, Any, List, Dict
from uavcan.node import Heartbeat_1_0
from dinosaurs.actuator.wheel_motor import OdometryAndVelocityPublish_1_0, Enable_1_0
from MotorAsst.drivers.can.monitors.base import BaseMonitor
from MotorAsst.drivers.can.monitors.heartbeat import HeartbeatMonitor
from MotorAsst.drivers.can.monitors.odometry import OdometryMonitor

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
    data_type: Type[Any]        # 协议数据类型类
    port: int                   # 端口号
    monitor_class: Type[BaseMonitor]
    display_name: str           # 显示名称
    enabled: bool = True

@dataclass
class CommandConfig:
    """命令配置"""
    data_type: Type[Any]        # 协议数据类型类
    server_node_id: int         # 目标节点ID
    port: int                   # 端口号
    timeout: float              # 超时时间(秒)
    display_name: str           # 显示名称
    enabled: bool = True

@dataclass 
class DriverConfig:
    """驱动层总配置"""
    can: CanConfig
    monitors: List[MonitorConfig]
    commands: Dict[str, CommandConfig]  # 命令配置字典

    @classmethod
    def default(cls):
        return cls(
            can=CanConfig(),
            monitors=[
                MonitorConfig(
                    data_type=Heartbeat_1_0,
                    port=7509,
                    monitor_class=HeartbeatMonitor,
                    display_name="Heartbeat"
                ),
                MonitorConfig(
                    data_type=OdometryAndVelocityPublish_1_0,
                    port=1100,
                    monitor_class=OdometryMonitor,
                    display_name="Odometry"
                )
            ],
            commands={
                "MotorEnable": CommandConfig(
                    data_type=Enable_1_0,
                    server_node_id=28,
                    port=113,
                    timeout=0.2,
                    display_name="Motor Enable"
                )
            }
        )