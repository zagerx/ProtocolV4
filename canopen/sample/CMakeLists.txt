
#zephyr_library_sources(${CMAKE_CURRENT_SOURCE_DIR}/objdict/CO_OD.c)
#zephyr_library_sources(${CMAKE_CURRENT_SOURCE_DIR}/test.c)
#zephyr_include_directories(objdict)

# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.20.0)
set(BOARD_ROOT ${CMAKE_CURRENT_SOURCE_DIR})



find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(canopen_app)


target_sources(app PRIVATE
    src/main.c
    src/canopen_program.c
    objdict/CO_OD.c
)
zephyr_include_directories(objdict)
