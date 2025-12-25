from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    urdf = os.path.join(
        get_package_share_directory('rrobot_description'),
        'urdf',
        'rrbot.urdf'
    )

    return LaunchDescription([
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': open(urdf).read()}]
        ),
        Node(
            package='rviz2',
            executable='rviz2'
        )
    ])
