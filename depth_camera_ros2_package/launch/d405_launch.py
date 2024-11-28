import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            name='d405_camera',
            output='screen',
            parameters=[{
                'camera_name': 'd405',
                'enable_depth': True,
                'enable_rgb': True,
                'enable_pointcloud': True
            }]
        )
    ])
