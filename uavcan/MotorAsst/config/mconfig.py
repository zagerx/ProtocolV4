import logging
from typing import Optional
from pathlib import Path
import yaml

from MotorAsst.config.configdrivers import DriverConfig
from MotorAsst.config.configapp import AppConfig

class ConfigManager:
    """
    配置管理器（单例模式）
    功能：
    1. 分层配置管理
    2. 文件持久化
    3. 环境变量覆盖
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_config()
        return cls._instance

    def _init_config(self):
        self.driver = DriverConfig.default()
        self.app = AppConfig.default()
        self._config_file: Optional[Path] = None

    def load(self, file_path: str) -> bool:
        """从YAML加载配置"""
        try:
            path = Path(file_path)
            with open(path) as f:
                data = yaml.safe_load(f) or {}
            
            # 更新驱动配置
            if 'driver' in data:
                driver_data = data['driver']
                if 'can' in driver_data:
                    self.driver.can.__dict__.update(driver_data['can'])
                if 'monitors' in driver_data:
                    self._update_monitors(driver_data['monitors'])

            # 更新应用配置
            if 'app' in data:
                self.app.__dict__.update(data['app'])

            self._config_file = path
            return True
        except Exception as e:
            logging.error(f"Config load error: {e}")
            return False

    def _update_monitors(self, monitors_data: list):
        """动态更新监控器配置"""
        for cfg in self.driver.monitors:
            for data in monitors_data:
                if cfg.data_type.__name__ == data.get('data_type'):
                    cfg.enabled = data.get('enabled', True)
                    break

    def save(self, file_path: Optional[str] = None) -> bool:
        """保存配置到YAML"""
        path = Path(file_path) if file_path else self._config_file
        if not path:
            return False

        try:
            data = {
                'driver': {
                    'can': self.driver.can.__dict__,
                    'monitors': [
                        {'data_type': m.data_type.__name__, 'port': m.port, 'enabled': m.enabled}
                        for m in self.driver.monitors
                    ]
                },
                'app': self.app.__dict__
            }
            path.parent.mkdir(exist_ok=True)
            with open(path, 'w') as f:
                yaml.dump(data, f, sort_keys=False)
            return True
        except Exception as e:
            logging.error(f"Config save error: {e}")
            return False