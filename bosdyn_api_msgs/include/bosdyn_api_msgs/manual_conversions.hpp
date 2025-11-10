// Copyright (c) 2024 Robotics and AI Institute LLC dba RAI Institute. All rights reserved.

#pragma once

#include <bosdyn/api/geometry.pb.h>

#include <geometry_msgs/msg/vector3.hpp>
#include <geometry_msgs/msg/quaternion.hpp>
#include <geometry_msgs/msg/pose.hpp>
#include <geometry_msgs/msg/twist.hpp>
#include <geometry_msgs/msg/wrench.hpp>

namespace bosdyn_api_msgs::conversions {

/// Convert from geometry_msgs/Vector3 ROS messages to bosdyn.api.Vec3 Protobuf messages.
void Convert(const geometry_msgs::msg::Vector3& ros_msg, bosdyn::api::Vec3* proto_msg);

/// Convert from bosdyn.api.Vec3 Protobuf messages to geometry_msgs/Vector3 ROS messages.
void Convert(const bosdyn::api::Vec3& proto_msg, geometry_msgs::msg::Vector3* ros_msg);

/// Convert from geometry_msgs/Point ROS messages to bosdyn.api.Vec3 Protobuf messages.
void Convert(const geometry_msgs::msg::Point& ros_msg, bosdyn::api::Vec3* proto_msg);

/// Convert from bosdyn.api.Vec3 Protobuf messages to geometry_msgs/Point ROS messages.
void Convert(const bosdyn::api::Vec3& proto_msg, geometry_msgs::msg::Point* ros_msg);

/// Convert from geometry_msgs/Quaternion ROS messages to bosdyn.api.Quaternion Protobuf messages.
void Convert(const geometry_msgs::msg::Quaternion& ros_msg, bosdyn::api::Quaternion* proto_msg);

/// Convert from bosdyn.api.Quaternion Protobuf messages to geometry_msgs/Quaternion ROS messages.
void Convert(const bosdyn::api::Quaternion& proto_msg, geometry_msgs::msg::Quaternion* ros_msg);

/// Convert from geometry_msgs/Pose ROS messages to bosdyn.api.SE3Pose Protobuf messages.
void Convert(const geometry_msgs::msg::Pose& ros_msg, bosdyn::api::SE3Pose* proto_msg);

/// Convert from bosdyn.api.SE3Pose Protobuf messages to geometry_msgs/Pose ROS messages.
void Convert(const bosdyn::api::SE3Pose& proto_msg, geometry_msgs::msg::Pose* ros_msg);

/// Convert from geometry_msgs/Twist ROS messages to bosdyn.api.SE3Velocity Protobuf messages.
void Convert(const geometry_msgs::msg::Twist& ros_msg, bosdyn::api::SE3Velocity* proto_msg);

/// Convert from bosdyn.api.SE3Velocity Protobuf messages to geometry_msgs/Twist ROS messages.
void Convert(const bosdyn::api::SE3Velocity& proto_msg, geometry_msgs::msg::Twist* ros_msg);

/// Convert from geometry_msgs/Wrench ROS messages to bosdyn.api.Wrench Protobuf messages.
void Convert(const geometry_msgs::msg::Wrench& ros_msg, bosdyn::api::Wrench* proto_msg);

/// Convert from bosdyn.api.Wrench Protobuf messages to geometry_msgs/Wrench ROS messages.
void Convert(const bosdyn::api::Wrench& proto_msg, geometry_msgs::msg::Wrench* ros_msg);

}  // namespace bosdyn_api_msgs::conversions
