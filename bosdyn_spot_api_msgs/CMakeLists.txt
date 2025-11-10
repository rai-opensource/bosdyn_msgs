# Copyright (c) 2023 Robotics and AI Institute LLC dba RAI Institute. All rights reserved.
cmake_minimum_required(VERSION 3.8)
project(bosdyn_spot_api_msgs)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(bosdyn_api_msgs REQUIRED)
find_package(proto2ros REQUIRED)

find_package(bosdyn_cmake_module REQUIRED)
find_package(bosdyn REQUIRED)  # always after bosdyn_cmake_module

fetch_spot_sdk(spotsdk)
file(GLOB ${PROJECT_NAME}_PROTOS
  "${spotsdk_SOURCE_DIR}/protos/bosdyn/api/spot/*.proto"
  "${spotsdk_SOURCE_DIR}/choreography_protos/bosdyn/api/spot/*.proto"
)

set(${PROJECT_NAME}_IMPORT_DIRS
  "${spotsdk_SOURCE_DIR}/protos"
  "${spotsdk_SOURCE_DIR}/choreography_protos"
)

proto2ros_vendor_package(${PROJECT_NAME}
  PROTOS ${${PROJECT_NAME}_PROTOS}
  IMPORT_DIRS ${${PROJECT_NAME}_IMPORT_DIRS}
  CONFIG_OVERLAYS config/overlay.yaml
  CPP_DEPENDENCIES bosdyn::bosdyn_api
  ROS_DEPENDENCIES bosdyn_api_msgs
)

ament_export_dependencies(
  bosdyn_api_msgs
  bosdyn_cmake_module
  geometry_msgs
  bosdyn
)

ament_package()
