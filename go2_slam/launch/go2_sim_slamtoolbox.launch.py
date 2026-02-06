from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get slam_toolbox package path
    slam_toolbox_dir = get_package_share_directory('slam_toolbox')
    
    # Set configuration file path
    slam_toolbox_config = os.path.join(
        get_package_share_directory('go2_slam'),
        'config',
        'mapper_params_sim_online_async.yaml'
    )

    # Include slam_toolbox launch file
    slam_toolbox_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(slam_toolbox_dir, 'launch', 'online_async_launch.py')
        ]),
        launch_arguments={
            'slam_params_file': slam_toolbox_config,
            'use_sim_time': 'false',
            'remappings': str([
                ('/odom', '/unitree_go2/odom')
            ])
        }.items(),
    )

    return LaunchDescription([
        slam_toolbox_launch
    ])