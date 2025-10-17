# Zsákutca felismerő ROS 2 Python package

Ez a package két node-ból áll:

1. **image_generator_node** – szimulált képadatokat küld a `/zsakutca_topic` topicra.
2. **recognizer_node** – feliratkozik a topicra, és jelzi, ha zsákutcát észlel.

## Node-ok és topic-ok kapcsolata

```mermaid
graph TD
    A[/Kép_generáló node/] -->|std_msgs/String: zsákutca vagy nem_zsákutca| B[/Fel-ismerő node/]
    B -->|std_msgs/String: észlelés eredménye| C[/Terminál/]

