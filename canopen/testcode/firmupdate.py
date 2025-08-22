#!/usr/bin/env python3
"""
CANopen 程序升级工具
功能：支持通过 CANopen 协议进行固件升级
作者：CANopen 专家
日期：2023-10-15
"""

import argparse
import can
import time
import sys
import os
from tqdm import tqdm

class CANopenProgramUpdater:
    def __init__(self, interface='can1', bitrate=1000000, node_id=10):
        self.interface = interface
        self.bitrate = bitrate
        self.node_id = node_id
        self.bus = None
        # SDO通信参数
        self.sdo_tx_cobid = 0x600 + self.node_id  # 发送到节点的SDO请求COB-ID
        self.sdo_rx_cobid = 0x580 + self.node_id  # 从节点接收的SDO响应COB-ID

    def connect(self):
        """连接到CAN总线"""
        try:
            self.bus = can.Bus(
                interface='socketcan',
                channel=self.interface,
                bitrate=self.bitrate
            )
            print(f"✅ 已连接到CAN接口 {self.interface}，波特率 {self.bitrate}")
            return True
        except can.CanError as e:
            print(f"❌ 连接CAN接口失败: {e}")
            return False

    def send_nmt_command(self, command_code):
        """发送NMT命令"""
        try:
            msg = can.Message(
                arbitration_id=0x000,  # NMT COB-ID
                data=[command_code, self.node_id],
                is_extended_id=False
            )
            self.bus.send(msg)
            print(f"📤 已发送NMT命令: 0x{command_code:02X} 到节点 {self.node_id}")
            return True
        except can.CanError as e:
            print(f"❌ 发送NMT命令失败: {e}")
            return False

    def send_sdo_request(self, data):
        """发送SDO请求"""
        try:
            msg = can.Message(
                arbitration_id=self.sdo_tx_cobid,
                data=data,
                is_extended_id=False
            )
            self.bus.send(msg)
            return True
        except can.CanError as e:
            print(f"❌ 发送SDO请求失败: {e}")
            return False

    def wait_for_sdo_response(self, timeout=1.0):
        """等待SDO响应"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                msg = self.bus.recv(timeout=0.1)
                if msg and msg.arbitration_id == self.sdo_rx_cobid:
                    return msg.data
            except can.CanError as e:
                print(f"❌ 接收SDO响应时发生错误: {e}")
                return None
        return None

    def sdo_write_expedited(self, index, subindex, data):
        """SDO快速写入（4字节以内数据）"""
        if len(data) > 4:
            raise ValueError("快速写入只支持4字节以内数据")
        
        # 构建命令字节
        n = 4 - len(data)  # 空字节数
        command_byte = 0x23 | (n << 2)  # 写入请求 + 数据长度指示
        
        # 构建数据帧
        frame = [
            command_byte,
            index & 0xFF,           # 索引低字节
            (index >> 8) & 0xFF,    # 索引高字节
            subindex
        ]
        
        # 添加数据（小端序）
        frame.extend(data)
        # 填充剩余字节
        frame.extend([0] * (8 - len(frame)))
        
        if not self.send_sdo_request(frame):
            return False
        
        response = self.wait_for_sdo_response()
        if response is None:
            print("❌ 等待SDO响应超时")
            return False
        
        if response[0] == 0x60:  # 写入成功响应
            return True
        elif (response[0] & 0xE0) == 0x80:  # 错误响应
            error_code = int.from_bytes(response[4:8], byteorder='little')
            print(f"❌ SDO写入失败，错误代码: 0x{error_code:08X}")
            return False
        else:
            print(f"❌ 未知的响应: {response.hex()}")
            return False
    def sdo_write_expedited_domain(self, index, subindex, data):
        """SDO快速写入DOMAIN类型数据（最大32字节）"""
        if len(data) > 32:
            raise ValueError("DOMAIN类型数据最大支持32字节")
        
        # 构建命令字节
        n = 4 - min(4, len(data))  # 空字节数 (对于DOMAIN类型，可能需要特殊处理)
        command_byte = 0x23 | (n << 2)  # 写入请求 + 数据长度指示
        
        # 构建数据帧
        frame = [
            command_byte,
            index & 0xFF,           # 索引低字节
            (index >> 8) & 0xFF,    # 索引高字节
            subindex
        ]
        
        # 添加数据（小端序）
        frame.extend(data)
        # 填充剩余字节
        frame.extend([0] * (8 - len(frame)))
        
        if not self.send_sdo_request(frame):
            return False
        
        response = self.wait_for_sdo_response()
        if response is None:
            print("❌ 等待SDO响应超时")
            return False
        
        if response[0] == 0x60:  # 写入成功响应
            return True
        elif (response[0] & 0xE0) == 0x80:  # 错误响应
            error_code = int.from_bytes(response[4:8], byteorder='little')
            print(f"❌ SDO写入失败，错误代码: 0x{error_code:08X}")
            return False
        else:
            print(f"❌ 未知的响应: {response.hex()}")
            return False


    def program_download(self, firmware_file):
        print(f"\n开始程序下载: {firmware_file}")
        
        # 读取固件文件
        try:
            with open(firmware_file, 'rb') as f:
                firmware_data = f.read()
        except Exception as e:
            print(f"❌ 读取固件文件失败: {e}")
            return False
        
        print(f"固件大小: {len(firmware_data)} 字节")
        
        # 定义参数
        chunk_size = 32  # 匹配节点programData大小
        timeout = 30  # 30秒超时
        max_retries = 3  # 最大重试次数
        
        # 1. 设置节点为预操作状态
        print("\n1. 设置节点为预操作状态")
        retry_count = 0
        while retry_count < max_retries:
            if self.send_nmt_command(0x80):  # 进入预操作状态
                break
            retry_count += 1
            time.sleep(0.1)
        else:
            return False
        time.sleep(0.1)
        
        # 2. 启动下载程序
        print("\n2. 启动下载程序")
        retry_count = 0
        while retry_count < max_retries:
            if self.sdo_write_expedited(0x1F51, 0x01, [0x01]):  # 写入0x01启动下载
                break
            retry_count += 1
            time.sleep(0.1)
        else:
            return False
        
        # 3. 写入程序数据到0x1F50
        print("\n3. 写入程序数据到0x1F50")
        total_size = len(firmware_data)
        offset = 0
        with tqdm(total=total_size, unit='B', unit_scale=True) as pbar:
            while offset < total_size:
                chunk = list(firmware_data[offset:offset+chunk_size])
                # 使用快速写入方式写入DOMAIN数据
                retry_count = 0
                while retry_count < max_retries:
                    try:
                        if self.sdo_write_expedited(0x1F50, 0x01, chunk):
                            break
                    except ValueError as e:
                        # 如果数据超过4字节，则进行分块处理
                        if "快速写入只支持4字节以内数据" in str(e):
                            # 分割成4字节一块进行传输
                            segment_success = True
                            for i in range(0, len(chunk), 4):
                                segment = chunk[i:i+4]
                                if not self.sdo_write_expedited(0x1F50, 0x01, segment):
                                    segment_success = False
                                    break
                            if segment_success:
                                break
                        else:
                            print(f"❌ 数据写入失败: {e}")
                            return False
                    retry_count += 1
                    time.sleep(0.1)
                else:
                    return False
                    
                offset += len(chunk)
                pbar.update(len(chunk))
                # 添加小延迟以避免总线过载
                time.sleep(0.001)
        
        # 4. 完成下载
        print("\n4. 完成下载")
        retry_count = 0
        while retry_count < max_retries:
            if self.sdo_write_expedited(0x1F51, 0x01, [0x02]):  # 写入0x02完成下载
                break
            retry_count += 1
            time.sleep(0.1)
        else:
            return False
        
        # 5. 等待下载完成并检查状态
        print("\n5. 等待下载完成...")
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            # 读取下载状态 (0x1F57)
            status = self.read_status()
            if status is not None:
                if status == 0x00000001:  # 下载成功
                    print("✅ 程序下载成功")
                    return True
                elif status != 0x00000000:  # 下载失败
                    print(f"❌ 程序下载失败，状态码: 0x{status:08X}")
                    return False
            
            time.sleep(0.5)
        
        print("❌ 等待下载状态超时")
        return False


    def read_status(self):
        """读取下载状态 (0x1F57)"""
        # 发送读取请求
        read_request = [
            0x40,  # 读取请求
            0x57, 0x1F,  # 索引0x1F57 (小端序)
            0x01,  # 子索引1
            0, 0, 0, 0
        ]
        
        if not self.send_sdo_request(read_request):
            return None
        
        response = self.wait_for_sdo_response()
        if response is None:
            return None
        
        if response[0] == 0x43:  # 读取成功响应
            return int.from_bytes(response[4:8], byteorder='little')
        else:
            return None

    def activate_firmware(self):
        """激活新固件（发送应用复位命令）"""
        print("\n5. 激活新固件")
        return self.send_nmt_command(0x01)  # 应用复位命令

    def close(self):
        """关闭CAN连接"""
        if self.bus:
            self.bus.shutdown()
            print("CAN总线连接已关闭")

def main():
    parser = argparse.ArgumentParser(
        description="CANopen程序升级工具",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-i', '--interface', default='can1',
                        help='CAN接口名称')
    parser.add_argument('-b', '--bitrate', type=int, default=1000000,
                        help='CAN总线波特率')
    parser.add_argument('-n', '--node', type=int, default=10,
                        help='目标节点ID')
    parser.add_argument('-f', '--firmware', required=True,
                        help='固件文件路径')
    
    args = parser.parse_args()
    
    # 验证参数
    if args.node < 1 or args.node > 127:
        print("❌ 错误: 节点ID必须在 1-127 范围内")
        sys.exit(1)
    
    if not os.path.isfile(args.firmware):
        print(f"❌ 错误: 固件文件 '{args.firmware}' 不存在")
        sys.exit(1)
    
    # 创建升级器
    updater = CANopenProgramUpdater(
        interface=args.interface,
        bitrate=args.bitrate,
        node_id=args.node
    )
    
    # 连接到CAN总线
    if not updater.connect():
        sys.exit(1)
    
    try:
        # 执行程序下载
        if updater.program_download(args.firmware):
            # 激活新固件
            if updater.activate_firmware():
                print("✅ 程序升级完成，新固件已激活")
                sys.exit(0)
            else:
                print("❌ 激活新固件失败")
                sys.exit(1)
        else:
            print("❌ 程序下载失败")
            sys.exit(1)
    finally:
        updater.close()

if __name__ == "__main__":
    main()