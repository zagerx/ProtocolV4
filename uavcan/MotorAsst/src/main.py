#!/usr/bin/env python3
import asyncio
import logging
import qasync
import numpy as np
from PyQt6.QtWidgets import QApplication
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.si.unit.velocity import Scalar_1_0
from dinosaurs.actuator.wheel_motor import SetTargetValue_2_0
from MotorAsst.drivers.can.transport import CANNodeService
from MotorAsst.core.monitorthread import MonitorThread
from MotorAsst.core.commendthread import CommandThread
from MotorAsst.config.configlog import setup_logging
from MotorAsst.ui.windowmain import MainWindow
from MotorAsst.config import ConfigManager
from dinosaurs.peripheral import OperateRemoteDevice_1_0

import os

command_thread = None

# 连接控制模式信号 - 使用下划线命名
def _handle_operation_mode(mode):
    logging.info(f"Operation mode changed to: {mode}")
    if mode == "start":
        # 执行启动指令
        print("start motor")
        asyncio.create_task(
            command_thread.send_command("MotorEnable", {"enable_state": 1})
        )
        pass
    elif mode == "stop":
        # 执行停止指令
        print("stop motor")
        asyncio.create_task(
            command_thread.send_command("MotorEnable", {"enable_state": 0}))        
        pass
    elif mode == "brake_lock":
        asyncio.create_task(
            command_thread.send_command("OperateBrake", {
                "method": OperateRemoteDevice_1_0.Request.CLOSE,
                "name": "m-brake",
                "param": "mode=emergency"
            })
        )
    elif mode == "brake_unlock":
        asyncio.create_task(
            command_thread.send_command("OperateBrake", {
                "method": OperateRemoteDevice_1_0.Request.OPEN 
            })
        )

async def async_main():
    global command_thread
    """主业务逻辑协程"""
    # 初始化配置和日志
    config = ConfigManager()
    setup_logging(config.app.logging)

    # 初始化Qt
    app = QApplication([])
    window = MainWindow()

    window.operationModeChanged.connect(_handle_operation_mode)

    if not os.path.exists("./MotorAsst/output/odom.csv"):
        with open("./MotorAsst/output/odom.csv", "w", encoding="utf-8") as f:
            f.write("\n")

    # 初始化CAN总线
    transport = CANTransport(
        SocketCANMedia(config.driver.can.interface, mtu=config.driver.can.mtu),
        local_node_id=config.driver.can.node_id
    )
    node_service = CANNodeService(transport)
    if not await node_service.start():
        return
    # 初始化速度指令客户端
    try:
        # 启动监控线程
        monitor_thread = MonitorThread(
            node_service,
            config.driver.monitors,
        )
        monitor_thread.signals.raw_data_updated.connect(window.on_raw_data)  # 关键连接！
 
        # 启动命令线程
        command_thread = CommandThread(node_service, config.driver.commands)
        
        await monitor_thread.start()
        await command_thread.start()
        
        # 发送使能命令并启动速度循环
        # if await command_thread.send_command("MotorEnable", {"enable_state": 0}):
        #     await command_thread.start_velocity_loop(
        #         initial_velocity={"left": -0.03, "right": 0.03},
        #         interval_ms = 300,
        #         duration_per_direction=8.0,
        #         cycles= 100
        #     )
        window.show()
        # window.
        await asyncio.get_event_loop().create_future()
    except asyncio.CancelledError:
        logging.info("正常退出")
    finally:
        await monitor_thread.stop()
        await command_thread.stop()
        await node_service.stop()

def main():
    try:
        qasync.run(async_main())
    except KeyboardInterrupt:
        logging.info("用户终止")

if __name__ == "__main__":
    main()