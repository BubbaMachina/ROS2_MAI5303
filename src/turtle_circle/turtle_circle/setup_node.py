#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_srvs.srv import Empty
from turtlesim.srv import SetPen


class SetupNode(Node):

    def __init__(self):
        super().__init__('setup_node')

        self.reset_client = self.create_client(Empty, '/reset')
        self.clear_client = self.create_client(Empty, '/clear')
        self.pen_client = self.create_client(SetPen, '/turtle1/set_pen')

        self.wait_for_services()
        self.run_setup()

    def wait_for_services(self):
        self.get_logger().info("Waiting for setup services...")
        self.reset_client.wait_for_service()
        self.clear_client.wait_for_service()
        self.pen_client.wait_for_service()

    def run_setup(self):
        self.get_logger().info("Resetting turtle")
        self.reset_client.call_async(Empty.Request())

        self.get_logger().info("Clearing screen")
        self.clear_client.call_async(Empty.Request())

        self.get_logger().info("Setting pen")
        pen_req = SetPen.Request()
        pen_req.r = 0
        pen_req.g = 120
        pen_req.b = 255
        pen_req.width = 3
        pen_req.off = 0
        self.pen_client.call_async(pen_req)

        self.get_logger().info("Setup complete, exiting.")


def main():
    rclpy.init()
    node = SetupNode()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
