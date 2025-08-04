#超龙顶升机构自动化测试脚本
#循环上升/下降
import asyncio
import pycyphal
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Version_1_0
from dinosaurs.peripheral import MovableAddons_1_0, OperateRemoteDevice_1_0

# ================== 配置参数 ==================
TEST_CYCLES = 50000  # 测试循环次数
MOVABLE_PORT = 1022  # MovableAddons 订阅端口
OPERATE_PORT = 121   # OperateRemoteDevice 服务端口
SERVER_NODE_ID = 25  # 服务端节点ID
CLIENT_NODE_ID = 100 # 客户端节点ID

# 状态映射
STATE_MAP = {
    0: "INIT",
    1: "NOT_READY",
    2: "UNLOCK",
    3: "LOCKING",
    4: "LOCK",
    5: "UNLOCKING",
    6: "INTERMEDIATE",
    255: "EXCEPTION"
}

class AutomationTest:
    def __init__(self):
        self.current_cycle = 0
        self.last_state = None
        self.media = None
        self.transport = None
        self.node = None
        self.sub = None
        self.client = None
        self.stop_event = asyncio.Event()
        
    async def start(self):
        """初始化节点和通信"""
        print("初始化测试环境...")
        self.media = SocketCANMedia("can1", mtu=8)
        self.transport = CANTransport(self.media, local_node_id=CLIENT_NODE_ID)
        
        self.node = make_node(
            transport=self.transport,
            info=NodeInfo(
                name="automation_test",
                software_version=Version_1_0(major=1, minor=0),
                unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF01")
            )
        )
        self.node.start()
        
        # 创建订阅者和客户端
        self.sub = self.node.make_subscriber(MovableAddons_1_0, MOVABLE_PORT)
        self.sub.receive_in_background(self._handle_movable_message)
        
        self.client = self.node.make_client(
            OperateRemoteDevice_1_0,
            server_node_id=SERVER_NODE_ID,
            port_name=OPERATE_PORT
        )
        
        print(f"开始自动化测试，循环次数={TEST_CYCLES}")
        await self.stop_event.wait()  # 等待测试完成
    
    async def _handle_movable_message(self, msg, transfer):
        """处理 MovableAddons 消息"""
        current_state = msg.state.current_state
        state_name = STATE_MAP.get(current_state, f"UNKNOWN({current_state})")
        
        # 仅处理状态变化
        if current_state != self.last_state:
            print(f"状态变化: {STATE_MAP.get(self.last_state, 'N/A')} -> {state_name}")
            self.last_state = current_state
            
            # 状态触发逻辑
            if current_state == 2:  # UNLOCK
                print("检测到 UNLOCK 状态，等待2秒发送上升指令...")
                await asyncio.sleep(2)
                await self._send_operate_command("1")  # 上升
                
            elif current_state == 4:  # LOCK
                print("检测到 LOCK 状态，等待2秒发送下降指令...")
                await asyncio.sleep(2)
                await self._send_operate_command("0")  # 下降
                
                # 完成一次循环
                self.current_cycle += 1
                print(f"完成循环 {self.current_cycle}/{TEST_CYCLES}")
                
                # 检查测试是否完成
                if self.current_cycle >= TEST_CYCLES:
                    print(f"已完成 {TEST_CYCLES} 次循环，停止测试")
                    self.stop_event.set()
    
    async def _send_operate_command(self, param: str):
        """发送操作指令"""
        request = OperateRemoteDevice_1_0.Request(
            method=OperateRemoteDevice_1_0.Request.OPEN,
            name="ieb_motor_lift",
            param=param
        )
        
        try:
            response = await asyncio.wait_for(self.client.call(request), timeout=2.0)
            if response is not None:
                result = bytes(response[0].value).decode('utf-8', errors='replace')
                print(f"指令发送成功: 参数={param}, 结果={response[0].result}, 返回值={result}")
            else:
                print(f"指令发送失败: 无响应 (参数={param})")
        except asyncio.TimeoutError:
            print(f"指令发送超时: 参数={param}")
        except Exception as e:
            print(f"指令发送异常: {str(e)} (参数={param})")
    
    def cleanup(self):
        """清理资源"""
        print("清理资源...")
        if self.sub:
            self.sub.close()
        if self.client:
            self.client.close()
        if self.node:
            self.node.close()
        if self.transport:
            self.transport.close()
        if self.media:
            self.media.close()
        print("资源已清理")

async def main():
    """主函数"""
    test = AutomationTest()
    try:
        await test.start()
    finally:
        test.cleanup()

if __name__ == "__main__":
    asyncio.run(main())