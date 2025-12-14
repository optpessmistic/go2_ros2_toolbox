import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()
    
    # 1. 设置 use_sim_time (必须为 true)
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    # ========================================================================
    # ➕ 新增：TF 桥接修复
    # 作用：将仿真器的 'unitree_go2/base_link' 映射为标准的 'base_link'
    # 参数：x y z yaw pitch roll frame_id child_frame_id
    # ========================================================================
    tf_bridge_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='sim_to_real_base_link',
        # 意思是：base_link 紧紧贴在 unitree_go2/base_link 上，不做位移和旋转
        arguments=['0', '0', '0', '0', '0', '0', 'unitree_go2/base_link', 'base_link'],
        parameters=[{'use_sim_time': use_sim_time}]
    )

    # 2. 感知模块
    pointcloud_to_laserscan_node = Node(
        package='go2_perception', 
        executable='pointcloud_to_laserscan_node',
        name='pointcloud_to_laserscan_node',
        remappings=[
            ('cloud_in', '/unitree_go2/lidar/point_cloud'), 
            ('scan', '/scan')
        ],
        parameters=[{
            'target_frame': 'base_link', # 现在这个 frame 终于存在了！
            'transform_tolerance': 0.05, #稍微放宽一点容差
            'min_height': -0.1,
            'max_height': 0.5,
            'angle_min': -3.14,
            'angle_max': 3.14,
            'angle_increment': 0.0087,
            'scan_time': 0.1,
            'range_min': 0.15,
            'range_max': 12.0,
            'use_inf': True,
            'use_sim_time': use_sim_time
        }]
    )

    # 3. 引入 SLAM 或 Nav2 (保持原样，按需开启)
    # slam_launch = ... 
    # nav2_launch = ...

    # 添加节点到启动描述
    ld.add_action(tf_bridge_node)           # <--- 别忘了加这个
    ld.add_action(pointcloud_to_laserscan_node)
    
    return ld