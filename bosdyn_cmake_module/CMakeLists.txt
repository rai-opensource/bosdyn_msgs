# Copyright (c) 2024 Robotics and AI Institute LLC dba RAI Institute. All rights reserved.
cmake_minimum_required(VERSION 3.12)
project(bosdyn_cmake_module)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY cmake
  DESTINATION share/${PROJECT_NAME}
)

set(BOSDYN_CMAKE_PREFIX_PATH /opt/spot-cpp-sdk)

find_package(bosdyn REQUIRED PATHS "${BOSDYN_CMAKE_PREFIX_PATH}")

get_target_property(BOSDYN_API_SO_LOCATION bosdyn::bosdyn_api IMPORTED_LOCATION_RELEASE)
get_filename_component(BOSDYN_LIBRARY_PATH "${BOSDYN_API_SO_LOCATION}" DIRECTORY)
set(AMENT_CMAKE_ENVIRONMENT_HOOKS_DESC_library_path
  "prepend-non-duplicate;LD_LIBRARY_PATH;${BOSDYN_LIBRARY_PATH}"
)
ament_environment_hooks(cmake/templates/library_path.sh.in)

ament_package(CONFIG_EXTRAS cmake/templates/bosdyn_cmake_module-extras.cmake.in)
