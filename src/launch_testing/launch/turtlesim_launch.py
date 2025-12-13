from launch import LaunchDescription 
from launch_ros.actions import Node 

# def generate_launch_description(): 
#     return LaunchDescription([ 
#         Node(
#             package='turtlesim', 
#              executable='turtlesim_node'
#              ), 
#         Node(
#             package='turtlesim', 
#              executable='turtle_teleop_key',
#              output='screen',
#              emulate_tty=True
#              ), 
#     ])
    
def generate_launch_description(): 
    return LaunchDescription([ 
        Node(
            package='turtlesim', 
             namespace='turtlesim1',
             executable='turtlesim_node'
             ), 
        Node(
            package='turtlesim', 
             namespace='turtlesim2',
             executable='turtlesim_node'
             ), 
        Node(
            package='turtlesim', 
             executable='mimic',
             remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ]
             ), 
    ])