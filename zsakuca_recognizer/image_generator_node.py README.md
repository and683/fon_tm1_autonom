
cd ~

mkdir -p ros2_ws/src
cd ros2_ws/src

ros2 pkg create --build-type ament_python zsakuca_recognizer
cd zsakuca_recognizer


cd zsakuca_recognizer

touch image_generator_node.py recognizer_node.py
chmod +x image_generator_node.py recognizer_node.py


cat > image_generator_node.py << EOL

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class ImageGeneratorNode(Node):
    def __init__(self):
        super().__init__('image_generator_node')
        self.publisher_ = self.create_publisher(String, 'zsakuca_topic', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        msg = String()
        if self.counter % 5 == 0:
            msg.data = "zsákuca"
        else:
            msg.data = random.choice(["zsákuca", "nem_zsákuca"])
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publikált: "{msg.data}"')
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = ImageGeneratorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
EOL

cat > recognizer_node.py << EOL

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
        if msg.data == "zsákuca":
            self.get_logger().info("Zsákuca észlelve!")
        else:
            self.get_logger().info("Nincs zsákuca.")

def main(args=None):
    rclpy.init(args=args)
    node = RecognizerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
EOL

mkdir -p ../launch
cat > ../launch/zsakuca.launch.py << EOL
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='zsakuca_recognizer',
            executable='image_generator_node',
            name='image_generator_node'
        ),
        Node(
            package='zsakuca_recognizer',
            executable='recognizer_node',
            name='recognizer_node'
        ),
    ])
EOL

mkdir -p ../diagrams
cat > ../diagrams/topics.mmd << EOL
graph TD
    A[/image_generator_node/] -->|std_msgs/String| B[/recognizer_node/]
    B -->|std_msgs/String (output)| C[/console/]
EOL


cat > ../README.md << EOL


Ez a package két node-ból áll:

1. **image_generator_node** – szimulált képadatokat küld a /zsakuca_topic topicra.
2. **recognizer_node** – feliratkozik a topicra, és jelzi, ha zsákucát észlel.



\`\`\`bash
cd ~/ros2_ws
colcon build
. install/setup.bash
ros2 launch zsakuca_recognizer zsakuca.launch.py
\`\`\`


- /zsakuca_topic : std_msgs/String, a generált objektum neve ("zsákuca" vagy "nem_zsákuca")



cd ~/ros2_ws

colcon build

. install/setup.bash

ros2 launch zsakuca_recognizer zsakuca.launch.py

