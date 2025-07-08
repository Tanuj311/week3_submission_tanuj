#!/usr/bin/env python3

# Import required ROS 2 Python libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Define a publisher node that switches between "green" and "red" every 10 seconds
class S1Publisher(Node):
    def __init__(self):
        super().__init__('s1_publisher')
        self.publisher_ = self.create_publisher(String, '/s1', 10)

        # Initial state is green
        self.state = 'green'

        self.counter = 0
        self.timer = self.create_timer(1.0 , self.timer_callback) # 1 Hz

    # Timer callback that toggles state and publishes the message
    def timer_callback(self):
        # Switch after 10 seconds (since frequency is 1 Hz)
        if self.counter >= 10: 
            self.state = 'red' if self.state == 'green' else 'green'
            self.counter = 0

        # Create and publish the message
        msg = String()
        msg.data = self.state
        self.publisher_.publish(msg)

        # Log the published state
        self.get_logger().info(f'S1 publishes: {msg.data}')
        self.counter +=1

def main(args=None):
    rclpy.init(args=args)

    # Create node
    node = S1Publisher()

    # Use node
    rclpy.spin(node)

    # Destroy node
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
