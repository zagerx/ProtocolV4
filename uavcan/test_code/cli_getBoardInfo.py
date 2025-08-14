import asyncio
import numpy as np
import pycyphal
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Version_1_0
from dinosaurs import BoardInfo_1_0  # 导入板级信息服务

async def get_board_info():
    """查询并打印板级信息"""
    # ================== 配置参数 ==================
    SERVER_NODE_ID = 42       # 目标节点ID
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
    
    # 要查询的数据类型列表
    QUERY_TYPES = [
        BoardInfo_1_0.Request.BOARD_ID_TYPE,
        BoardInfo_1_0.Request.MODEL_ID_TYPE,
        BoardInfo_1_0.Request.ROBOT_SN_TYPE,
        BoardInfo_1_0.Request.BOARD_SN_TYPE,
        BoardInfo_1_0.Request.BOARD_NAME_TYPE
    ]

    # ================== 初始化节点 ==================
    transport = CANTransport(
        media=SocketCANMedia("can1", mtu=8),
        local_node_id=LOCAL_NODE_ID
    )
    
    node = make_node(
        transport=transport,
        info=NodeInfo(
            name="board_info_client",
            software_version=Version_1_0(major=1, minor=0),
            unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF01")
        )
    )
    
    # 创建客户端
    client = node.make_client(BoardInfo_1_0, server_node_id=SERVER_NODE_ID, port_name=2)


    try:
        print(f"查询板级信息中 (节点ID={SERVER_NODE_ID})...")
        
        for data_type in QUERY_TYPES:
            # 创建读取请求（data为空表示读取操作）
            request = BoardInfo_1_0.Request(
                data_type=data_type,
                data=bytes()  # 空字节数组表示读取操作
            )
            
            try:
                # 发送请求并等待响应
                response = await asyncio.wait_for(client.call(request), timeout=TIMEOUT)
                
                if response is None:
                    print(f"[错误] 无响应数据 (类型={DATA_TYPE_MAP.get(data_type, f'未知({data_type})')})")
                    continue
                    
                # 解析响应
                result = response[0].result
                value = bytes(response[0].value).decode('utf-8', errors='replace').rstrip('\x00')
                
                # 打印结果
                type_name = DATA_TYPE_MAP.get(data_type, f"未知({data_type})")
                if result == 0:
                    print(f"- {type_name}: {value}")
                else:
                    print(f"- {type_name}: [错误] 操作失败 (结果码={result})")
                    
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
    asyncio.run(get_board_info())