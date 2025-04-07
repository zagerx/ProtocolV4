from PyQt6.QtWidgets import QMainWindow
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("控制指令已发送")
        # 示例：未来可以在这里发送CAN指令

    def handle_heartbeat(self, data):
        """处理心跳数据"""
        print(f"心跳更新: {data}")
        # 更新UI示例：
        status_text = f"节点 {data['node_id']} | 状态: {data['mode']}"
        self.status_label.setText(status_text)