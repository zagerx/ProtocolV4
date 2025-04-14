import asyncio
import logging
from typing import Dict, Optional
from MotorAsst.drivers.can.transport import CANNodeService
from MotorAsst.config.configdrivers import CommandConfig

class CommandThread:
    def __init__(self, node_service: CANNodeService, commands_config: Dict[str, CommandConfig]):
        self.node_service = node_service
        self.commands_config = commands_config
        self._logger = logging.getLogger(self.__class__.__name__)
        self._active = False
        self._periodic_tasks: Dict[str, asyncio.Task] = {}

    async def start(self):
        """启动命令线程"""
        self._active = True

    async def send_command(self, command_name: str, params: dict) -> bool:
        """发送命令（根据配置决定执行方式）"""
        if not self._active:
            self._logger.warning("Command thread not started")
            return False

        if command_name not in self.commands_config:
            self._logger.error(f"Unknown command: {command_name}")
            return False

        config = self.commands_config[command_name]
        
        if config.execution_mode == "periodic":
            return await self._start_periodic_command(command_name, params, config.interval)
        else:
            return await self._send_single_command(command_name, params)

    async def _send_single_command(self, command_name: str, params: dict) -> bool:
        """发送单次命令（每次创建新客户端）"""
        config = self.commands_config[command_name]
        client = None
        
        try:
            # 创建新客户端
            client = self.node_service.create_client(
                config.data_type,
                config.server_node_id,
                config.port
            )
            
            if not client:
                self._logger.error(f"Failed to create client for {command_name}")
                return False

            request = self._build_request(command_name, config.data_type, params)
            self._logger.debug(f"Sending {command_name} request")
            
            response = await asyncio.wait_for(
                client.call(request),
                timeout=config.timeout
            )
            
            if response:
                self._logger.info(f"命令 {command_name} 成功: {response}")
                return True
            return False
                
        except asyncio.TimeoutError:
            self._logger.warning(f"命令 {command_name} 超时")
            return False
        except Exception as e:
            self._logger.error(f"命令 {command_name} 失败: {e}", exc_info=True)
            return False
        finally:
            # 确保客户端被清理
            if client is not None:
                client.close()

    async def _start_periodic_command(self, command_name: str, params: dict, interval: float) -> bool:
        """启动周期性命令"""
        if command_name in self._periodic_tasks:
            self._logger.warning(f"Periodic command {command_name} already running")
            return False

        async def _periodic_task():
            while self._active:
                try:
                    start_time = asyncio.get_event_loop().time()
                    success = await self._send_single_command(command_name, params)
                    elapsed = asyncio.get_event_loop().time() - start_time
                    
                    if not success:
                        self._logger.warning(f"Periodic command {command_name} failed")
                    
                    sleep_time = max(0, interval - elapsed)
                    await asyncio.sleep(sleep_time)
                    
                except asyncio.CancelledError:
                    break
                except Exception as e:
                    self._logger.error(f"Periodic command {command_name} failed: {e}")
                    break

        self._periodic_tasks[command_name] = asyncio.create_task(_periodic_task())
        return True

    async def stop_periodic_command(self, command_name: str) -> bool:
        """停止指定的周期性命令"""
        task = self._periodic_tasks.pop(command_name, None)
        if task:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
            return True
        return False

    def _build_request(self, command_name: str, data_type: type, params: dict):
        """构建请求对象"""
        return data_type.Request(**params)

    async def stop(self):
        """停止所有命令任务"""
        self._active = False
        for task in self._periodic_tasks.values():
            task.cancel()
        await asyncio.gather(*self._periodic_tasks.values(), return_exceptions=True)
        self._periodic_tasks.clear()