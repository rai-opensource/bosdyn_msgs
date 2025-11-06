# Copyright (c) 2023 Robotics and AI Institute LLC dba RAI Institute. All rights reserved.

from typing import Callable, Optional, Tuple, Union

import google.protobuf.duration_pb2
import google.protobuf.timestamp_pb2
from bosdyn.api.graph_nav import nav_pb2
from bosdyn.client.math_helpers import Quat, SE2Pose, SE3Pose
from builtin_interfaces.msg import Time
from geometry_msgs.msg import (
    Point,
    Pose,
    Pose2D,  # Note: Pose2D is deprecated
    PoseStamped,
    Quaternion,
    Transform,
    TransformStamped,
    Vector3,
)


def ros_transform_to_se3_pose(transform: Transform) -> SE3Pose:
    return SE3Pose(
        transform.translation.x,
        transform.translation.y,
        transform.translation.z,
        Quat(
            transform.rotation.w,
            transform.rotation.x,
            transform.rotation.y,
            transform.rotation.z
        )
    )


def ros_pose_to_se3_pose(pose: Pose) -> SE3Pose:
    return SE3Pose(
        pose.position.x,
        pose.position.y,
        pose.position.z,
        Quat(
            pose.orientation.w,
            pose.orientation.x,
            pose.orientation.y,
            pose.orientation.z
        )
    )


def se2_pose_to_ros_pose2(se2_pose: SE2Pose) -> Pose2D:
    return Pose2D(x=se2_pose.x, y=se2_pose.y, theta=se2_pose.angle)


def se3_pose_to_ros_pose(se3_pose: SE3Pose) -> Pose:
    return Pose(
        position=Point(
            x=float(se3_pose.x),
            y=float(se3_pose.y),
            z=float(se3_pose.z)
        ),
        orientation=Quaternion(
            w=float(se3_pose.rot.w),
            x=float(se3_pose.rot.x),
            y=float(se3_pose.rot.y),
            z=float(se3_pose.rot.z)
        ),
    )


def se3_pose_to_ros_transform(se3_pose: SE3Pose) -> Transform:
    return Transform(
        translation=Vector3(
            x=float(se3_pose.x),
            y=float(se3_pose.y),
            z=float(se3_pose.z)
        ),
        rotation=Quaternion(
            w=float(se3_pose.rot.w),
            x=float(se3_pose.rot.x),
            y=float(se3_pose.rot.y),
            z=float(se3_pose.rot.z)
        ),
    )


def bosdyn_pose_to_msg(
    frame_t_pose: SE3Pose, frame: Optional[str], local_stamp: Optional[Time] = None
) -> PoseStamped:
    """
    Convert an SE3Pose object into a ROS PoseStamped message.

    Note that the user is expected to pass in the local timestamp for the resulting message.

    Args:
        frame_t_pose: SE3Pose in frame 'frame'
        frame: the name of the frame the pose is with respect to
        local_stamp: the local timestamp for the returned message.

    Returns:
        PoseStamped message: google.protobuf.Timestamp
    """
    pose_stamped = PoseStamped()
    pose_stamped.header.stamp = local_stamp
    pose_stamped.header.frame_id = frame
    pose_stamped.pose.position.x = frame_t_pose.position.x
    pose_stamped.pose.position.y = frame_t_pose.position.y
    pose_stamped.pose.position.z = frame_t_pose.position.z
    pose_stamped.pose.orientation.x = frame_t_pose.rotation.x
    pose_stamped.pose.orientation.y = frame_t_pose.rotation.y
    pose_stamped.pose.orientation.z = frame_t_pose.rotation.z
    pose_stamped.pose.orientation.w = frame_t_pose.rotation.w
    return pose_stamped


