#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from geometry_msgs.msg import Twist
from turtlesim.action import RotateAbsolute


class CircleDriver(Node):

    def __init__(self):
        super().__init__('circle_driver')

        self.cmd_vel_pub = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10
        )

        self.rotate_client = ActionClient(
            self, RotateAbsolute, '/turtle1/rotate_absolute'
        )

        self.rotate_client.wait_for_server()
        self.rotate_to_center()

    def rotate_to_center(self):
        self.get_logger().info("Rotating turtle to 0 radians")

        goal = RotateAbsolute.Goal()
        goal.theta = 0.0

        send_goal = self.rotate_client.send_goal_async(goal)
        send_goal.add_done_callback(self.start_circle)

    def start_circle(self, future):
        self.get_logger().info("Starting circular motion")

        self.timer = self.create_timer(0.1, self.publish_circle)

    def publish_circle(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub.publish(msg)


def main():
    rclpy.init()
    node = CircleDriver()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
