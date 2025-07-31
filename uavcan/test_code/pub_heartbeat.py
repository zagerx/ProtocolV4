import asyncio
import pycyphal
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Heartbeat_1_0, Health_1_0, Mode_1_0
from uavcan.node import Version_1_0

async def publish_heartbeat():
    """以节点ID 16发布心跳消息"""
    # ================== 配置参数 ==================
    NODE_ID = 16              # 节点ID
    PUBLISH_INTERVAL = 1.0    # 发布间隔 (秒)
    
    # ================== 初始化节点 ==================
    print(f"初始化节点 (ID={NODE_ID})...")
    transport = CANTransport(
        media=SocketCANMedia("can1", mtu=8),
        local_node_id=NODE_ID
    )
    
    node = make_node(
        transport=transport,
        info=NodeInfo(
            name="updatee_info_client",
            software_version=Version_1_0(major=1, minor=0),
            unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF01")
        )
    )
    node.start()
    
    # 创建心跳发布者 (固定主题ID 7509)
    print("创建心跳发布者 (主题ID=7509)...")
    publisher = node.make_publisher(Heartbeat_1_0, 7509)
    
    try:
        print(f"开始发布心跳 (间隔={PUBLISH_INTERVAL}秒)...")
        uptime = 0
        
        while True:
            # 创建心跳消息
            heartbeat = Heartbeat_1_0(
                uptime=uptime,
                health=Health_1_0(value=Health_1_0.NOMINAL),  # 健康状态: NOMINAL
                mode=Mode_1_0(value=Mode_1_0.OPERATIONAL),    # 运行模式: OPERATIONAL
                vendor_specific_status_code=0                   # 供应商状态码
            )
            
            # 发布心跳
            await publisher.publish(heartbeat)
            print(f"已发送心跳: uptime={uptime}s, health=NOMINAL, mode=OPERATIONAL")
            
            # 等待并增加运行时间
            await asyncio.sleep(PUBLISH_INTERVAL)
            uptime += 1
            
    except KeyboardInterrupt:
        print("\n停止发布心跳")
    finally:
        print("清理资源...")
        publisher.close()
        node.close()
        transport.close()
        print("资源已清理")

if __name__ == "__main__":
    asyncio.run(publish_heartbeat())