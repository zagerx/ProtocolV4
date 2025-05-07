from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6.QtCore import QTimer, pyqtSlot,pyqtSignal
from MotorAsst.ui.uimain import Ui_MainWindow
from collections import deque
import time
'''
里程计数据原型
(dinosaurs.actuator.wheel_motor.OdometryAndVelocityPublish.1.0(timestamp=uavcan.time.SynchronizedTimestamp.1.0(microsecond=16), current_velocity=[uavcan.si.unit.velocity.Scalar.1.0(meter_per_second=0.3610669672489166),uavcan.si.unit.velocity.Scalar.1.0(meter_per_second=0.9325398802757263)], odometry=[uavcan.si.unit.length.Scalar.1.0(meter=0.9325398802757263),uavcan.si.unit.length.Scalar.1.0(meter=0.3610669672489166)]), TransferFrom(2025-04-15T17:14:37.486956/116008.786266, priority=NOMINAL, transfer_id=15, fragmented_payload=[7B+7B+7B+4B], source_node_id=28))
'''
class MainWindow(QMainWindow):
    """
    主窗口类，封装UI界面和基本功能
    """
    operationModeChanged = pyqtSignal(str)  # 添加这行
    targetValueRequested = pyqtSignal(dict)  # 新增目标值信号
    targetClearRequested = pyqtSignal()  # 新增清除信号

    def __init__(self):
        super().__init__()
        # 初始化UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 数据缓冲池（按优先级分离）
        self._high_freq_buffer = deque(maxlen=200)  # 100Hz数据保留2秒
        self._mid_freq_buffer = deque(maxlen=100)   # 50Hz数据保留2秒        
        self._last_update_time = {}  # 初始化时间记录字典

        # 初始化UI定时器
        self._init_timers()
        # 设置窗口标题
        self.setWindowTitle("电机监控系统")
        # 状态组
        self._init_status_group()
        # 连接按钮信号
        self._setup_button_connections()        
        # 设置互斥组
        self.ui.radioButton_4.setAutoExclusive(True)
        self.ui.radioButton_5.setAutoExclusive(True)
        # 连接信号 - 使用下划线命名
        self.ui.radioButton_4.toggled.connect(
            lambda checked: self._on_operation_mode_changed(checked, "start"))
        self.ui.radioButton_5.toggled.connect(
            lambda checked: self._on_operation_mode_changed(checked, "stop"))
        # 连接刹车控制信号
        self.ui.radioButton_6.toggled.connect(
            lambda checked: self._on_operation_mode_changed(checked, "brake_lock"))
        self.ui.radioButton_7.toggled.connect(
            lambda checked: self._on_operation_mode_changed(checked, "brake_unlock"))                
    def _init_status_group(self):
        """初始化状态显示组件"""
        self.ui.lineEdit_5_1.setReadOnly(True)
        self.ui.radioButton_5.setChecked(True)

    def _init_timers(self):
        """初始化多级刷新定时器"""
        # 高频数据UI更新（10ms间隔，实际渲染频率受限于Qt性能）
        self._high_freq_timer = QTimer()
        self._high_freq_timer.timeout.connect(self._update_high_freq_ui)
        self._high_freq_timer.start(10)  # ≈100Hz刷新
        
        # 中频数据UI更新（20ms间隔）
        self._mid_freq_timer = QTimer()
        # self._mid_freq_timer.timeout.connect(self._update_mid_freq_ui)
        self._mid_freq_timer.start(20)  # ≈50Hz刷新
        
        # 低频数据使用信号槽直连
        self._low_freq_timer = QTimer()
        self._low_freq_timer.timeout.connect(self._check_heartbeat)
        self._low_freq_timer.start(1000)  # 每秒检查一次

    @pyqtSlot(str, object, int)
    def on_raw_data(self, name, raw_data, priority):
        """信号槽：数据分类处理"""
        now = time.time()
        self._last_update_time[name] = now
        
        if priority == 2:
            # 低频数据
            self._update_low_freq_ui(name,raw_data)
        # if priority == 1:
            # 中频数据
            # self._mid_freq_buffer.append(event)
            # self._last_update_time[name] = now
        else:
            #高频数据
            self._high_freq_buffer.append({
                "name": name,
                "data": raw_data,
                "timestamp": now
            })

    def _update_high_freq_ui(self):
        """处理高频数据（odometry/velocity）"""
        if not self._high_freq_buffer:
            return

        latest_data = {}
        for item in reversed(self._high_freq_buffer):
            name_lower = item["name"].lower()
            if name_lower not in latest_data:
                latest_data[name_lower] = item["data"]

        # 分类处理各数据类型
        for data_type, raw_data in latest_data.items():
            if data_type == "odometry":
                self._handle_odometry(raw_data)


    # def _update_mid_freq_ui(self):
    #     """处理中频数据（temperature/voltage/current）"""
    #     if not self._mid_freq_buffer:
    #         return

    #     # 聚合显示（示例：温度显示最近值+最大值）
    #     temp_values = [
    #         e.data["value"] for e in self._mid_freq_buffer 
    #         if e.name == "temperature"
    #     ]
    #     if temp_values:
    #         self._widget_mapping["temperature"].setText(
    #             f"当前: {temp_values[-1]:.1f}°C\n峰值: {max(temp_values):.1f}°C"
    #         )

    ''' 
    心跳数据数据原型:
    (uavcan.node.Heartbeat.1.0(uptime=72, health=uavcan.node.Health.1.0(value=0), mode=uavcan.node.Mode.1.0(value=0), vendor_specific_status_code=0), TransferFrom(2025-04-15T16:07:38.662016/111989.961179, priority=NOMINAL, transfer_id=7, fragmented_payload=[7B], source_node_id=28))
    '''
    def _update_low_freq_ui(self, name, raw_data):
        """低频数据处理（保持扩展性）"""
        try:
            if name.lower() == "heartbeat":
                msg, transfer = raw_data
                # 更新心跳数据
                self.ui.lineEdit_5_1.setText(str(transfer.source_node_id))
                self.ui.lineEdit_5_2.setText(str(msg.mode.value))
                self._last_update_time["heartbeat"] = time.time()

            # 可在此扩展其他低频数据类型处理
            # elif name.lower() == "other_type":
            #    self._handle_other_type(raw_data)

        except Exception as e:
            print(f"低频数据处理异常 ({name}): {e}")

    def _check_heartbeat(self):
        """心跳丢失检测"""
        if time.time() - self._last_update_time.get("heartbeat", 0) > 2.0:
            self.ui.lineEdit_5_1.setText("×××")
            self.ui.lineEdit_5_2.setText("断线")

    def _handle_odometry(self, raw_data):
        """处理里程计数据"""
        try:
            msg, _ = raw_data
            timestamp = time.time()  # 获取当前时间戳

            self.ui.lineEdit_6_1.setText(f"{msg.current_velocity[0].meter_per_second:.3f}")
            self.ui.lineEdit_6_2.setText(f"{msg.current_velocity[1].meter_per_second:.3f}")
            self.ui.lineEdit_7_1.setText(f"{msg.odometry[0].meter:.3f}")
            self.ui.lineEdit_7_2.setText(f"{msg.odometry[1].meter:.3f}")
            # 准备CSV数据行
            csv_line = (
                f"timestamp:{timestamp:.6f},"
                f"v_l:{msg.current_velocity[0].meter_per_second:.3f},"
                f"v_r:{msg.current_velocity[1].meter_per_second:.3f},"
                f"o_l:{msg.odometry[0].meter:.3f},"
                f"o_r:{msg.odometry[1].meter:.3f}\n"
            )
            
            # 写入文件（追加模式）
            with open("./MotorAsst/output/odom.csv", "a", encoding="utf-8") as f:
                f.write(csv_line)            
        except Exception as e:
            print(f"里程计处理异常: {e}")


    def _setup_button_connections(self):
        """集中管理按钮信号连接"""
        self.ui.pushButton.clicked.connect(self._on_target_set_clicked)
        # 后续按钮可在此添加:
        self.ui.pushButton_3.clicked.connect(self._on_target_clear_clicked)  # 新增连接
    def _on_target_clear_clicked(self):
        """处理目标值清除"""
        self.targetClearRequested.emit()

    def _on_target_set_clicked(self):
        """处理目标值设置"""
        try:
            values = {
                "left": self.ui.doubleSpinBox.value(),
                "right": self.ui.doubleSpinBox_2.value()
            }
            self.targetValueRequested.emit(values)
        except ValueError as e:
            print(f"目标值设置错误: {e}")

    def _on_operation_mode_changed(self, checked, mode):
        """操作模式变化处理"""
        if checked:
            self.operationModeChanged.emit(mode)
            # self.ui.lineEdit_5_3.setText(mode.capitalize())