#!/usr/bin/env python3
import asyncio
import logging
from MotorAsst.core.monitorthread import MonitorThread
from MotorAsst.config import ConfigManager
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from MotorAsst.drivers.can.transport import CANNodeService
from MotorAsst.config.configlog import setup_logging  # 直接从configlog导入

async def main():
    config = ConfigManager()
    setup_logging(config.app.logging)
    
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
        monitor_thread = MonitorThread(node_service, config.driver.monitors)
        await monitor_thread.start()
        
        # 主线程保持运行（后续可替换为UI事件循环）
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        logging.info("Application shutdown")
    finally:
        await monitor_thread.stop()
        await node_service.stop()

if __name__ == "__main__":
    asyncio.run(main())