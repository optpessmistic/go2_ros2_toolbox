from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        #Node(
        #    package='go2_perception', executable='cloud_accumulation',
        #    remappings=[
        #        ('/utlidar/cloud_deskewed', '/unitree_go2/lidar/point_cloud'),
        #        ('cloud', '/trans_cloud')
        #        ],
        #    name='cloud_accumulation'
        #),
        Node(
            package='go2_perception', executable='pointcloud_to_laserscan_node',
            remappings=[
                ('cloud_in', '/unitree_go2/lidar/point_cloud'), 
                ('scan', '/scan'),
                ('/utlidar/robot_pose', '/unitree_go2/pose')
                ],
            parameters=[{
                'use_sim_time': False,
                'target_frame': 'base_link',
                'transform_tolerance': 0.01,
                'min_height': -0.1,
                'max_height': 1.0,
                'angle_min': -3.14,  # -M_PI/2
                'angle_max': 3.14,  # M_PI/2
                'angle_increment': 0.0087,  # M_PI/360.0
                'scan_time': 0.25,
                'range_min': 0.10,
                'range_max': 20.0,
                'use_inf': True,
                'inf_epsilon': 1.0
            }],
            name='pointcloud_to_laserscan_node'
        )
    ])
