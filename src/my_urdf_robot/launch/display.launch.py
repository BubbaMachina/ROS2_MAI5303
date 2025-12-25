from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': open(
            '/root/ros2_ws/src/my_urdf_robot/urdf/simple_robot.urdf').read()
        }]  
        ),
Node(
package='joint_state_publisher',
executable='joint_state_publisher'
),
Node(
package='rviz2',
executable='rviz2'
),
])