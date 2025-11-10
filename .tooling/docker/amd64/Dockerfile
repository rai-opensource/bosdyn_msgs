# Copyright (c) 2025 Robotics and AI Institute LLC dba RAI Institute. All rights reserved.

# Use a base image by OSRF that already contains ROS 2 Humble
FROM ros:humble-ros-base-jammy

RUN apt-get update && apt-get install -y \
    git \
    python3-pip \
    python3-bloom \
    makeself \
    dpkg-dev \
    debhelper \
    wget && \
  rm -rf /var/lib/apt/lists/*

COPY .tooling/pip/pip.conf /etc/pip.conf
COPY pip-constraint.txt /etc/pip/constraint.txt

CMD ["bash"]
