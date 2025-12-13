from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_path = get_package_share_directory('arm1_description')
    xacro_file = os.path.join(pkg_path, 'urdf', 'arm1.xacro')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': open(xacro_file).read()
            }]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=[]
        )
    ])
