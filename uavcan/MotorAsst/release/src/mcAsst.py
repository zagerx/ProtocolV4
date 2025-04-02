
import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow  # 替换 QWidget 为 QMainWindow

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.window.ui_main import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):  
    def __init__(self):  
        super().__init__()  
        self.setupUi(self)  
        self.pushButton.clicked.connect(self.on_button_click)  # 绑定信号与槽‌:ml-citation{ref="5,6" data="citationList"}  

    def on_button_click(self):  
        print("按钮被点击！")  

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
