#!/usr/bin/env python3
"""
主窗口界面 - 完整手动创建控件版本
"""
from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QMessageBox, 
    QVBoxLayout, QHBoxLayout, QGroupBox, QWidget
)
from PyQt6.QtCore import Qt, pyqtSlot
from PyQt6.QtGui import QFont
from MotorAsst.ui.ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._create_missing_controls()
        self._setup_ui()

    def _create_missing_controls(self):
        """手动创建缺失的控件"""
        # 主容器
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 1. 里程计数据组
        self.odom_group = QGroupBox("里程计数据")
        odom_layout = QHBoxLayout()
        
        self.left_odom_label = QLabel("0.000 m")
        self.right_odom_label = QLabel("0.000 m")
        
        odom_layout.addWidget(QLabel("左轮里程:"))
        odom_layout.addWidget(self.left_odom_label)
        odom_layout.addSpacing(20)
        odom_layout.addWidget(QLabel("右轮里程:"))
        odom_layout.addWidget(self.right_odom_label)
        self.odom_group.setLayout(odom_layout)
        
        # 2. 速度数据组
        self.vel_group = QGroupBox("速度数据")
        vel_layout = QHBoxLayout()
        
        self.left_vel_label = QLabel("0.000 m/s")
        self.right_vel_label = QLabel("0.000 m/s")
        
        vel_layout.addWidget(QLabel("左轮速度:"))
        vel_layout.addWidget(self.left_vel_label)
        vel_layout.addSpacing(20)
        vel_layout.addWidget(QLabel("右轮速度:"))
        vel_layout.addWidget(self.right_vel_label)
        self.vel_group.setLayout(vel_layout)
        
        # 添加到主布局
        self.main_layout.addWidget(self.odom_group)
        self.main_layout.addWidget(self.vel_group)
        self.main_layout.addStretch()

    def _setup_ui(self):
        """初始化UI设置"""
        # 设置字体
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        for label in [self.left_odom_label, self.right_odom_label, 
                     self.left_vel_label, self.right_vel_label]:
            label.setFont(font)
        
        # 状态栏标签
        self.status_label = QLabel("状态: 等待连接...")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.statusbar.addPermanentWidget(self.status_label)

    @pyqtSlot(dict)
    def handle_heartbeat(self, data: dict):
        """处理心跳数据"""
        mode_map = {0: "运行", 1: "初始化", 2: "维护", 3: "升级"}
        health_map = {0: "正常", 1: "注意", 2: "警告", 3: "故障"}
        
        status_text = (
            f"节点 {data['node_id']} | "
            f"模式: {mode_map.get(data['mode'], '未知')} | "
            f"健康: {health_map.get(data['health'], '未知')}"
        )
        self.status_label.setText(status_text)

    @pyqtSlot(dict)
    def handle_odometry(self, data: dict):
        """处理里程计数据"""
        self.left_odom_label.setText(f"{data['left_odometry']:.3f} m")
        self.right_odom_label.setText(f"{data['right_odometry']:.3f} m")
        self.left_vel_label.setText(f"{data['left_velocity']:.3f} m/s")
        self.right_vel_label.setText(f"{data['right_velocity']:.3f} m/s")
        self.status_label.setText("数据更新正常")

    @pyqtSlot(str)
    def handle_error(self, message: str):
        """处理错误信息"""
        QMessageBox.critical(self, "错误", message)
        self.status_label.setText(f"错误: {message[:30]}...")

    def closeEvent(self, event):
        """窗口关闭事件"""
        if hasattr(self, 'can_thread'):
            self.can_thread.stop()
        event.accept()