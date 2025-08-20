# Copyright (c) 2021 Teslabs Engineering S.L.
# SPDX-License-Identifier: Apache-2.0

if(CONFIG_UAVCAN_ENABLE)
	add_subdirectory(uavcan)
endif()
if(CONFIG_CANOPEN)
	add_subdirectory(canopen)
endif()