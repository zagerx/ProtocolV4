#!/usr/bin/env python3
import asyncio
import logging
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from MotorAsst.drivers.can.transport import CANNodeService
from MotorAsst.drivers.can.monitors.heartbeat import HeartbeatMonitor
from MotorAsst.drivers.can.monitors.odometry import OdometryMonitor
from uavcan.node import Heartbeat_1_0
from dinosaurs.actuator.wheel_motor import OdometryAndVelocityPublish_1_0

async def monitor_heartbeat(monitor: HeartbeatMonitor):
    while True:
        success, data = await monitor.monitor(1.0)
        if success:
            logging.info(f"Heartbeat: {data}")

async def monitor_odometry(monitor: OdometryMonitor):
    while True:
        success, data = await monitor.monitor(1.0)
        if success:
            logging.info(
                f"Odometry: TS={data['timestamp']}ms\n"
                f"Left: vel={data['left_velocity']:.3f}m/s odom={data['left_odometry']:.3f}m\n"
                f"Right: vel={data['right_velocity']:.3f}m/s odom={data['right_odometry']:.3f}m"
            )

async def main():
    # 1. 初始化传输层
    transport = CANTransport((SocketCANMedia(("can1"), mtu=8)), local_node_id=100)
    
    # 2. 启动节点服务
    node_service = CANNodeService(transport)
    if not await node_service.start():
        return

    try:
        # 3. 创建并启动监控任务
        tasks = []
        
        # 心跳监控
        hb_sub = node_service.create_subscriber(Heartbeat_1_0, 7509)
        if hb_sub:
            tasks.append(asyncio.create_task(
                monitor_heartbeat(HeartbeatMonitor(hb_sub))
            ))
        
        # 里程计监控
        odom_sub = node_service.create_subscriber(OdometryAndVelocityPublish_1_0, 1100)
        if odom_sub:
            tasks.append(asyncio.create_task(
                monitor_odometry(OdometryMonitor(odom_sub))
            ))
        
        await asyncio.gather(*tasks)
        
    except asyncio.CancelledError:
        logging.info("Monitoring cancelled")
    except KeyboardInterrupt:
        logging.info("Keyboard interrupt received")
    finally:
        # 4. 资源释放
        await node_service.stop()

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass