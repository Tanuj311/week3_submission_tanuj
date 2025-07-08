#!/usr/bin/env python3

# Import required ROS 2 Python libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Define a custom Publisher class that inherits from Node
class Publisher(Node):
    def __init__(self):
        # Initialize the node with the name 'hello_world_publisher'
        super().__init__('hello_world_publisher')

        # Create a publisher that will publish messages of type String on topic '/new'
        self.publisher_ = self.create_publisher(String, '/new', 10)

        timer_period = 1 / 15  # seconds

        self.timer = self.create_timer(timer_period, self.timer_callback)  

    # This callback function is called at a 15 Hz rate
    def timer_callback(self):
        msg = String()  
        msg.data = 'Hello World !' 
        self.publisher_.publish(msg)  # Publish the message
        self.get_logger().info(f'Publishing: "{msg.data}"')  # Log the published message


def main(args=None):
    rclpy.init(args=args) 

    # Create node
    node = Publisher()

    # Use node 
    rclpy.spin(node) 

    # Destroy node
    node.destroy_node()  
    rclpy.shutdown()  

if __name__ == '__main__':
    main()
