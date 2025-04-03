# src/mcAsst.py
import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QObject, pyqtSignal

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.window.ui_main import Ui_MainWindow
from src.rThread import HeartbeatMonitorThread

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_button_click)
        self.heartbeat_thread = None

    def on_button_click(self):
        print("按钮被点击！")
        if not self.heartbeat_thread or not self.heartbeat_thread.is_alive():
            self.start_heartbeat_monitor()

    def start_heartbeat_monitor(self):
        self.heartbeat_thread = HeartbeatMonitorThread()
        self.heartbeat_thread.start()
        print("心跳监听线程已启动")

    def closeEvent(self, event):
        if self.heartbeat_thread:
            self.heartbeat_thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