def bosdyn_pose_to_tf(
    frame_t_pose: SE3Pose,
    frame: Optional[str],
    child_frame: Optional[str],
    local_stamp: Optional[Time] = None
) -> TransformStamped:
    """
    Convert an SE3Pose object into a ROS TransformStamped object.

    The transform would be between frame->child_frame.  Note that
    the user is expected to pass in the local timestamp for the
    returned message.

    Args:
        frame_t_pose: SE3Pose in frame 'frame'
        frame: the name of the frame this transform is with respect to
        child_frame: the name of the frame whose origin is defined by the given pose
        local_stamp: the local timestamp for the returned message.

    Returns:
        TransformStamped message
    """
    tfmsg = TransformStamped()
    tfmsg.header.stamp = local_stamp
    tfmsg.header.frame_id = frame
    tfmsg.child_frame_id = child_frame
    tfmsg.transform.translation.x = frame_t_pose.position.x
    tfmsg.transform.translation.y = frame_t_pose.position.y
    tfmsg.transform.translation.z = frame_t_pose.position.z
    tfmsg.transform.rotation.x = frame_t_pose.rotation.x
    tfmsg.transform.rotation.y = frame_t_pose.rotation.y
    tfmsg.transform.rotation.z = frame_t_pose.rotation.z
    tfmsg.transform.rotation.w = frame_t_pose.rotation.w
    return tfmsg


def bosdyn_localization_to_pose_msg(
    localization: nav_pb2.Localization,
    robot_to_local_time: Callable[
        [google.protobuf.timestamp_pb2.Timestamp],
        google.protobuf.timestamp_pb2.Timestamp
    ],
    in_seed_frame: bool = True,
    seed_frame: Optional[str] = None,
    body_frame: Optional[str] = None,
    return_tf: bool = True,
) -> Optional[Union[PoseStamped, Tuple[PoseStamped, TransformStamped]]]:
    """
    Extract PoseStamped pose from a Localization proto object.

    Returns a PoseStamped message and optionally a TransformStamped message.
    If 'in_seed_frame' is True, then the pose would be with respect to the seed
    frame (given by 'seed_frame'). Otherwise, the pose would be with respect to
    localization.waypoint_id, which is the waypoint the Localization object is
    relative to.

    The pose will itself define the origin of a frame called 'body_frame'

    Args:
        localization: the Localization object obtained from e.g. GetLocalizationState RPC.
        robot_to_local_time: Function to convert the robot time to the local time
        in_seed_frame: True if the resulting pose should be in seed frame
        seed_frame: The name of the seed frame in ROS context.
        body_frame: the origin of a frame defined by the pose;
        only necessary when 'return_tf' is True
        return_tf: returns a TransformStamped message as well

    Returns:
        if return_tf is True:
           (PoseStamped, TransformStamped)
        else:
            PoseStamped
    """
    if not localization.waypoint_id:
        # the robot is not yet localized
        return None
    if in_seed_frame and seed_frame is None:
        raise ValueError("seed_frame must not be None if in_seed_frame is True")
    if return_tf and body_frame is None:
        raise ValueError(
            "body_frame must not be None if return_tf is True; Constructing"
            "a TransformStamped message requires knowing body_frame."
        )

    local_time = robot_to_local_time(localization.timestamp)
    local_stamp = Time(sec=local_time.seconds, nanosec=local_time.nanos)
    if in_seed_frame:
        seed_t_body_proto = localization.seed_tform_body
        pose_msg = bosdyn_pose_to_msg(seed_t_body_proto, seed_frame, local_stamp)
        if return_tf:
            trans_msg = bosdyn_pose_to_tf(seed_t_body_proto, seed_frame, body_frame, local_stamp)
    else:
        waypoint_frame = localization.waypoint_id
        waypoint_t_body_proto = localization.waypoint_tform_body
        pose_msg = bosdyn_pose_to_msg(waypoint_t_body_proto, waypoint_frame, local_stamp)
        if return_tf:
            trans_msg = bosdyn_pose_to_tf(
                waypoint_t_body_proto, waypoint_frame, body_frame, local_stamp)
    if return_tf:
        return pose_msg, trans_msg
    else:
        return pose_msg
