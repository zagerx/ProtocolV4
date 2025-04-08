from dataclasses import dataclass
from typing import List
from enum import Enum

class MonitorType(Enum):
    HEARTBEAT = "heartbeat"
    ODOMETRY = "odometry"

@dataclass
class MonitorConfig:
    type: MonitorType
    port: int
    enabled: bool = True

@dataclass
class CanConfig:
    interface: str = "can1"
    node_id: int = 28
    mtu: int = 8
    timeout: float = 2.0
    monitors: List[MonitorConfig] = None

    def __post_init__(self):
        if self.monitors is None:
            self.monitors = [
                MonitorConfig(MonitorType.HEARTBEAT, 7509),
                MonitorConfig(MonitorType.ODOMETRY, 1100)
            ]

@dataclass
class UIConfig:
    refresh_interval: int = 500  # ms
    decimal_precision: int = 3

@dataclass
class AppConfig:
    can: CanConfig
    ui: UIConfig

    @classmethod
    def default(cls):
        return cls(
            can=CanConfig(),
            ui=UIConfig()
        )