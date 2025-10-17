import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/bandi/ros2_ws/src/zsakuca_recognizer/install/zsakuca_recognizer'
