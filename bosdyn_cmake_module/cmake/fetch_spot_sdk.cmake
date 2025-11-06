# Copyright (c) 2024 Robotics and AI Institute LLC dba RAI Institute. All rights reserved.

macro(fetch_spot_sdk target)
  get_executable_path(PYTHON_EXECUTABLE Python3::Interpreter CONFIGURE)
  execute_process(COMMAND ${PYTHON_EXECUTABLE} -c
    "from importlib.metadata import version; print(version('bosdyn-api'), end='')"
    OUTPUT_VARIABLE version COMMAND_ERROR_IS_FATAL ANY
  )
  FetchContent_Declare(
    ${target}
    GIT_REPOSITORY https://github.com/boston-dynamics/spot-sdk.git
    GIT_TAG v${version})
  FetchContent_Populate(${target})
endmacro()
