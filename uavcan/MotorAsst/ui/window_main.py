from PyQt6.QtWidgets import QMainWindow, QLabel
from MotorAsst.ui.ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 手动添加状态标签
        self.status_label = QLabel("状态: 初始化...", self)
        self.statusbar.addPermanentWidget(self.status_label)  # 添加到状态栏
        
        self.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("控制指令已发送")

    def handle_heartbeat(self, data):
        """处理心跳数据"""
        status_text = f"节点 {data['node_id']} | 模式: {self._parse_mode(data['mode'])} | 健康: {self._parse_health(data['health'])}"
        print(f"[状态更新] {status_text}")
        self.status_label.setText(status_text)
    
    def _parse_mode(self, mode_str):
        """解析模式枚举值"""
        mode_map = {
            "value=0": "OPERATIONAL",
            "value=1": "INITIALIZATION",
            "value=2": "MAINTENANCE",
            "value=3": "SOFTWARE_UPDATE"
        }
        return mode_map.get(mode_str.split("(")[-1].rstrip(")"), mode_str)

    def _parse_health(self, health_str):
        """解析健康状态枚举值"""
        health_map = {
            "value=0": "NOMINAL",
            "value=1": "ADVISORY",
            "value=2": "CAUTION",
            "value=3": "WARNING"
        }
        return health_map.get(health_str.split("(")[-1].rstrip(")"), health_str)