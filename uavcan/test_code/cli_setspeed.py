import asyncio
import math
import signal
import pycyphal
import numpy as np
from pycyphal.application import make_node, NodeInfo
from pycyphal.transport.can import CANTransport
from pycyphal.transport.can.media.socketcan import SocketCANMedia
from uavcan.node import Version_1_0
from uavcan.si.unit.velocity import Scalar_1_0
from dinosaurs.actuator.wheel_motor import SetTargetValue_2_0

# 全局变量用于控制循环
running = True

def signal_handler(sig, frame):
    """处理Ctrl+C信号"""
    global running
    print("\nStopping velocity commands...")
    running = False

async def send_velocity_commands(client, velocities):
    """发送速度指令到指定客户端"""
    request = SetTargetValue_2_0.Request(velocity=velocities)
    try:
        response = await asyncio.wait_for(client.call(request), timeout=0.1)
        return response
    except asyncio.TimeoutError:
        print("[Timeout] No response within 100ms")
        return None

def generate_velocity_pattern(step, pattern="random", amplitude=20.0, frequency=0.1):
    """
    生成速度模式
    :param step: 当前时间步长
    :param pattern: 模式类型 ('sine', 'triangle', 'sawtooth', 'random')
    :param amplitude: 速度幅度 (m/s)
    :param frequency: 模式频率 (Hz)
    :return: 速度值
    """
    t = step * 0.1  # 每个步长100ms
    
    if pattern == "sine":
        # 正弦波模式
        return amplitude * math.sin(2 * math.pi * frequency * t)
    
    elif pattern == "triangle":
        # 三角波模式
        period = 1.0 / frequency
        phase = t % period
        half_period = period / 2
        if phase < half_period:
            return amplitude * (2 * phase / half_period - 1)
        else:
            return amplitude * (1 - 2 * (phase - half_period) / half_period)
    
    elif pattern == "sawtooth":
        # 锯齿波模式
        period = 1.0 / frequency
        return amplitude * (2 * (t % period) / period - 1)
    
    elif pattern == "random":
        # 随机模式
        return amplitude * (2 * np.random.random() - 1)
    
    else:
        # 默认返回0
        return 0.0

async def velocity_command_loop():
    """主循环：持续发送速度指令"""
    global running
    
    # 设置信号处理
    signal.signal(signal.SIGINT, signal_handler)
    
    transport = CANTransport(
        media=SocketCANMedia("can1", mtu=8),
        local_node_id=100
    )
    node = make_node(
        transport=transport,
        info=NodeInfo(
            name="velocity_controller",
            software_version=Version_1_0(major=1, minor=0),
            unique_id=bytes.fromhex("DEADBEEFCAFEBABE12345678ABCDEF01")
        )
    )
    client = node.make_client(SetTargetValue_2_0, server_node_id=28, port_name=117)
    
    print("Starting velocity command loop. Press Ctrl+C to stop...")
    print("Velocity pattern: sine wave (-20 to 20 m/s)")
    
    step = 0
    try:
        while running:
            # 生成当前速度值
            velocity_value = generate_velocity_pattern(step)
            
            # 创建速度数组（这里保持两个电机相同的速度）
            velocities = np.array([
                Scalar_1_0(velocity_value),
                Scalar_1_0(velocity_value)
            ], dtype=object)
            
            # 发送速度指令
            response = await send_velocity_commands(client, velocities)
            
            if response is not None:
                print(f"[Step {step}] Velocity: {velocity_value:.2f} m/s | Response: {response}")
            else:
                print(f"[Step {step}] Velocity: {velocity_value:.2f} m/s | No response")
            
            step += 1
            await asyncio.sleep(2)  # 100ms周期
    
    finally:
        # 发送停止指令
        stop_velocities = np.array([
            Scalar_1_0(0.0),
            Scalar_1_0(0.0)
        ], dtype=object)
        await send_velocity_commands(client, stop_velocities)
        
        # 清理资源
        client.close()
        node.close()
        transport.close()
        print("Resources cleaned up. Exiting.")

if __name__ == "__main__":
    asyncio.run(velocity_command_loop())