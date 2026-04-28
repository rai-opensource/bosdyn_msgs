<!-- Copyright (c) 2025 Robotics and AI Institute LLC dba RAI Institute. All rights reserved. -->

# bosdyn_msgs

![SDK Support](https://img.shields.io/badge/SDK-3.3.2%20%7C%204.0.0%20%7C%204.0.2%20%7C%205.0.1-blue)
![C++ Support](https://img.shields.io/badge/C++-17%20%7C%2020-blue)
![Python Support](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)
![ROS Support](https://img.shields.io/badge/ROS-humble-blue)

# Repository Migration Notice

> [!IMPORTANT]
> This repository has moved to the **RAI-Opensource** GitHub organization!
>
> Current status: **Migrated**.
> - Migration target org: https://github.com/RAI-Opensource
> - Previous target org: https://github.com/bdaiinstitute
>
> What to do now:
> - Update your git remote:
>   ```bash
>   git remote set-url origin https://github.com/RAI-Opensource/bosdyn_msgs
>   ```
> - If you maintain downstream docs/scripts, update links from this repository to the new org.


## Overview

`bosdyn_msgs` offers an interoperability layer between Boston Dynamics Spot SDK and ROS 2 aware code by providing ROS 2 messages equivalent to [Spot SDK Protobuf messages](https://github.com/boston-dynamics/spot-sdk/tree/master/protos), as well bi-directional conversion APIs in C++ and Python.

## Packages

This repository contains the following packages:

| Package | Description |
|:--------|:------------|
| [`bosdyn_msgs`](bosdyn_msgs) | ROS 2 interoperability support for the Boston Dynamics Spot SDK (metapackage) |
| [`bosdyn_api_msgs`](bosdyn_api_msgs) | ROS 2 interoperability support for `bosdyn.api`, `bosdyn.api.gps`, and `bosdyn.api.docking` APIs |
| [`bosdyn_spot_api_msgs`](bosdyn_spot_api_msgs) | ROS 2 interoperability support for `bosdyn.api.spot` APIs |
| [`bosdyn_spot_cam_api_msgs`](bosdyn_spot_cam_api_msgs) | ROS 2 interoperability support for `bosdyn.api.spot_cam` APIs |
| [`bosdyn_mission_api_msgs`](bosdyn_mission_api_msgs) | ROS 2 interoperability support for `bosdyn.api.mission` APIs |
| [`bosdyn_autowalk_api_msgs`](bosdyn_autowalk_api_msgs) | ROS 2 interoperability support for `bosdyn.api.autowalk` APIs |
| [`bosdyn_graph_nav_api_msgs`](bosdyn_graph_nav_api_msgs) | ROS 2 interoperability support for `bosdyn.api.graph_nav` APIs |
| [`bosdyn_keepalive_api_msgs`](bosdyn_keepalive_api_msgs) | ROS 2 interoperability support for `bosdyn.api.keepalive` APIs |
| [`bosdyn_log_status_api_msgs`](bosdyn_log_status_api_msgs) | ROS 2 interoperability support for `bosdyn.api.log_status` APIs |
| [`bosdyn_auto_return_api_msgs`](bosdyn_auto_return_api_msgs) | ROS 2 interoperability support for `bosdyn.api.auto_return` APIs |
| [`bosdyn_metrics_logging_api_msgs`](bosdyn_metrics_logging_api_msgs) | ROS 2 interoperability support for `bosdyn.api.metrics_logging` APIs |
| [`bosdyn_cmake_module`](bosdyn_cmake_module) | CMake modules for the Boston Dynamics Spot SDK |

## User guides

### Installing `bosdyn_msgs`

Just grab a binary bundle for your architecture (e.g. downloaded from available [releases ](https://github.com/rai-opensource/bosdyn_msgs/releases)) and execute it.

Packages will be installed alongside your ROS 2 distribution (e.g. under `/opt/ros/<distribution>`).

### Using `bosdyn_msgs` in C++

```c++
#include <cassert>

#include <bosdyn/api/robot_state.pb.h>

#include <bosdyn_api_msgs/msg/motor_temperature.hpp>
#include <bosdyn_api_msgs/conversions.hpp>

int main() {
    // Instantiate a Spot SDK Protobuf message.
    auto proto_message = bosdyn::api::MotorTemperature{};
    proto_message.set_name("wr0_joint_motor");
    proto_message.set_temperature(34.0);

    // Convert the Protobuf message to its ROS 2 equivalent.
    auto ros_message = bosdyn_api_msgs::msg::MotorTemperature{};
    bosdyn_api_msgs::conversions::convert(proto_message, &ros_message);
    assert(proto_message.name() == ros_message.name);
    assert(proto_message.temperature() == ros_message.temperature);

    // Convert the ROS 2 message back to Protobuf message form.
    auto other_proto_message = bosdyn::api::MotorTemperature{};
    bosdyn_api_msgs::conversions::convert(ros_message, &other_proto_message)
    assert(proto_message.name() == other_proto_message.name());
    assert(proto_message.temperature() == other_proto_message.temperature());
}
```

Note the header naming and namespacing patterns in `bosdyn_msgs` packages.
These lead to the following procedure when working with `bosdyn_msgs` in C++:

1. Look up the Protobuf package on which the Protobuf message of interest is defined.
2. Look up the ROS 2 package that maps interfaces from the corresponding Protobuf package.
3. Include the header for the corresponding Protobuf package:

   ```c++
   #include <path/to/proto/package.pb.h>
   ```

4. Include the header for the corresponding ROS 2 package and message, like:

   ```c++
   #include <path/to/ros/package/msg/snake_cased_message_name.hpp>
   ```

5. Include the header exposing conversion APIs:

   ```c++
   #include <path/to/ros/package/conversions.hpp>
   ```

6. Use `proto::package::MessageName` and `ros_package::msg::MessageName` messages, converting back and forth using `ros_package::conversions::convert()` overloads.

### Using `bosdyn_msgs` in Python

```python
import bosdyn.api.robot_state_pb2

import bosdyn_api_msgs.msg
from bosdyn_api_msgs.conversions import convert

proto_message = bosdyn.api.robot_state_pb2.MotorTemperature()
proto_message.name = "wr0_joint_motor"
proto_message.temperature = 34.0

ros_message = bosdyn_api_msgs.msg.MotorTemperature()
convert(proto_message, ros_message)
assert proto_message.name == ros_message.name
assert proto_message.temperature == ros_message.temperature

other_proto_message = bosdyn.api.robot_state_pb2.MotorTemperature()
convert(ros_message, other_proto_message)
assert proto_message.name == other_proto_message.name
assert proto_message.temperature == other_proto_message.temperature
```

Note the module naming pattern for `bosdyn_msgs` packages.
This leads to the following procedure when working with `bosdyn_msgs` in Python:

1. Look up the Protobuf package on which the Protobuf message of interest is defined.
2. Look up the ROS 2 package that maps interfaces from the corresponding Protobuf package.
3. Import the module for the corresponding Protobuf package:

   ```python
   import proto.package_pb2
   ```

4. Import the module for the corresponding ROS 2 package, like:

   ```python
   import ros_package.msg
   ```

5. Import conversion APIs:

   ```c++
   from ros_package.conversions import convert
   ```

6. Use `proto.package_pb2.MessageName` and `ros_package.msg.MessageName` messages, converting back and forth using `convert()` overloads.

### Using `bosdyn_msgs` for ROS 2 interfaces

```
# LocomotionStatus.msg
bosdyn_api_msgs/MotorTemperature[] temperatures
```

Note the message naming pattern. As elsewhere, the procedure boils down to identifying the ROS 2 package that contains the Protobuf message of interest.

## Developer guides

### Releasing `bosdyn_msgs`

Just push a tag with an appropriate release version to this repository e.g.:

``` bash
git tag MAJOR.MINOR.PATCH
git push origin MAJOR.MINOR.PATCH
```

This will trigger a release job. Once the release is complete, `bosdyn_msgs-bundle_MAJOR.MINOR.PATCH-*.run`
binary bundles will be made available as release assets. As of January 2024, releases include binary
bundles compatible with ROS 2 Humble Hawksbill on Ubuntu Jammy 22.04 for AMD64 and ARM64 architectures.

**Attention**: it is strongly advised to keep package versions and tags in lockstep with the version of the
latest Boston Dynamics Spot SDK release to PyPI. This can be achieved by updating versions in `package.xml`
files and `pip-constraint.txt` file to match each other and the tag.

### Bundling `bosdyn_msgs`

First, ensure QEMU virtualization for multi-platform Docker containers is enabled:

```sh
sudo apt-get install qemu binfmt-support qemu-user-static
sudo docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
```

Now, simply invoke `make -jN` at the repostory root with a suitable number of jobs `N`.
This will build `bosdyn_msgs_unknown-bundle-amd64.run` and `bosdyn_msgs_unknown-bundle-arm64.run`
binary bundles (of `unknown` version, as none was specified).

You can also bundle fewer packages for specific architectures with:

``` bash
make -jN <package_name>-bundle-<arch>.run
```

Binary bundles include the target package and its local dependencies.

**Note**: QEMU virtualization makes for _very_ slow builds (from minutes to hours).

### Building `bosdyn_msgs`

You can build these packages in `colcon` workspaces, like you would for any other ROS 2 package.
First, ensure [ROS 2 Humble Hawksbill](https://docs.ros.org/en/humble/Installation.html) is installed.
That includes development tools:

``` bash
sudo apt update && sudo apt install -y python3-pip ros-dev-tools
```

Then clone this repository into a workspace:

``` bash
mkdir -p workspace/src; cd workspace
git -C src clone --recursive https://github.com/rai-opensource/bosdyn_msgs.git
```

When installing package dependencies, make sure `pip` constraints are enforced:

``` bash
PIP_CONSTRAINT=src/bosdyn_msgs/pip-constraint.txt rosdep install -i -y --from-path src --skip-keys "$(cat src/bosdyn_msgs/rosdep-skip.txt)"
```

This will ensure `apt` and `pip` managed packages are compatible with each other.

Unfortunately, this is not yet enough. There are a few dependencies that are distributed separately:

``` bash
ARCH=amd64  # or arm64
for url in $(cat ${ARCH}-dpkg.txt); do wget $url && sudo apt install -y ./$(basename $url); done
```

Finally, you can now build:

``` bash
colcon build
```
