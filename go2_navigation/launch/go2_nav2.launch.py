from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Create LaunchDescription object
    ld = LaunchDescription()

    # Set configuration file path
    nav2_config = os.path.join(
        get_package_share_directory('go2_navigation'),
        'config',
        'nav2_params.yaml'
    )

    # Include nav2 launch file
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(
                'nav2_bringup'), 'launch', 'navigation_launch.py')
        ]),
        launch_arguments={
            'params_file': nav2_config,
            'use_sim_time': 'false',
        }.items(),
    )

    # Add launch action
    ld.add_action(nav2_launch)

    return ld