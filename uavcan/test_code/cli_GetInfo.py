import asyncio
import numpy as np
import pycyphal
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Version_1_0
from uavcan.node import GetInfo_1_0  # 导入GetInfo服务

async def client_getinfo_process():
    # ================== 配置参数 ==================
    SERVER_NODE_ID = 25       # 目标节点ID
    LOCAL_NODE_ID = 100       # 客户端节点ID
    TIMEOUT = 2.0             # 请求超时时间

    # ================== 初始化节点 ==================
    transport = CANTransport(
        media=SocketCANMedia("can1", mtu=8),
        local_node_id=LOCAL_NODE_ID
    )
    node = make_node(
        transport=transport,
        info=NodeInfo(
            name="get_info_client",
            software_version=Version_1_0(major=1, minor=0),
            unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF01")
        )
    )
    
    # 创建GetInfo服务客户端（固定端口ID 430）
    client = node.make_client(BoardInfo_1_0, server_node_id=28, port_name=113)


    try:
        print(f"查询节点信息中 (节点ID={SERVER_NODE_ID})...")
        
        # 创建空请求
        request = GetInfo_1_0.Request()
        
        try:
            # 发送请求并等待响应
            response = await asyncio.wait_for(client.call(request), timeout=TIMEOUT)
            
            if response is None:
                print("[错误] 无响应数据")
                return
                
            info = response[0]
            
            # 解码字符串字段
            name = bytes(info.name).decode('utf-8', errors='replace').rstrip('\x00')
            coa = bytes(info.certificate_of_authenticity).decode('utf-8', errors='replace').rstrip('\x00')
            
            # 处理软件镜像CRC（可选字段）
            image_crc = "未提供"
            if len(info.software_image_crc) > 0:
                image_crc = hex(info.software_image_crc[0])
            
            # 打印节点信息
            print("\n[节点信息]")
            print(f"协议版本:    {info.protocol_version.major}.{info.protocol_version.minor}")
            print(f"硬件版本:    {info.hardware_version.major}.{info.hardware_version.minor}")
            print(f"软件版本:    {info.software_version.major}.{info.software_version.minor}")
            print(f"VCS版本号:   {info.software_vcs_revision_id} (0x{info.software_vcs_revision_id:x})")
            print(f"唯一ID:      {bytes(info.unique_id).hex()}")
            print(f"节点名称:    {name}")
            print(f"软件镜像CRC: {image_crc}")
            print(f"认证证书:    {coa[:50]}{'...' if len(coa) > 50 else ''}")
            
        except asyncio.TimeoutError:
            print(f"[超时] {TIMEOUT}秒内无响应")
            print("可能原因:")
            print("1. 目标节点未在线")
            print("2. CAN连接问题")
            print("3. 目标节点未实现GetInfo服务")
            
    except Exception as e:
        print(f"[异常] {str(e)}")
    finally:
        client.close()
        node.close()
        transport.close()
        print("资源已清理")

if __name__ == "__main__":
    asyncio.run(client_getinfo_process())