// Copyright (c) 2024 Robotics and AI Institute LLC dba RAI Institute. All rights reserved.

#include "bosdyn_api_msgs/manual_conversions.hpp"

namespace bosdyn_api_msgs::conversions {

void Convert(const geometry_msgs::msg::Vector3& ros_msg, bosdyn::api::Vec3* proto_msg) {
  proto_msg->set_x(ros_msg.x);
  proto_msg->set_y(ros_msg.y);
  proto_msg->set_z(ros_msg.z);
}

void Convert(const bosdyn::api::Vec3& proto_msg, geometry_msgs::msg::Vector3* ros_msg) {
  ros_msg->x = proto_msg.x();
  ros_msg->y = proto_msg.y();
  ros_msg->z = proto_msg.z();
}

void Convert(const geometry_msgs::msg::Point& ros_msg, bosdyn::api::Vec3* proto_msg) {
  proto_msg->set_x(ros_msg.x);
  proto_msg->set_y(ros_msg.y);
  proto_msg->set_z(ros_msg.z);
}

void Convert(const bosdyn::api::Vec3& proto_msg, geometry_msgs::msg::Point* ros_msg) {
  ros_msg->x = proto_msg.x();
  ros_msg->y = proto_msg.y();
  ros_msg->z = proto_msg.z();
}

void Convert(const geometry_msgs::msg::Quaternion& ros_msg, bosdyn::api::Quaternion* proto_msg) {
  proto_msg->set_x(ros_msg.x);
  proto_msg->set_y(ros_msg.y);
  proto_msg->set_z(ros_msg.z);
  proto_msg->set_w(ros_msg.w);
}

void Convert(const bosdyn::api::Quaternion& proto_msg, geometry_msgs::msg::Quaternion* ros_msg) {
  ros_msg->x = proto_msg.x();
  ros_msg->y = proto_msg.y();
  ros_msg->z = proto_msg.z();
  ros_msg->w = proto_msg.w();
}

void Convert(const geometry_msgs::msg::Pose& ros_msg, bosdyn::api::SE3Pose* proto_msg) {
  Convert(ros_msg.position, proto_msg->mutable_position());
  Convert(ros_msg.orientation, proto_msg->mutable_rotation());
}

void Convert(const bosdyn::api::SE3Pose& proto_msg, geometry_msgs::msg::Pose* ros_msg) {
  Convert(proto_msg.position(), &ros_msg->position);
  Convert(proto_msg.rotation(), &ros_msg->orientation);
}

void Convert(const geometry_msgs::msg::Twist& ros_msg, bosdyn::api::SE3Velocity* proto_msg) {
  Convert(ros_msg.linear, proto_msg->mutable_linear());
  Convert(ros_msg.angular, proto_msg->mutable_angular());
}

void Convert(const bosdyn::api::SE3Velocity& proto_msg, geometry_msgs::msg::Twist* ros_msg) {
  Convert(proto_msg.linear(), &ros_msg->linear);
  Convert(proto_msg.angular(), &ros_msg->angular);
}

void Convert(const geometry_msgs::msg::Wrench& ros_msg, bosdyn::api::Wrench* proto_msg) {
  Convert(ros_msg.force, proto_msg->mutable_force());
  Convert(ros_msg.torque, proto_msg->mutable_torque());
}

void Convert(const bosdyn::api::Wrench& proto_msg, geometry_msgs::msg::Wrench* ros_msg) {
  Convert(proto_msg.force(), &ros_msg->force);
  Convert(proto_msg.torque(), &ros_msg->torque);
}

}  // namespace bosdyn_api_msgs::conversions
