import sys
import os

# 路径设置
# ui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ui")
# sys.path.append(os.path.normpath(ui_dir))

from PyQt6.QtWidgets import QApplication
from rthread import BaseCanThread
from MotorAsst.ui.window_main import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # 初始化CAN线程
    can_thread = BaseCanThread()
    can_thread.register_handler("heartbeat", window.handle_heartbeat)
    can_thread.start()

    window.show()
    ret = app.exec()
    
    # 清理
    can_thread.stop()
    sys.exit(ret)

if __name__ == "__main__":
    main()