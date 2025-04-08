from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class CanConfig:
    interface: str = "can1"
    node_id: int = 28
    heartbeat_port: int = 7509
    odometry_port: int = 1100
    mtu: int = 8
    timeout: float = 2.0

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