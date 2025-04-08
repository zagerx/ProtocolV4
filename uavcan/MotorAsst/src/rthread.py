import asyncio
from PyQt6.QtCore import QThread, pyqtSignal
from MotorAsst.lib.sub_heart import HeartbeatMonitor
from MotorAsst.lib.sub_odom import OdomMonitor
class BaseCanThread(QThread):
    """CAN总线基础线程类"""
    message_received = pyqtSignal(str, object)  # (msg_type, data)

    def __init__(self, can_interface="can1", local_node_id=28):
        super().__init__()
        self.can_interface = can_interface
        self.local_node_id = local_node_id
        self._running = True
        self._monitor_tasks = {}
        self.heartbeat_monitor = None
        self.odom_monitor = None

    def register_handler(self, msg_type, handler):
        """注册消息处理器"""
        self.message_received.connect(
            lambda mtype, data: handler(data) if mtype == msg_type else None)

    async def _monitor_heartbeat(self):
        """心跳监控任务"""
        try:
            while self._running:
                success, result = await self.heartbeat_monitor.monitor_heartbeat(timeout=2.0)
                if not success:
                    print("heart timout")
                    continue

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
        except Exception as e:
            print(f"心跳监控错误: {type(e).__name__}: {e}")

    async def _monitor_odometry(self):
        """里程计监控任务"""
        try:
            while self._running:
                success, result = await self.odom_monitor.monitor_odom(timeout=2.0)
                if not success:
                    continue

                self.message_received.emit(
                    "odometry",
                    result
                )
        except asyncio.CancelledError:
            print("里程计监控任务已取消")
        except Exception as e:
            print(f"里程计监控错误: {type(e).__name__}: {e}")

    async def _run_tasks(self):
        """运行所有监控任务"""
        # 初始化两个监控器
        self.heartbeat_monitor = HeartbeatMonitor(
            can_interface=self.can_interface,
            local_node_id=self.local_node_id
        )
        await self.heartbeat_monitor.initialize()

        self.odom_monitor = OdomMonitor(
            can_interface=self.can_interface,
            local_node_id=self.local_node_id
        )
        await self.odom_monitor.initialize()

        # 创建并运行监控任务
        self._monitor_tasks["heartbeat"] = asyncio.create_task(self._monitor_heartbeat())
        self._monitor_tasks["odometry"] = asyncio.create_task(self._monitor_odometry())

        # 等待所有任务完成
        await asyncio.gather(*self._monitor_tasks.values())

    async def _cleanup(self):
        """安全的资源清理"""
        # 取消所有监控任务
        for task in self._monitor_tasks.values():
            if not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

        # 关闭监控器
        if self.heartbeat_monitor:
            await self.heartbeat_monitor.close()
        if self.odom_monitor:
            await self.odom_monitor.close()

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