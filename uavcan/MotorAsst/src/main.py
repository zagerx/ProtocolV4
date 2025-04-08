#!/usr/bin/env python3
import sys
import logging
from PyQt6.QtWidgets import QApplication
from MotorAsst.ui.window_main import MainWindow
from MotorAsst.src.rthread import CanThread
from MotorAsst.src.config import AppConfig

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    setup_logging()
    app = QApplication(sys.argv)
    
    # 初始化
    config = AppConfig.default()
    window = MainWindow()
    can_thread = CanThread(config)
    
    # 连接信号
    can_thread.connect_signals({
        "heartbeat_received": window.handle_heartbeat,
        "odometry_received": window.handle_odometry,
        "error_occurred": window.handle_error
    })
    
    # 启动
    window.can_thread = can_thread  # 保持引用
    can_thread.start()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()