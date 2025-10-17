# Zsákutca felismerő ROS 2 Python package

Ez a package két node-ból áll:

1. **image_generator_node** – szimulált képadatokat küld a `/zsakutca_topic` topicra.
2. **recognizer_node** – feliratkozik a topicra, és jelzi, ha zsákutcát észlel.

## Node-ok és topic-ok kapcsolata

```mermaid
graph TD
    A[/Kép_generáló node/] -->|std_msgs/String: zsákutca vagy nem_zsákutca| B[/Fel-ismerő node/]
    B -->|std_msgs/String: észlelés eredménye| C[/Terminál/]

## Clone the package

Ha szeretnéd letölteni a package-ot a saját gépedre:

```bash
cd ~/ros2_ws/src
git clone https://github.com/and683/fon_tm1_autonom.git
cd fon_tm1_autonom

