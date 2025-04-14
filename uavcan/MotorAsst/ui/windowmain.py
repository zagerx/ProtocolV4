from PyQt6.QtWidgets import QMainWindow
from MotorAsst.ui.uimain import Ui_MainWindow

class MainWindow(QMainWindow):
    """
    主窗口类，封装UI界面和基本功能
    """
    def __init__(self):
        super().__init__()
        # 初始化UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # 设置窗口标题
        self.setWindowTitle("电机监控系统")
        
        # 可以在这里添加其他初始化代码
        self._setup_connections()
        # 状态组
        self._init_status_group()
        

    def _setup_connections(self):
        """初始化信号槽连接"""
        # 示例：连接按钮点击信
        # self.ui.OpBt.clicked.connect(self._on_open_serial)
        pass
    def _init_status_group(self):
        """初始化状态显示组件"""
        self.ui.lineEdit_5_1.setReadOnly(True)
        # self.ui.lineEdit_5_1.setFrame(False)
    
    # 可以在这里添加其他方法
    # def _on_open_serial(self):
    #     """处理打开串口按钮点击"""
    #     pass