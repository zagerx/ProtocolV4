from typing import Dict
from dinosaurs.actuator.wheel_motor import Enable_1_0

class MotorEnableClient:
    @staticmethod
    def build_request(params: Dict) -> Enable_1_0.Request:
        """构建Enable请求"""
        enable_state = params.get("enable_state", 1)
        return Enable_1_0.Request(enable_state=enable_state)