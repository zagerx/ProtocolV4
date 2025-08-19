import sys
import pathlib
import asyncio
import pycyphal
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Version_1_0

# 添加生成的DSDL路径
sys.path.append(str(pathlib.Path(".dsdl_generated").resolve()))
from dinosaurs.exception import Event_1_0  # 导入事件消息类型

async def subscribe_event_process():
    # ================== 初始化节点 ==================
    media = SocketCANMedia("can1", mtu=8)
    transport = CANTransport(media, local_node_id=111)
    
    node = make_node(
        transport=transport,
        info=NodeInfo(
            name="event_subscriber",
            software_version=Version_1_0(major=1, minor=0),
            unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF04")
        )
    )
    node.start()
    
    # 事件处理函数
    async def handle_event(msg: Event_1_0, transfer: pycyphal.transport.TransferFrom):
        """打印接收到的所有事件数据"""
        print("\n[事件报告]")
        print(f"组件ID: {msg.component_id}")
        print(f"设备ID: {msg.device_id}")
        print(f"事件代码: 0x{msg.event_code:04X} ({msg.event_code})")
        print(f"用户数据: 0x{msg.user_data:04X} ({msg.user_data})")
        print(f"来源节点: {transfer.source_node_id}")
        print("-" * 40)
    
    # 创建事件订阅者 (端口ID=1017)
    subscriber = node.make_subscriber(Event_1_0, 1017)
    subscriber.receive_in_background(handle_event)
    
    print(f"开始监听事件消息 (端口ID=1017)...")
    print("按 Ctrl+C 停止监听")
    
    try:
        # 保持运行
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        pass
    finally:
        # 清理资源
        subscriber.close()
        node.close()
        transport.close()
        print("\n资源已清理，停止监听")

if __name__ == "__main__":
    try:
        asyncio.run(subscribe_event_process())
    except KeyboardInterrupt:
        print("\n程序被用户中断")