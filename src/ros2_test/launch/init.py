import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
   config = os.path.join(
      get_package_share_directory('ros2-test'),
      'config',
      'default.yaml'
      )

   return LaunchDescription([
      Node(
         package='ros2-test',
         executable='my_node',
         namespace='ros2_test',
         parameters=[config],
         output='screen'
         # output={'both': 'screen'}
      )
   ])
