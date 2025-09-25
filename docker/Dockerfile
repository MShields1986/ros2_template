ARG ROS_DISTRO=jazzy

FROM ros:$ROS_DISTRO-ros-base

# Switch to cyclonedds
RUN apt update && apt install ros-$ROS_DISTRO-rmw-cyclonedds-cpp -y
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ENV CYCLONEDDS_URI="<CycloneDDS><Domain><General><AllowMulticast>true</AllowMulticast><Interfaces><NetworkInterface address='10.1.1.0' /></Interfaces></General></Domain></CycloneDDS>"

# Increase buffer size as recommended by rmw_cyclonedds_cpp
RUN echo 'net.core.rmem_max=2147483647' >> /etc/sysctl.conf \
 && echo 'net.core.rmem_default=8388608' >> /etc/sysctl.conf

SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive

# Your deps go here
RUN apt-get update #\
# && sudo apt-get install -y \
# libzmq3-dev \
# libboost-dev \
# ros-$ROS_DISTRO-behaviortree-cpp-v3

COPY ../src /ros2_ws/src

WORKDIR /ros2_ws

RUN source /opt/ros/$ROS_DISTRO/setup.bash \
 && rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y \
 && colcon build \
 && echo 'source /opt/ros/$ROS_DISTRO/setup.bash' >> /root/.bashrc \
 && echo 'source /ros2_ws/install/setup.bash' >> /root/.bashrc \
 && echo 'source /ros2_ws/install/setup.bash' >> /ros_entrypoint.sh

RUN sed -i '/exec "$@"/d' /ros_entrypoint.sh \
 && echo 'exec "$@"' >> /ros_entrypoint.sh

ENTRYPOINT [ "/ros_entrypoint.sh" ]

ENV DEBIAN_FRONTEND=dialog
