import asyncio
import pycyphal
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Version_1_0
from dinosaurs import BoardInfo_1_0  # 导入板级信息服务

async def write_board_info():
    """写入板级信息"""
    # ================== 配置参数 ==================
    SERVER_NODE_ID = 25       # 目标节点ID
    LOCAL_NODE_ID = 100       # 客户端节点ID
    TIMEOUT = 2.0             # 请求超时时间
    
    # 数据类型映射（用于友好显示）
    DATA_TYPE_MAP = {
        0: "BOARD_ID",
        1: "MODEL_ID",
        2: "ROBOT_SN",
        3: "BOARD_SN",
        4: "BOARD_NAME",
        5: "PRODUCTIVE_DATE",
        6: "TX2_SN",
        7: "JCB_SN"
    }
    
    # 要写入的数据（类型: 值）
    WRITE_DATA = {
        BoardInfo_1_0.Request.BOARD_ID_TYPE: "WWBA0101303COB03",
        BoardInfo_1_0.Request.MODEL_ID_TYPE: "LMLBA0200",
        BoardInfo_1_0.Request.ROBOT_SN_TYPE: "ROBOT_SN_NULL_TEST",  # 空字符串
        BoardInfo_1_0.Request.BOARD_SN_TYPE: "COBA2243003002",
        BoardInfo_1_0.Request.BOARD_NAME_TYPE: "SUPER LIFT"  # 空字符串
    }

    # ================== 初始化节点 ==================
    transport = CANTransport(
        media=SocketCANMedia("can1", mtu=8),
        local_node_id=LOCAL_NODE_ID
    )
    
    node = make_node(
        transport=transport,
        info=NodeInfo(
            name="board_info_writer",
            software_version=Version_1_0(major=1, minor=0),
            unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF01")
        )
    )
    
    # 创建客户端
    client = node.make_client(BoardInfo_1_0, server_node_id=SERVER_NODE_ID, port_name=2)


    try:
        print(f"写入板级信息中 (节点ID={SERVER_NODE_ID})...")
        
        for data_type, value in WRITE_DATA.items():
            # 创建写入请求
            request = BoardInfo_1_0.Request(
                data_type=data_type,
                data=value.encode('utf-8')  # 将字符串编码为字节
            )
            
            try:
                # 发送请求并等待响应
                response = await asyncio.wait_for(client.call(request), timeout=TIMEOUT)
                
                if response is None:
                    print(f"[错误] 无响应数据 (类型={DATA_TYPE_MAP.get(data_type, f'未知({data_type})')})")
                    continue
                    
                # 解析响应
                result = response[0].result
                type_name = DATA_TYPE_MAP.get(data_type, f"未知({data_type})")
                
                # 打印结果
                if result == 0:
                    print(f"- 成功写入 {type_name}: {value}")
                else:
                    print(f"- [失败] 写入 {type_name} 错误 (结果码={result})")
                    
            except asyncio.TimeoutError:
                print(f"[超时] {TIMEOUT}秒内无响应 (类型={DATA_TYPE_MAP.get(data_type, f'未知({data_type})')})")
            
    except Exception as e:
        print(f"[异常] {str(e)}")
    finally:
        client.close()
        node.close()
        transport.close()
        print("资源已清理")

if __name__ == "__main__":
    asyncio.run(write_board_info())