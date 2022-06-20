FROM ros:noetic
ENV DEBIAN_FRONTEND noninteractive


# Franka ROS install
RUN apt-get update && apt-get install -y ros-noetic-libfranka ros-noetic-franka-ros

# MoveIt install
RUN rosdep update
RUN apt-get install -y ros-noetic-catkin python3-catkin-tools python3-osrf-pycommon python3-wstool git
WORKDIR /ws_moveit/src
RUN wstool init .
RUN wstool merge -t . https://raw.githubusercontent.com/ros-planning/moveit/master/moveit.rosinstall
RUN wstool remove  moveit_tutorials  # this is cloned in the next section
RUN wstool update -t .
RUN git clone https://github.com/ros-planning/moveit_tutorials.git -b master
RUN git clone https://github.com/ros-planning/panda_moveit_config.git -b melodic-devel; exit 0
RUN rosdep install -y --from-paths . --ignore-src --rosdistro noetic
WORKDIR /ws_moveit
RUN catkin config --extend /opt/ros/${ROS_DISTRO} --cmake-args -DCMAKE_BUILD_TYPE=Release
RUN catkin build

