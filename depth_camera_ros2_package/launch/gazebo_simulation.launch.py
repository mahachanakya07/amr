import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    urdf_file = os.path.join(get_package_share_directory('simulated_depth_camera_package'), 'urdf', 'turtlebot_with_simulated_camera.urdf')
    world_file = os.path.join(get_package_share_directory('simulated_depth_camera_package'), 'worlds', 'simulated_environment.world')

    return LaunchDescription([
        # Launch Gazebo
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_file, '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        # Spawn the TurtleBot with the simulated depth camera
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-file', urdf_file, '-entity', 'turtlebot_camera'],
            output='screen'
        )
    ])
