import asyncio
import logging
from typing import Dict, Optional
from MotorAsst.drivers.can.transport import CANNodeService
from MotorAsst.config.configdrivers import CommandConfig

class CommandThread:
    def __init__(self, node_service: CANNodeService, commands_config: Dict[str, CommandConfig]):
        """
        初始化命令线程
        :param node_service: CAN节点服务
        :param commands_config: 命令配置字典
        """
        self.node_service = node_service
        self.commands_config = commands_config
        self._logger = logging.getLogger(self.__class__.__name__)
        self._active = False

    async def start(self):
        """启动命令线程"""
        self._active = True

    async def send_command(self, command_name: str, params: dict) -> bool:
        """发送单次命令"""
        if not self._active:
            self._logger.warning("Command thread not started")
            return False

        if command_name not in self.commands_config:
            self._logger.error(f"Unknown command: {command_name}")
            return False

        config = self.commands_config[command_name]
        client = self.node_service.create_client(
            config.data_type,
            config.server_node_id,
            config.port
        )
        
        if not client:
            self._logger.error(f"Failed to create client for {command_name}")
            return False

        try:
            request = self._build_request(command_name, config.data_type, params)
            response = await asyncio.wait_for(
                client.call(request),
                timeout=config.timeout
            )
            if response:
                print(f"命令 {command_name} 响应结果: {response}")
                return True
            return False
        except asyncio.TimeoutError:
            self._logger.warning(f"命令 {command_name} 超时")
            return False
        except Exception as e:
            self._logger.error(f"命令 {command_name} 失败: {e}")
            return False

    def _build_request(self, command_name: str, data_type: type, params: dict):
        """构建请求对象"""
        # 这里可以根据不同命令类型进行特殊处理
        # 默认情况下直接使用参数构造请求对象
        return data_type.Request(**params)

    async def stop(self):
        """停止所有命令任务"""
        self._active = False