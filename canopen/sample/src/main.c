/*
 * Copyright (c) 2019 Vestas Wind Systems A/S
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/kernel.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/sys/reboot.h>
#include <zephyr/settings/settings.h>
#include <canopennode.h>

#define LOG_LEVEL LOG_LEVEL_DBG
#include <zephyr/logging/log.h>
LOG_MODULE_REGISTER(testcanopen);
#define CAN_INTERFACE DEVICE_DT_GET(DT_CHOSEN(zephyr_canbus))
#define CAN_BITRATE                                                                                \
	(DT_PROP_OR(DT_CHOSEN(zephyr_canbus), bitrate,                                             \
		    DT_PROP_OR(DT_CHOSEN(zephyr_canbus), bus_speed, CONFIG_CAN_DEFAULT_BITRATE)) / \
	 1000)
/**
 * @brief 处理通信复位命令
 *
 * 重新初始化 CANopen 协议栈，但不影响应用程序状态
 */
static void handle_communication_reset(struct canopen_context *can)
{
	LOG_INF("Executing communication reset");

	// 删除当前的 CANopen 对象
	CO_delete(can);

	// 重新初始化协议栈
	CO_ReturnError_t err = CO_init(can, CONFIG_CANOPEN_NODE_ID, CAN_BITRATE);
	if (err != CO_ERROR_NO) {
		LOG_ERR("CO_init failed after communication reset (err = %d)", err);
		return;
	}

	// 设置 CAN 模块为正常模式
	CO_CANsetNormalMode(CO->CANmodule[0]);

	LOG_INF("Communication reset completed");
}

/**
 * @brief 处理应用复位命令
 *
 * 执行完整的应用复位，可以重新启动设备或重置应用状态
 */
static void handle_application_reset(void)
{
	LOG_INF("Executing application reset");
	k_msleep(10); // 等待LOG输出

	sys_reboot(SYS_REBOOT_COLD);
}

int main(void)
{
	CO_ReturnError_t err;
	struct canopen_context can;
	uint16_t timeout;
	uint32_t elapsed;
	int64_t timestamp;
	CO_NMT_internalState_t prev_nmt_state = CO_NMT_INITIALIZING;
	CO_NMT_reset_cmd_t prev_reset_cmd = CO_RESET_NOT;

	// 获取 CAN 接口设备
	can.dev = CAN_INTERFACE;
	if (!device_is_ready(can.dev)) {
		LOG_ERR("CAN interface not ready");
		return 0;
	}

	// 初始化对象字典上电计数器
	OD_powerOnCounter++;

	// 初始化 CANopen 协议栈
	err = CO_init(&can, CONFIG_CANOPEN_NODE_ID, CAN_BITRATE);
	if (err != CO_ERROR_NO) {
		LOG_ERR("CO_init failed (err = %d)", err);
		return 0;
	}

	LOG_INF("CANopen stack initialized with Node ID: %d", CONFIG_CANOPEN_NODE_ID);

	// 设置 CAN 模块为正常模式
	CO_CANsetNormalMode(CO->CANmodule[0]);

	// 主处理循环
	while (true) {
		timeout = 1U; // 默认超时时间（毫秒）
		timestamp = k_uptime_get();

		// 处理 CANopen 协议栈
		CO_NMT_reset_cmd_t reset = CO_process(CO, (uint16_t)elapsed, &timeout);

		// 检查 NMT 状态变化
		CO_NMT_internalState_t current_nmt_state = CO->NMT->operatingState;
		if (current_nmt_state != prev_nmt_state) {
			switch (current_nmt_state) {
			case CO_NMT_INITIALIZING:
				LOG_INF("NMT state: INITIALIZING");
				break;
			case CO_NMT_PRE_OPERATIONAL:
				LOG_INF("NMT state: PRE_OPERATIONAL");
				break;
			case CO_NMT_OPERATIONAL:
				LOG_INF("NMT state: OPERATIONAL");
				break;
			case CO_NMT_STOPPED:
				LOG_INF("NMT state: STOPPED");
				break;
			default:
				LOG_INF("NMT state: UNKNOWN (%d)", current_nmt_state);
				break;
			}
			prev_nmt_state = current_nmt_state;
		}

		// 检查并处理复位命令
		if (reset != CO_RESET_NOT && reset != prev_reset_cmd) {
			switch (reset) {
			case CO_RESET_COMM:
				LOG_INF("Received communication reset command");
				handle_communication_reset(&can);
				break;
			case CO_RESET_APP:
				LOG_INF("Received application reset command");
				handle_application_reset();
				// 注意：handle_application_reset() 可能不会返回
				break;
			default:
				LOG_INF("Received unknown reset command: %d", reset);
				break;
			}
			prev_reset_cmd = reset;
		} else if (reset == CO_RESET_NOT && prev_reset_cmd != CO_RESET_NOT) {
			// 复位命令已清除
			prev_reset_cmd = CO_RESET_NOT;
		}

		// 根据协议栈返回的超时值休眠
		if (timeout > 0) {
			k_sleep(K_MSEC(timeout));
			elapsed = (uint32_t)k_uptime_delta(&timestamp);
		} else {
			// 不需要休眠，继续处理
			elapsed = 0U;
		}
	}
}
