cmake_minimum_required(VERSION 3.8)
project(ros2-test)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

##########################
# Find Dependencies
##########################
set(
  THIS_PACKAGE_DEPS
    ament_cmake
    rclcpp
    rclcpp_action
    rclcpp_components
    tf2
    tf2_ros
    std_srvs
    geometry_msgs
    trajectory_msgs
    ament_index_cpp
  )

foreach(PACKAGE ${THIS_PACKAGE_DEPS})
  find_package(${PACKAGE} REQUIRED)
endforeach()

##########################
# Compilation
##########################
include_directories(
  include
)

set(
  NODES_SRC
    src/my_lib.cpp
  )

add_library(ros2-test_lib SHARED ${NODES_SRC})
target_include_directories(ros2-test_lib PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)
ament_target_dependencies(ros2-test_lib ${THIS_PACKAGE_DEPS})


add_executable(my_node src/my_node.cpp)
target_link_libraries(my_node ros2-test_lib)
ament_target_dependencies(my_node ${THIS_PACKAGE_DEPS})

target_include_directories(my_node
  PUBLIC
    "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
    "$<INSTALL_INTERFACE:include>")

target_compile_features(my_node PUBLIC c_std_99 cxx_std_17)


##########################
# Installation
##########################

install(
  DIRECTORY
    config
    launch
  DESTINATION share/${PROJECT_NAME}
  )

install(
  TARGETS ros2-test_lib
  DESTINATION lib
)

install(TARGETS my_node
  DESTINATION lib/${PROJECT_NAME}
  )

#install(
#  DIRECTORY include/${PROJECT_NAME}/
#  DESTINATION include/${PROJECT_NAME}/
#  )

#ament_export_include_directories(include)

##########################
# Tests
##########################

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
