#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class ImageGeneratorNode(Node):
    def __init__(self):
        super().__init__('image_generator_node')
        self.publisher_ = self.create_publisher(String, 'zsakutca_topic', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        msg = String()
        if self.counter % 5 == 0:
            msg.data = "zsákutca"
        else:
            msg.data = random.choice(["zsákutca", "nem_zsákutca"])
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publikált: "{msg.data}"')
        self.counter += 1

def main(args=None):
    import rclpy
    from rclpy.node import Node

    rclpy.init(args=args)
    node = ImageGeneratorNode() 
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
