"""
命令执行线程
功能:
1. 管理电机控制命令的执行
2. 实现速度循环控制
3. 处理刹车等特殊命令
"""

import asyncio
import logging
from typing import Dict, Any, Optional

# === 自定义模块导入 ===
from MotorAsst.drivers.can.transport import CANNodeService
from MotorAsst.config.configdrivers import DriverConfig

class CommandThread:

    def __init__(self, node_service: CANNodeService, commands_config: Dict[str, Any]):
        """初始化命令线程"""
        self.node_service = node_service
        self.commands_config = commands_config
        self._logger = logging.getLogger(self.__class__.__name__)
        self._active = False
        self._velocity_loop_task: Optional[asyncio.Task] = None

    async def start(self):
        """启动命令线程"""
        self._active = True
        self._logger.info("命令线程已启动")

    async def send_command(self, command_name: str, params: Dict) -> bool:
        """
        发送命令统一接口
        参数:
            command_name: 命令名称
            params: 命令参数字典
        返回:
            命令执行结果(bool)
        """
        if not self._active:
            self._logger.warning("命令线程未启动")
            return False

        if command_name not in self.commands_config:
            self._logger.error(f"未知命令: {command_name}")
            return False

        if command_name == "OperateBrake":
            return await self._send_brake_command(params)

        return await self._send_single_command(command_name, params)

    async def start_velocity_loop(self, 
                                initial_velocity: Dict[str, float],
                                interval_ms: int = 200,
                                duration_per_direction: float = 5.0,
                                cycles: int = 20):
        """
        启动速度循环控制
        :param initial_velocity: 初始速度 {left: x, right: y}
        :param interval_ms: 发送间隔(毫秒)
        :param duration_per_direction: 每个方向持续时间(秒)
        :param cycles: 循环次数
        """
        await self._stop_velocity_loop()
        self._velocity_loop_task = asyncio.create_task(
            self._velocity_control_loop(
                initial_velocity,
                interval_ms,
                duration_per_direction,
                cycles
            )
        )

    async def _stop_velocity_loop(self):
        """停止速度循环控制"""
        if self._velocity_loop_task:
            self._velocity_loop_task.cancel()
            try:
                await self._velocity_loop_task
            except asyncio.CancelledError:
                self._logger.info("速度循环控制已停止")
            self._velocity_loop_task = None

    async def _velocity_control_loop(self,
                                   initial_velocity: Dict[str, float],
                                   interval_ms: int,
                                   duration_per_direction: float,
                                   cycles: int):
        """速度控制循环逻辑（带归零停顿）"""
        try:
            current_velocity = initial_velocity.copy()
            interval_sec = interval_ms / 1000
            iterations_per_direction = int(duration_per_direction / interval_sec)
            
            for cycle in range(cycles * 2):  # 每个循环包含正向和反向
                # 正常速度发送阶段
                for _ in range(iterations_per_direction):
                    if not self._active:
                        return
                    await self._send_single_command("SetVelocity", current_velocity)
                    await asyncio.sleep(interval_sec)
                
                # 归零阶段
                zero_velocity = {k: 0.0 for k in current_velocity}
                await self._send_single_command("SetVelocity", zero_velocity)
                self._logger.info(f"速度已归零，等待2秒后反转")
                await asyncio.sleep(2.0)  # 归零后等待2秒
                
                # 反转速度方向
                current_velocity = {k: -v for k, v in current_velocity.items()}
                self._logger.info(f"速度方向已反转: {current_velocity}")

        except asyncio.CancelledError:
            self._logger.info("速度循环控制被取消")
        except Exception as ex:
            self._logger.error(f"速度循环控制异常: {ex}")
        finally:
            # 确保最终速度为0
            await self._send_single_command("SetVelocity", 
                {k: 0.0 for k in current_velocity})
            self._logger.info("速度循环控制完成")

    async def _send_brake_command(self, params: Dict) -> bool:
        """执行刹车操作命令"""
        try:
            return await self._send_single_command("OperateBrake", {
                "method": params.get("method", 0),
                "name": params.get("name", "m-brake"),
                "param": params.get("param", "")
            })
        except Exception as e:
            self._logger.error(f"刹车命令执行失败: {e}")
            return False

    async def _send_single_command(self, command_name: str, params: Dict) -> bool:
        """执行单次命令"""
        config = self.commands_config[command_name]  # 直接访问字典
        client = None
        
        try:
            client = self.node_service.create_client(
                config.data_type,
                config.server_node_id,
                config.port
            )
            
            if not client:
                self._logger.error(f"创建{command_name}客户端失败")
                return False

            request = self._build_request(command_name, params)
            response = await asyncio.wait_for(
                client.call(request),
                timeout=config.timeout
            )
            
            if response:
                self._logger.info(f"命令 {command_name} 执行成功")
                return True
            return False
                
        except asyncio.TimeoutError:
            self._logger.warning(f"命令 {command_name} 超时")
            return False
        except Exception as e:
            self._logger.error(f"命令 {command_name} 执行失败: {e}")
            return False
        finally:
            if client:
                client.close()

    def _build_request(self, command_name: str, params: Dict) -> Any:
        """构建请求对象（特殊处理速度指令）"""
        if command_name == "SetVelocity":
            # 直接从DriverConfig调用构建方法
            from MotorAsst.config.configdrivers import DriverConfig
            return DriverConfig.build_velocity_request(params)
        return self.commands_config[command_name].data_type.Request(**params)

    async def stop(self):
        """停止命令线程"""
        self._active = False
        self._logger.info("命令线程已停止")