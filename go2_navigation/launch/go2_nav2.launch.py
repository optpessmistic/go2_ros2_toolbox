from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, SetRemap
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()

    # 1. 获取各个包的路径
    go2_nav_dir = get_package_share_directory('go2_navigation')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    nav2_bt_navigator_dir = get_package_share_directory('nav2_bt_navigator')

    # 2. 设置配置文件路径
    nav2_config = os.path.join(go2_nav_dir, 'config', 'nav2_params.yaml')

    # 3. 获取默认的行为树 XML 绝对路径 (关键修复)
    # 这解决了 bt_navigator 找不到文件而崩溃的问题
    default_bt_xml_path = os.path.join(
        nav2_bt_navigator_dir,
        'behavior_trees',
        'navigate_w_replanning_and_recovery.xml'
    )

    # 4. 包含 nav2 launch
    nav2_launch_group = GroupAction([
        # 设置重映射
        SetRemap(src='/cmd_vel', dst='/unitree_go2/cmd_vel'),
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                os.path.join(nav2_bringup_dir, 'launch', 'navigation_launch.py')
            ]),
            launch_arguments={
                'params_file': nav2_config,
                'use_sim_time': 'false',
                'default_bt_xml_filename': default_bt_xml_path, # 显式传递绝对路径
            }.items(),
        )
    ])

    ld.add_action(nav2_launch_group)

    return ld