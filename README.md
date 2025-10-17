# Zsákuca felismerő ROS 2 Python package

Ez a package két node-ból áll:

1. **image_generator_node** – szimulált képadatokat küld a `/zsakuca_topic` topicra.
2. **recognizer_node** – feliratkozik a topicra, és jelzi, ha zsákucát észlel.

## Build és futtatás

```bash
cd ~/ros2_ws
colcon build
. install/setup.bash
ros2 launch zsakuca_recognizer zsakuca.launch.py

