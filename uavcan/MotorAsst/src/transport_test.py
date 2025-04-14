#!/usr/bin/env python3
import asyncio
import logging
import qasync
from PyQt6.QtWidgets import QApplication
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from MotorAsst.drivers.can.transport import CANNodeService
from MotorAsst.core.monitorthread import MonitorThread
from MotorAsst.core.commendthread import CommandThread
from MotorAsst.config.configlog import setup_logging
from MotorAsst.ui.window_main import MainWindow
from MotorAsst.config import ConfigManager

class UIController:
    def __init__(self, window: MainWindow):
        self.window = window

    def on_monitor_data(self, name: str, data: dict):
        if name == "Heartbeat":
            self.window.handle_heartbeat(data)
        elif name == "Odometry":
            self.window.handle_odometry(data)
    def enable_motor(self) -> bool:
        """使能电机"""
        print("motor enable")
        return True  # 返回操作结果

    def disable_motor(self) -> bool:
        """失能电机"""
        print("motor disable")
        return True
    def stop(self):
        """停止控制器资源"""
        print("Controller stopped")

async def async_main():
    """主业务逻辑协程"""
    # 初始化配置和日志
    config = ConfigManager()
    setup_logging(config.app.logging)

    # 初始化Qt
    app = QApplication([])
    window = MainWindow(config.ui)
    controller = UIController(window)
    window.set_controller(controller)

    # 初始化CAN总线
    transport = CANTransport(
        SocketCANMedia(config.driver.can.interface, mtu=config.driver.can.mtu),
        local_node_id=config.driver.can.node_id
    )
    node_service = CANNodeService(transport)
    if not await node_service.start():
        return

    try:
        # 启动监控线程
        monitor_thread = MonitorThread(
            node_service,
            config.driver.monitors,
            # ui_callback=controller.on_monitor_data
        )
        
        # 启动命令线程
        command_thread = CommandThread(node_service, config.driver.commands)
        
        await monitor_thread.start()
        await command_thread.start()
        
        # 发送单次使能命令
        await command_thread.send_command("MotorEnable", {"enable_state": 1})
        
        window.show()
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