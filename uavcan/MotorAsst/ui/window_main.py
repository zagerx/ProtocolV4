#!/usr/bin/env python3
"""
主窗口界面 - 优化解耦版本
"""
import time
from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QMessageBox, QVBoxLayout,
    QHBoxLayout, QGroupBox, QWidget, QStatusBar
)
from PyQt6.QtCore import Qt, pyqtSlot, QTimer  # 修正：从QtCore导入QTimer
from PyQt6.QtGui import QFont
from typing import Optional
from config import UIConfig

class MainWindow(QMainWindow):
    def __init__(self, ui_config: UIConfig):
        super().__init__()
        self._ui_config = ui_config
        self._precision = ui_config.decimal_precision
        self._last_heartbeat_time = 0  # 记录最后心跳时间
        self._heartbeat_timeout = 2000  # 心跳超时阈值(ms)
        self._init_ui()
        self._setup_connections()
        self._start_status_timer()  # 启动状态检查定时器

    def _init_ui(self):
        """初始化所有UI组件"""
        self.setWindowTitle("UAVCAN 电机助手")
        self.resize(800, 600)

        # 主容器
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # 1. 状态显示组
        self.status_group = QGroupBox("节点状态")
        status_layout = QHBoxLayout()
        self.node_status_label = QLabel("未连接")
        self.node_mode_label = QLabel("模式: -")
        self.node_health_label = QLabel("健康: -")
        
        for widget in [self.node_status_label, self.node_mode_label, self.node_health_label]:
            widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
            widget.setStyleSheet("font-weight: bold;")
        
        status_layout.addWidget(self.node_status_label)
        status_layout.addWidget(self.node_mode_label)
        status_layout.addWidget(self.node_health_label)
        self.status_group.setLayout(status_layout)

        # 2. 里程计数据组
        self.odom_group = QGroupBox("里程计数据")
        odom_layout = QHBoxLayout()
        
        self.left_odom_label = self._create_data_label("-.---")
        self.right_odom_label = self._create_data_label("-.---")
        
        odom_layout.addWidget(QLabel("左轮里程:"))
        odom_layout.addWidget(self.left_odom_label)
        odom_layout.addSpacing(20)
        odom_layout.addWidget(QLabel("右轮里程:"))
        odom_layout.addWidget(self.right_odom_label)
        self.odom_group.setLayout(odom_layout)

        # 3. 速度数据组
        self.vel_group = QGroupBox("速度数据")
        vel_layout = QHBoxLayout()
        
        self.left_vel_label = self._create_data_label("-.---")
        self.right_vel_label = self._create_data_label("-.---")
        
        vel_layout.addWidget(QLabel("左轮速度:"))
        vel_layout.addWidget(self.left_vel_label)
        vel_layout.addSpacing(20)
        vel_layout.addWidget(QLabel("右轮速度:"))
        vel_layout.addWidget(self.right_vel_label)
        self.vel_group.setLayout(vel_layout)

        # 添加到主布局
        self.main_layout.addWidget(self.status_group)
        self.main_layout.addWidget(self.odom_group)
        self.main_layout.addWidget(self.vel_group)
        self.main_layout.addStretch()

        # 状态栏
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_label = QLabel("就绪")
        self.status_bar.addPermanentWidget(self.status_label)

    def _create_data_label(self, text: str) -> QLabel:
        """创建统一风格的数据标签"""
        label = QLabel(text)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignRight)
        label.setMinimumWidth(100)
        return label

    def _setup_connections(self):
        """初始化信号连接"""
        pass

    def _start_status_timer(self):
        """启动状态检查定时器"""
        self._status_timer = QTimer(self)
        self._status_timer.timeout.connect(self._check_connection_status)
        self._status_timer.start(1000)  # 每秒检查一次

    def _check_connection_status(self):
        """检查连接状态"""
        current_time = time.time() * 1000  # 当前时间戳(ms)
        if current_time - self._last_heartbeat_time > self._heartbeat_timeout:
            self._show_disconnected_status()

    def _show_disconnected_status(self):
        """显示断开连接状态"""
        self.node_status_label.setText("节点断开")
        self.node_mode_label.setText("模式: 离线")
        self.node_health_label.setText("健康: 故障")
        self.node_health_label.setStyleSheet("color: red;")
        
        # 清空里程计和速度显示
        self.left_odom_label.setText("-.---")
        self.right_odom_label.setText("-.---")
        self.left_vel_label.setText("-.---")
        self.right_vel_label.setText("-.---")
        self.status_label.setText("通信超时")

    @pyqtSlot(dict)
    def handle_heartbeat(self, data: dict):
        """处理心跳数据"""
        self._last_heartbeat_time = time.time() * 1000  # 更新最后心跳时间
        
        mode_map = {
            0: "运行", 1: "初始化",
            2: "维护", 3: "升级"
        }
        health_map = {
            0: ("正常", "green"),
            1: ("注意", "orange"),
            2: ("警告", "yellow"),
            3: ("故障", "red")
        }

        health_text, health_color = health_map.get(data['health'], ("未知", "gray"))
        
        self.node_status_label.setText(f"节点ID: {data['node_id']}")
        self.node_mode_label.setText(f"模式: {mode_map.get(data['mode'], '未知')}")
        self.node_health_label.setText(f"健康: {health_text}")
        self.node_health_label.setStyleSheet(f"color: {health_color};")

    @pyqtSlot(dict)
    def handle_odometry(self, data: dict):
        """处理里程计数据"""
        fmt = f"{{:.{self._precision}f}}"
        self.left_odom_label.setText(fmt.format(data['left_odometry']))
        self.right_odom_label.setText(fmt.format(data['right_odometry']))
        self.left_vel_label.setText(fmt.format(data['left_velocity']))
        self.right_vel_label.setText(fmt.format(data['right_velocity']))
        self.status_label.setText(f"最后更新: {data['timestamp']}ms")

    @pyqtSlot(str)
    def handle_error(self, message: str):
        """处理错误信息"""
        QMessageBox.critical(self, "通信错误", message)
        self.status_label.setText(f"错误: {message[:50]}...")
        self._show_disconnected_status()

    def closeEvent(self, event):
        """窗口关闭事件处理"""
        if hasattr(self, '_controller'):
            self._controller.stop()
        event.accept()

    def set_controller(self, controller):
        """注入控制器引用"""
        self._controller = controller