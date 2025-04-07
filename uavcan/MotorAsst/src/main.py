# import sys
# sys.path.append('/home/zhangge/worknote/ProtocolV4/uavcan/MotorAsst/lib')
# import asyncio

# from sub_heart import HeartbeatMonitor

# async def check_heartbeat():
#     async with HeartbeatMonitor(can_interface="can1", local_node_id=28) as monitor:
#         result = await monitor.monitor_heartbeat(timeout=2.0)
#         if result:
#             print("检测到心跳包")
#         else:
#             print("未检测到心跳包")

# if __name__ == "__main__":
#     asyncio.run(check_heartbeat())

import sys
import os

# 路径设置
ui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ui")
sys.path.append(os.path.normpath(ui_dir))
# sys.path.append('/home/zhangge/worknote/ProtocolV4/uavcan/MotorAsst/src')


from PyQt6.QtWidgets import QApplication
from rthread import BaseCanThread
from window_main import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # 初始化CAN线程
    can_thread = BaseCanThread()
    can_thread.register_handler("heartbeat", window.handle_heartbeat)
    can_thread.start()

    window.show()
    ret = app.exec()
    
    # 清理
    can_thread.stop()
    sys.exit(ret)

if __name__ == "__main__":
    main()