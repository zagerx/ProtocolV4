from dataclasses import dataclass
from pathlib import Path

@dataclass
class LoggingConfig:
    """日志配置"""
    level: str = "INFO"
    file: Path = Path("motor_assistant.log")  # 修改为直接输出到当前目录
    max_size: int = 10  # MB
    backup_count: int = 3
    enable_console: bool = False  # 新增控制台输出开关

@dataclass
class AppConfig:
    """应用层配置"""
    logging: LoggingConfig
    debug: bool = False

    @classmethod
    def default(cls):
        return cls(
            logging=LoggingConfig(),
            debug=False
        )