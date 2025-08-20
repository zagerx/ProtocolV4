#target_sources(objdict/CO_OD.c)



zephyr_library_sources(${CMAKE_CURRENT_SOURCE_DIR}/objdict/CO_OD.c)
zephyr_library_sources(${CMAKE_CURRENT_SOURCE_DIR}/test.c)

zephyr_include_directories(objdict)
