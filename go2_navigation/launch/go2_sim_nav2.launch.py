from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, SetRemap
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()

    # 1. Get paths of each package
    go2_nav_dir = get_package_share_directory('go2_navigation')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    nav2_bt_navigator_dir = get_package_share_directory('nav2_bt_navigator')

    # 2. Set configuration file path
    nav2_config = os.path.join(go2_nav_dir, 'config', 'nav2_sim_params.yaml')

    # 3. Get absolute path of default behavior tree XML (critical fix)
    # This solves the problem of bt_navigator crashing when file is not found
    default_bt_xml_path = os.path.join(
        nav2_bt_navigator_dir,
        'behavior_trees',
        'navigate_w_replanning_and_recovery.xml'
    )

    # 4. Include nav2 launch
    nav2_launch_group = GroupAction([
        # Set remapping
        SetRemap(src='/cmd_vel', dst='/unitree_go2/cmd_vel'),
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                os.path.join(nav2_bringup_dir, 'launch', 'navigation_launch.py')
            ]),
            launch_arguments={
                'params_file': nav2_config,
                'use_sim_time': 'false',
                'default_bt_xml_filename': default_bt_xml_path, # Explicitly pass absolute path
            }.items(),
        )
    ])

    ld.add_action(nav2_launch_group)

    return ld