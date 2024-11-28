import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    urdf_path = os.path.join(get_package_share_directory('depth_camera_ros2_package'), 'urdf', 'turtlebot_with_camera.urdf')
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-file', urdf_path, '-entity', 'turtlebot_camera'],
            output='screen'
        ),
        Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            name='d435_camera',
            parameters=[{
                'camera_name': 'd435',
                'enable_depth': True,
                'enable_rgb': True,
                'enable_pointcloud': True
            }]
        )
    ])
