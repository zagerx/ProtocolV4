import asyncio
import sys
sys.path.append('/home/zhangge/worknote/ProtocolV4/uavcan/MotorAsst/lib')


from PyQt6.QtCore import QThread, pyqtSignal


from sub_heart import HeartbeatMonitor
# import asyncio
# from PyQt6.QtCore import QThread, pyqtSignal
# from lib.sub_heart import HeartbeatMonitor

class BaseCanThread(QThread):
    """CAN总线基础线程类"""
    message_received = pyqtSignal(str, object)  # (msg_type, data)

    def __init__(self, can_interface="can1", local_node_id=28):
        super().__init__()
        self.can_interface = can_interface
        self.local_node_id = local_node_id
        self._running = True
        self._monitor_task = None
        self._handlers = {}
        self.heartbeat_monitor = None  # 显式初始化

    def register_handler(self, msg_type, handler):
        """注册消息处理器"""
        self._handlers[msg_type] = handler
        self.message_received.connect(
            lambda mtype, data: self._dispatch_message(mtype, data))

    def _dispatch_message(self, msg_type, data):
        """分发消息到对应处理器"""
        if msg_type in self._handlers:
            self._handlers[msg_type](data)

    async def _monitor_heartbeat(self):
        """心跳包监控任务"""
        try:
            while self._running:
                result = await self.heartbeat_monitor.monitor_heartbeat(timeout=1.0)
                if result:
                    msg, transfer = result
                    self.message_received.emit(
                        "heartbeat",
                        {
                            "node_id": transfer.source_node_id,
                            "mode": str(msg.mode),
                            "health": str(msg.health),
                            "uptime": msg.uptime
                        }
                    )
        except asyncio.CancelledError:
            print("心跳监控任务已取消")

    async def _run_tasks(self):
        """运行所有监控任务"""
        self.heartbeat_monitor = HeartbeatMonitor(
            can_interface=self.can_interface,
            local_node_id=self.local_node_id
        )
        await self.heartbeat_monitor.initialize()
        self._monitor_task = asyncio.create_task(self._monitor_heartbeat())
        try:
            await self._monitor_task
        except asyncio.CancelledError:
            pass

    async def _cleanup(self):
        """安全的资源清理"""
        if self._monitor_task and not self._monitor_task.done():
            self._monitor_task.cancel()
            try:
                await self._monitor_task
            except asyncio.CancelledError:
                pass
        
        if self.heartbeat_monitor:
            await self.heartbeat_monitor.close()

    def run(self):
        async def _main():
            try:
                await self._run_tasks()
            except Exception as e:
                print(f"线程运行错误: {e}")
            finally:
                await self._cleanup()

        asyncio.run(_main())

    def stop(self):
        self._running = False
        if self.isRunning():
            self.wait()