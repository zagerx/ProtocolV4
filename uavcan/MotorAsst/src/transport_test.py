#!/usr/bin/env python3
import asyncio
import logging
from MotorAsst.core.monitorthread import MonitorThread
from MotorAsst.config import ConfigManager
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from MotorAsst.drivers.can.transport import CANNodeService
from logging.handlers import RotatingFileHandler

def setup_logging(config):
    """根据配置初始化日志系统"""
    logger = logging.getLogger()
    logger.setLevel(config.logging.level)

    # 文件日志（自动轮转）
    file_handler = RotatingFileHandler(
        filename=config.logging.file,
        maxBytes=config.logging.max_size * 1024 * 1024,
        backupCount=config.logging.backup_count,
        encoding='utf-8'
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    ))
    logger.addHandler(file_handler)

    # 可选控制台输出
    if config.logging.enable_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            '[%(levelname)s] %(name)s: %(message)s'
        ))
        logger.addHandler(console_handler)

async def main():
    config = ConfigManager()
    setup_logging(config.app)
    
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