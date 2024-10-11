# Filename: ping360_launch.py

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ping360_sonar',
            executable='ping360_node',
            name='ping360',
            output='screen',
            parameters=[
                {'gain': 0},
                {'frequency': 740},
                {'range_max': 2},
                {'angle_sector': 360},
                {'angle_step': 1},
                {'image_size': 300},
                {'scan_threshold': 200},
                {'speed_of_sound': 1500},
                {'image_rate': 100},
                {'sonar_timeout': 8000},
                {'publish_image': True},
                {'publish_scan': True},
                {'publish_echo': True},
                {'frame': 'sonar'},
                {'device': '/dev/ttyUSB0'},
                {'baudrate': 115200},
                {'fallback_emulated': True},
                {'connection_type': 'serial'},
                {'udp_address': '0.0.0.0'},
                {'udp_port': 12345}
            ]
        )
    ])