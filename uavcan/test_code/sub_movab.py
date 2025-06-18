import sys
import pathlib
sys.path.append(str(pathlib.Path(".dsdl_generated").resolve()))
import asyncio
import pycyphal
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Version_1_0
from dinosaurs.peripheral import MovableAddons_1_0

# 状态名称映射
STATE_NAMES = {
    0: "INIT",
    1: "NOT_READY",
    2: "UNLOCK",
    3: "LOCKING",
    4: "LOCK",
    5: "UNLOCKING",
    6: "INTERMEDIATE",
    255: "EXCEPTION"
}

class MovableAddonsMonitor:
    def __init__(self):
        self.start_time = pycyphal.transport.Timestamp.now().system_ns
    
    def log(self, msg):
        """打印MovableAddons消息到控制台"""
        # 计算相对时间戳（毫秒）
        current_time = pycyphal.transport.Timestamp.now().system_ns
        ts_ms = (current_time - self.start_time) // 1_000_000
        
        # 提取数据
        device_id = msg.device_id
        device_name = msg.name.value.tobytes().decode('utf-8').rstrip('\x00')
        state_value = msg.state.current_state
        state_name = STATE_NAMES.get(state_value, f"UNKNOWN({state_value})")
        
        # 打印到控制台
        print(f"[{ts_ms}ms] Device {device_id} ({device_name}): {state_name}")

async def sub_movable_addons():
    """主订阅函数"""
    monitor = MovableAddonsMonitor()
    media = SocketCANMedia("can1", mtu=8)
    transport = CANTransport(media, local_node_id=28)
    
    node = make_node(
        transport=transport,
        info=NodeInfo(
            name="movable_addons_monitor",
            software_version=Version_1_0(major=1, minor=0),
            unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF01")
        )
    )
    node.start()

    async def handler(msg, transfer):
        monitor.log(msg)  # 处理消息

    # 订阅MovableAddons消息（假设端口号为1200）
    sub = node.make_subscriber(MovableAddons_1_0, 1022)
    sub.receive_in_background(handler)
    
    print("Starting MovableAddons monitor. Press Ctrl+C to exit...")
    try:
        while True:
            await asyncio.sleep(1)  # 保持运行
    except KeyboardInterrupt:
        print("\nStopping monitor...")
    finally:
        sub.close()
        node.close()
        transport.close()
        print("Resources released")

if __name__ == "__main__":
    asyncio.run(sub_movable_addons())