#!/usr/bin/env python3
import sys
import logging
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QTimer
from MotorAsst.ui.window_main import MainWindow
from MotorAsst.src.rthread import DataRThread
from MotorAsst.src.config import AppConfig

def setup_logging():
    logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('motor_assistant.log')
        ]
    )

def main():
    try:
        setup_logging()
        logger = logging.getLogger('Main')
        logger.info("启动电机助手应用")

        app = QApplication(sys.argv)
        config = AppConfig.default()
        window = MainWindow(config.ui)
        
        # 初始化线程
        thread = DataRThread(config)
        
        # 连接信号
        thread.connect_signals({
            "heartbeat_received": window.handle_heartbeat,
            "odometry_received": window.handle_odometry,
            "error_occurred": window.handle_error
        })

        # 启动
        window.set_controller(thread)
        thread.start()
        window.show()
        
        return app.exec()
        
    except Exception as e:
        logging.critical(f"应用启动失败: {str(e)}", exc_info=True)
        QMessageBox.critical(
            None, 
            "致命错误", 
            f"应用初始化失败:\n{str(e)}\n\n详见日志文件"
        )
        return 1

if __name__ == "__main__":
    sys.exit(main())