#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RecognizerNode(Node):
    def __init__(self):
        super().__init__('recognizer_node')
        self.subscription = self.create_subscription(
            String,
            'zsakuca_topic',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        if msg.data == "zsákutca":
            self.get_logger().info("Zsákutca észlelve!")
        else:
            self.get_logger().info("Nincs zsákutca.")

def main(args=None):
    rclpy.init(args=args)
    node = RecognizerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
