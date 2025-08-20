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

static void nmt_state_change_callback(CO_NMT_internalState_t state)
{
	switch (state) {
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
		LOG_INF("NMT state: UNKNOWN (%d)", state);
		break;
	}
}
static void canopen_thread_entry(void *p1, void *p2, void *p3)
{
	LOG_INF("canopen_thread_entry");

	while (1) {
		k_msleep(10);
	}
}
K_THREAD_STACK_DEFINE(canopen_thread_stack, 2048);

static struct k_thread canopen_thread; ///< Thread control block

int creat_canopen_thread(void)
{

	k_thread_create(&canopen_thread, canopen_thread_stack,
			K_THREAD_STACK_SIZEOF(canopen_thread_stack), canopen_thread_entry, NULL,
			NULL, NULL, K_PRIO_COOP(6), 0, K_NO_WAIT);
	return 0;
}
SYS_INIT(creat_canopen_thread, APPLICATION, CONFIG_APPLICATION_INIT_PRIORITY);