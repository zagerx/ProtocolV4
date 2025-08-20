import sys
import pathlib
import asyncio
import pycyphal
import numpy as np
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Version_1_0

# 添加生成的DSDL路径
sys.path.append(str(pathlib.Path(".dsdl_generated").resolve()))
from dinosaurs import GlobalHealth_1_0  # 导入全局健康消息类型

# 设备类型映射
DEVICE_TYPE_MAP = {
    1: "ACCELEROMETER",
    2: "GYROSCOPE",
    3: "IMU",
    4: "IR",
    5: "LIDAR",
    6: "BAROMETER",
    7: "SONAR",
    8: "THERMOMETER",
    9: "ENCODER",
    21: "LINEAR_MOTOR",
    22: "ORDINARY_MOTOR",
    23: "WHEELMOTOR",
    31: "BEEPER",
    32: "LIGHT",
    41: "BATTERY",
    42: "CHARGER"
}

# 健康状态映射
HEALTH_STATUS_MAP = {
    0: "NOMINAL",
    1: "ADVISORY",
    2: "CAUTION",
    3: "WARNING"
}

async def subscribe_globalhealth_process():
    # ================== 初始化节点 ==================
    media = SocketCANMedia("can1", mtu=8)
    transport = CANTransport(media, local_node_id=112)
    
    node = make_node(
        transport=transport,
        info=NodeInfo(
            name="globalhealth_subscriber",
            software_version=Version_1_0(major=1, minor=0),
            unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF05")
        )
    )
    node.start()
    
    # 全局健康消息处理函数
    async def handle_globalhealth(msg: GlobalHealth_1_0, transfer: pycyphal.transport.TransferFrom):
        """处理并打印全局健康消息"""
        print("\n[全局健康报告]")
        
        # 解码错误来源字符串
        error_source = msg.error_source.value.tobytes().decode('utf-8', errors='replace').rstrip('\x00')
        print(f"错误来源: {error_source}")
        
        # 设备类型解析
        device_type_str = DEVICE_TYPE_MAP.get(msg.device_type, f"未知({msg.device_type})")
        print(f"设备类型: {device_type_str}")
        
        # 健康状态解析
        health_status = HEALTH_STATUS_MAP.get(msg.health.value, f"未知({msg.health.value})")
        print(f"健康状态: {health_status}")
        
        # 错误代码解析
        if len(msg.error_code) > 0:
            error_code_hex = ''.join(f"{b:02X}" for b in msg.error_code)
            print(f"错误代码: {error_code_hex}")
        else:
            print("错误代码: 无")
        
        # 错误消息解析
        error_message = msg.error_message.value.tobytes().decode('utf-8', errors='replace').rstrip('\x00')
        print(f"错误描述: {error_message}")
        
        print(f"来源节点: {transfer.source_node_id}")
        print("-" * 60)
    
    # 创建订阅者 (端口ID=2 - 请根据实际配置调整)
    subscriber = node.make_subscriber(GlobalHealth_1_0, 2)
    subscriber.receive_in_background(handle_globalhealth)
    
    print(f"开始监听全局健康消息 (端口ID=2)...")
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
        asyncio.run(subscribe_globalhealth_process())
    except KeyboardInterrupt:
        print("\n程序被用户中断")