# Copyright (c) 2023 Robotics and AI Institute LLC dba RAI Institute. All rights reserved.

import bosdyn.api.geometry_pb2
import geometry_msgs.msg
from proto2ros.conversions import convert


@convert.register(geometry_msgs.msg.Vector3, bosdyn.api.geometry_pb2.Vec3)
def convert_geometry_msgs_vector3_message_to_bosdyn_api_vec3_proto(
    ros_msg: geometry_msgs.msg.Vector3, proto_msg: bosdyn.api.geometry_pb2.Vec3
) -> None:
    """Convert from geometry_msgs/Vector3 ROS messages to bosdyn.api.Vec3 Protobuf messages."""
    proto_msg.x = ros_msg.x
    proto_msg.y = ros_msg.y
    proto_msg.z = ros_msg.z


@convert.register(bosdyn.api.geometry_pb2.Vec3, geometry_msgs.msg.Vector3)
def convert_bosdyn_api_vec3_proto_to_geometry_msgs_vector3_message(
    proto_msg: bosdyn.api.geometry_pb2.Vec3, ros_msg: geometry_msgs.msg.Vector3
) -> None:
    """Convert from bosdyn.api.Vec3 Protobuf messages to geometry_msgs/Vector3 ROS messages."""
    ros_msg.x = proto_msg.x
    ros_msg.y = proto_msg.y
    ros_msg.z = proto_msg.z


@convert.register(geometry_msgs.msg.Quaternion, bosdyn.api.geometry_pb2.Quaternion)
def convert_geometry_msgs_quaternion_message_to_bosdyn_api_quaternion_proto(
    ros_msg: geometry_msgs.msg.Quaternion, proto_msg: bosdyn.api.geometry_pb2.Quaternion
) -> None:
    """Convert from geometry_msgs/Quaternion ROS messages to bosdyn.api.Quaternion Protobuf messages."""
    proto_msg.w = ros_msg.w
    proto_msg.x = ros_msg.x
    proto_msg.y = ros_msg.y
    proto_msg.z = ros_msg.z


@convert.register(bosdyn.api.geometry_pb2.Quaternion, geometry_msgs.msg.Quaternion)
def convert_bosdyn_api_quaternion_proto_to_geometry_msgs_quaternion_message(
    proto_msg: bosdyn.api.geometry_pb2.Quaternion, ros_msg: geometry_msgs.msg.Quaternion
) -> None:
    """Convert from bosdyn.api.Quaternion Protobuf messages to geometry_msgs/Quaternion ROS messages."""
    ros_msg.w = proto_msg.w
    ros_msg.x = proto_msg.x
    ros_msg.y = proto_msg.y
    ros_msg.z = proto_msg.z


@convert.register(geometry_msgs.msg.Pose, bosdyn.api.geometry_pb2.SE3Pose)
def convert_geometry_msgs_pose_message_to_bosdyn_api_se3_pose_proto(
    ros_msg: geometry_msgs.msg.Pose, proto_msg: bosdyn.api.geometry_pb2.SE3Pose
) -> None:
    """Convert from geometry_msgs/Pose ROS messages to bosdyn.api.SE3Pose Protobuf messages."""
    convert_geometry_msgs_vector3_message_to_bosdyn_api_vec3_proto(ros_msg.position, proto_msg.position)
    convert_geometry_msgs_quaternion_message_to_bosdyn_api_quaternion_proto(ros_msg.orientation, proto_msg.rotation)


@convert.register(bosdyn.api.geometry_pb2.SE3Pose, geometry_msgs.msg.Pose)
def convert_bosdyn_api_se3_pose_proto_to_geometry_msgs_pose_message(
    proto_msg: bosdyn.api.geometry_pb2.SE3Pose, ros_msg: geometry_msgs.msg.Pose
) -> None:
    """Convert from bosdyn.api.SE3Pose Protobuf messages to geometry_msgs/Pose ROS messages."""
    convert_bosdyn_api_vec3_proto_to_geometry_msgs_vector3_message(proto_msg.position, ros_msg.position)
    convert_bosdyn_api_quaternion_proto_to_geometry_msgs_quaternion_message(proto_msg.rotation, ros_msg.orientation)


@convert.register(geometry_msgs.msg.Twist, bosdyn.api.geometry_pb2.SE3Velocity)
def convert_geometry_msgs_twist_message_to_bosdyn_api_se3_velocity_proto(
    ros_msg: geometry_msgs.msg.Twist, proto_msg: bosdyn.api.geometry_pb2.SE3Velocity
) -> None:
    """Convert from geometry_msgs/Twist ROS messages to bosdyn.api.SE3Velocity Protobuf messages."""
    convert_geometry_msgs_vector3_message_to_bosdyn_api_vec3_proto(ros_msg.linear, proto_msg.linear)
    convert_geometry_msgs_vector3_message_to_bosdyn_api_vec3_proto(ros_msg.angular, proto_msg.angular)


@convert.register(bosdyn.api.geometry_pb2.SE3Velocity, geometry_msgs.msg.Twist)
def convert_bosdyn_api_se3_velocity_proto_to_geometry_msgs_twist_message(
    proto_msg: bosdyn.api.geometry_pb2.SE3Velocity, ros_msg: geometry_msgs.msg.Twist
) -> None:
    """Convert from bosdyn.api.SE3Velocity Protobuf messages to geometry_msgs/Twist ROS messages."""
    convert_bosdyn_api_vec3_proto_to_geometry_msgs_vector3_message(proto_msg.linear, ros_msg.linear)
    convert_bosdyn_api_vec3_proto_to_geometry_msgs_vector3_message(proto_msg.angular, ros_msg.angular)


@convert.register(geometry_msgs.msg.Wrench, bosdyn.api.geometry_pb2.Wrench)
def convert_geometry_msgs_wrench_message_to_bosdyn_api_wrench_proto(
    ros_msg: geometry_msgs.msg.Wrench, proto_msg: bosdyn.api.geometry_pb2.Wrench
) -> None:
    """Convert from geometry_msgs/Wrench ROS messages to bosdyn.api.Wrench Protobuf messages."""
    convert_geometry_msgs_vector3_message_to_bosdyn_api_vec3_proto(ros_msg.force, proto_msg.force)
    convert_geometry_msgs_vector3_message_to_bosdyn_api_vec3_proto(ros_msg.torque, proto_msg.torque)


@convert.register(bosdyn.api.geometry_pb2.Wrench, geometry_msgs.msg.Wrench)
def convert_bosdyn_api_wrench_proto_to_geometry_msgs_wrench_message(
    proto_msg: bosdyn.api.geometry_pb2.Wrench, ros_msg: geometry_msgs.msg.Wrench
) -> None:
    """Convert from bosdyn.api.Wrench Protobuf messages to geometry_msgs/Wrench ROS messages."""
    convert_bosdyn_api_vec3_proto_to_geometry_msgs_vector3_message(proto_msg.force, ros_msg.force)
    convert_bosdyn_api_vec3_proto_to_geometry_msgs_vector3_message(proto_msg.torque, ros_msg.torque)
