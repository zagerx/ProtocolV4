import asyncio
import argparse
import pycyphal
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Version_1_0
from uavcan.primitive import String_1_0
from dinosaurs.peripheral.AddonsGetState_1_0 import AddonsGetState_1_0

class AddonsGetStateClient:
    def __init__(self, args):
        self.args = args
        transport = CANTransport(
            media=SocketCANMedia(args.can_interface, mtu=8),
            local_node_id=100
        )
        self.node = make_node(
            transport=transport,
            info=NodeInfo(
                name="addons_get_state_client",
                software_version=Version_1_0(major=1, minor=0),
                unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF01")
            )
        )
        
        # 创建客户端
        self.client = self.node.make_client(
            AddonsGetState_1_0,
            args.server_node_id,
            port_name=201,
        )
        self.node.start()

    async def get_state(self, addon_name, device_id=0):
        """获取附加设备状态"""
        request = AddonsGetState_1_0.Request(
            name=String_1_0(value=addon_name),
            device_id=device_id
        )
        
        try:
            response_tuple = await asyncio.wait_for(
                self.client.call(request), 
                timeout=2.0
            )
            
            # 检查响应是否为 None
            if response_tuple is None:
                return None
                
            # 检查响应元组是否包含有效数据
            if len(response_tuple) > 0 and response_tuple[0] is not None:
                return response_tuple[0]  # 返回响应对象
            else:
                print("收到空响应")
                return None
                
        except asyncio.TimeoutError:
            print(f"[超时] {2.0}秒内无响应")
            return None
        except Exception as e:
            print(f"[异常] {str(e)}")
            return None

    async def close(self):
        """清理资源"""
        self.client.close()
        self.node.close()
        await asyncio.sleep(1)  # 给关闭操作一点时间

def parse_args():
    parser = argparse.ArgumentParser(description="附加设备状态查询客户端")
    parser.add_argument("-c", "--can-interface", default="can1", help="CAN接口名称")
    parser.add_argument("-s", "--server-node-id", type=int, default=25, help="服务器节点ID")
    parser.add_argument("-n", "--addon-name", default="lift", help="附加设备名称")
    parser.add_argument("-d", "--device-id", type=int, default=0, help="设备ID")
    return parser.parse_args()

async def main():
    args = parse_args()
    client = AddonsGetStateClient(args)
    
    try:
        response = await client.get_state(args.addon_name, args.device_id)
        if response:
            print(f"[响应] 接收到状态:")
            print(f"当前状态: {response.state.current_state}")
            print(f"时间戳: {response.state.timestamp.microsecond}微秒")
        else:
            print("未收到有效响应")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())