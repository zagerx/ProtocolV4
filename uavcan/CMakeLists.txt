# Copyright (c) 2021 Teslabs Engineering S.L.
# SPDX-License-Identifier: Apache-2.0

zephyr_library_sources(
    ${CMAKE_CURRENT_SOURCE_DIR}/libcanard/libcanard/canard.c
)

zephyr_include_directories(
    .cFolder/
    libcanard/libcanard/
)

