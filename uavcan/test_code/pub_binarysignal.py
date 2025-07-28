import asyncio
import pycyphal
import time
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Version_1_0
from uavcan.time import SynchronizedTimestamp_1_0
from uavcan.primitive import String_1_0
from dinosaurs.sensor.binarysignal import BinarySignal_2_0

async def send_single_binary_signal():
    """发送单条BinarySignal消息并退出"""
    # 初始化CAN传输层和节点
    media = SocketCANMedia("can1", mtu=8)
    transport = CANTransport(media, local_node_id=100)
    
    node = make_node(
        transport=transport,
        info=NodeInfo(
            name="binary_signal_publisher",
            software_version=Version_1_0(major=1, minor=0),
            unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF03")
        )
    )
    node.start()

    # 创建BinarySignal消息
    pub = node.make_publisher(BinarySignal_2_0, 1004)
    
    try:
        # 创建正确的时间戳（使用time.time()获取真实时间）
        current_time = time.time()
        timestamp = SynchronizedTimestamp_1_0(microsecond=int(current_time * 1e6))
        
        # 创建并发送消息
        message = BinarySignal_2_0(
            timestamp=timestamp,
            name=String_1_0(value="estop-reset".encode()),
            state=True,
            device_id=0
        )
       
        # 发送消息
        await pub.publish(message)
        
        # 打印发送信息
        print(f"已广播: estop-reset, 状态: 触发, 设备ID: 0")
        print(f"时间戳: {timestamp.microsecond}μs (对应UTC时间: {time.ctime(current_time)})")
        print("消息已发送，程序退出")
        
        # 建议运行candump验证消息
        print("\n建议运行以下命令验证CAN消息:")
        print("$ candump can1")
        
    finally:
        pub.close()
        node.close()
        transport.close()

if __name__ == "__main__":
    asyncio.run(send_single_binary_signal())