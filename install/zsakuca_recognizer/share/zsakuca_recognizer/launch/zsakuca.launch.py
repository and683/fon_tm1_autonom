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
