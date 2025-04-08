#!/usr/bin/env python3
"""
主窗口界面，负责:
1. 显示CAN总线设备状态
2. 处理用户交互
3. 展示心跳和里程计数据
"""
from PyQt6.QtWidgets import (QMainWindow, QLabel, QMessageBox, 
                            QVBoxLayout, QHBoxLayout, QGroupBox, QWidget)
from PyQt6.QtCore import Qt, pyqtSlot
from PyQt6.QtGui import QFont
from MotorAsst.ui.ui_main import Ui_MainWindow
from MotorAsst.src.rthread import BaseCanThread

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, can_interface="can1"):
        super().__init__()
        self.setupUi(self)
        self.can_interface = can_interface
        
        # 手动创建UI控件
        self._create_missing_widgets()
        
        # 初始化UI状态
        self._init_ui()
        
        # 创建CAN监控线程
        self.can_thread = BaseCanThread(can_interface=self.can_interface)
        self.can_thread.message_received.connect(self._handle_can_message)
        self.can_thread.register_handler("heartbeat", self.handle_heartbeat)
        self.can_thread.register_handler("odometry", self.handle_odometry)
        
        # 连接信号槽
        self.pushButton.clicked.connect(self.on_button_click)

    def _create_missing_widgets(self):
        """手动创建缺失的UI控件"""
        # 创建容器
        self.odom_group = QGroupBox("里程计数据", self)
        self.vel_group = QGroupBox("速度数据", self)
        self.status_group = QGroupBox("状态信息", self)
        
        # 创建标签
        self.left_odom_label = QLabel("0.000 m", self)
        self.right_odom_label = QLabel("0.000 m", self)
        self.left_vel_label = QLabel("0.000 m/s", self)
        self.right_vel_label = QLabel("0.000 m/s", self)
        self.uptime_label = QLabel("0.0 s", self)
        self.timestamp_label = QLabel("0 ms", self)
        
        # 设置字体
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        for label in [self.left_odom_label, self.right_odom_label, 
                     self.left_vel_label, self.right_vel_label]:
            label.setFont(font)
        
        # 布局里程计组
        odom_layout = QHBoxLayout()
        odom_layout.addWidget(QLabel("左轮里程:"))
        odom_layout.addWidget(self.left_odom_label)
        odom_layout.addSpacing(20)
        odom_layout.addWidget(QLabel("右轮里程:"))
        odom_layout.addWidget(self.right_odom_label)
        self.odom_group.setLayout(odom_layout)
        
        # 布局速度组
        vel_layout = QHBoxLayout()
        vel_layout.addWidget(QLabel("左轮速度:"))
        vel_layout.addWidget(self.left_vel_label)
        vel_layout.addSpacing(20)
        vel_layout.addWidget(QLabel("右轮速度:"))
        vel_layout.addWidget(self.right_vel_label)
        self.vel_group.setLayout(vel_layout)
        
        # 布局状态组
        status_layout = QVBoxLayout()
        status_layout.addWidget(QLabel("运行时间:"))
        status_layout.addWidget(self.uptime_label)
        status_layout.addWidget(QLabel("最后更新时间:"))
        status_layout.addWidget(self.timestamp_label)
        self.status_group.setLayout(status_layout)
        
        # 主布局
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.odom_group)
        main_layout.addWidget(self.vel_group)
        main_layout.addWidget(self.status_group)
        main_layout.addStretch()
        
        # 设置中心部件
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def _init_ui(self):
        """初始化UI元素"""
        # 状态栏标签
        self.status_label = QLabel("状态: 初始化CAN总线...", self)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.statusbar.addPermanentWidget(self.status_label)

        # 里程计数据显示初始化
        self.left_odom_label.setText("0.000 m")
        self.right_odom_label.setText("0.000 m")
        self.left_vel_label.setText("0.000 m/s")
        self.right_vel_label.setText("0.000 m/s")

    def showEvent(self, event):
        """窗口显示时启动CAN线程"""
        super().showEvent(event)
        self.can_thread.start()

    def closeEvent(self, event):
        """窗口关闭时安全停止线程"""
        self.can_thread.stop()
        super().closeEvent(event)

    @pyqtSlot(str, object)
    def _handle_can_message(self, msg_type, data):
        """分发CAN消息到对应处理器"""
        if msg_type == "heartbeat":
            self.handle_heartbeat(data)
        elif msg_type == "odometry":
            self.handle_odometry(data)

    def handle_heartbeat(self, data):
        """处理心跳数据并更新UI"""
        status_text = (
            f"节点 {data['node_id']} | "
            f"模式: {self._parse_mode(data['mode'])} | "
            f"健康: {self._parse_health(data['health'])}"
        )
        self.status_label.setText(status_text)
        
        # 更新运行时间显示
        uptime_sec = data['uptime'] / 1e6  # 转换为秒
        self.uptime_label.setText(f"{uptime_sec:.1f} s")

    def handle_odometry(self, data):
        """处理里程计数据并更新UI"""
        # 更新数值显示
        self.left_odom_label.setText(f"{data['left_odometry']:.3f} m")
        self.right_odom_label.setText(f"{data['right_odometry']:.3f} m")
        self.left_vel_label.setText(f"{data['left_velocity']:.3f} m/s")
        self.right_vel_label.setText(f"{data['right_velocity']:.3f} m/s")
        
        # 更新时间戳
        self.timestamp_label.setText(f"{data['timestamp']} ms")

    def on_button_click(self):
        """按钮点击事件处理"""
        QMessageBox.information(self, "控制指令", "控制指令已发送")

    def show_about(self):
        """显示关于对话框"""
        QMessageBox.about(self, "关于", 
            "CAN总线监控工具\n"
            "版本: 1.0\n"
            f"接口: {self.can_interface}")

    def _parse_mode(self, mode_str):
        """解析模式枚举值"""
        mode_map = {
            "value=0": "运行",
            "value=1": "初始化",
            "value=2": "维护",
            "value=3": "软件更新"
        }
        return mode_map.get(mode_str.split("(")[-1].rstrip(")"), mode_str)

    def _parse_health(self, health_str):
        """解析健康状态枚举值"""
        health_map = {
            "value=0": "正常",
            "value=1": "注意",
            "value=2": "警告",
            "value=3": "严重"
        }
        return health_map.get(health_str.split("(")[-1].rstrip(")"), health_str)