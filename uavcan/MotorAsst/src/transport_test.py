#!/usr/bin/env python3
import asyncio
import logging
from logging.handlers import RotatingFileHandler
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from MotorAsst.drivers.can.transport import CANNodeService
from MotorAsst.drivers.can.monitors.heartbeat import HeartbeatMonitor
from MotorAsst.drivers.can.monitors.odometry import OdometryMonitor



from MotorAsst.config import ConfigManager

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

async def run_monitor(monitor, name: str):
    """监控任务运行器"""
    try:
        while True:
            success, data = await monitor.monitor(1.0)
            if success:
                logging.getLogger(name).info(_format_data(name, data))
    except asyncio.CancelledError:
        pass

def _format_data(name: str, data: dict) -> str:
    """数据格式化"""
    if name == "Odometry":
        return (
            f"TS={data['timestamp']:.3f}ms | "
            f"Left: v={data['left_velocity']:.3f}m/s o={data['left_odometry']:.3f}m | "
            f"Right: v={data['right_velocity']:.3f}m/s o={data['right_odometry']:.3f}m"
        )
    return str(data)

async def main():
    config = ConfigManager()
    setup_logging(config.app)
    
    transport = CANTransport(
        SocketCANMedia(
            config.driver.can.interface,
            mtu=config.driver.can.mtu
        ),
        local_node_id=config.driver.can.node_id
    )
    
    node_service = CANNodeService(transport)
    if not await node_service.start():
        return

    try:
        tasks = []
        for monitor_cfg in config.driver.monitors:
            if not monitor_cfg.enabled:
                continue
                
            subscriber = node_service.create_subscriber(
                monitor_cfg.data_type,
                monitor_cfg.port
            )
            if not subscriber:
                continue

            monitor_map = {
                "Heartbeat_1_0": (HeartbeatMonitor, "Heartbeat"),
                "OdometryAndVelocityPublish_1_0": (OdometryMonitor, "Odometry")
            }
            
            if monitor_class := monitor_map.get(monitor_cfg.data_type.__name__):
                tasks.append(asyncio.create_task(
                    run_monitor(monitor_class[0](subscriber), monitor_class[1])
                ))

        await asyncio.gather(*tasks)
    except KeyboardInterrupt:
        logging.info("Application shutdown")
    finally:
        await node_service.stop()

if __name__ == "__main__":
    asyncio.run(main())