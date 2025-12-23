from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node


def generate_launch_description():

    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim',
        parameters=[{
            'background_r': 180,
            'background_g': 220,
            'background_b': 255
        }]
    )

    rosbag_record = ExecuteProcess(
        cmd=[
            'ros2', 'bag', 'record',
            '/turtle1/cmd_vel',
            '/turtle1/pose',
            '/parameter_events',
            '/turtle1/rotate_absolute/_action/status'
        ],
        output='screen'
    )

    setup_node = Node(
        package='turtle_circle',
        executable='setup_node',
        name='setup_node'
    )

    circle_driver = Node(
        package='turtle_circle',
        executable='circle_driver',
        name='circle_driver'
    )

    return LaunchDescription([
        turtlesim_node,

        # give turtlesim time to start
        TimerAction(period=2.0, actions=[setup_node]),

        # start motion after setup completes
        TimerAction(period=4.0, actions=[circle_driver]),

        # start recording
        TimerAction(period=1.0, actions=[rosbag_record])
    ])
