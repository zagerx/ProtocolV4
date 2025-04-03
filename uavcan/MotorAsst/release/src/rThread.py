# src/rThread.py
import asyncio
from threading import Thread
from lib.sub_heart import HeartbeatSubscriber

class HeartbeatMonitorThread(Thread):
    def __init__(self, target_node_id=28):
        super().__init__()
        self.target_node_id = target_node_id
        self.subscriber = HeartbeatSubscriber()
        self.subscriber.on_heartbeat_received = self._handle_heartbeat
        self._stop_event = asyncio.Event()

    def _handle_heartbeat(self, node_id, msg):
        if node_id == self.target_node_id:
            print("节点正常")  # 后续可替换为信号发射

    def run(self):
        self.subscriber.start()

    def stop(self):
        self.subscriber.stop()
