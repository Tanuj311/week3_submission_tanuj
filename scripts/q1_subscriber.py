#!/usr/bin/env python3

# Import required ROS 2 Python libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String  

# Define a custom subscriber class that inherits from Node
class HelloWorldSubscriber(Node):
    def __init__(self):
        # Initialize the node with the name 'hello_world_subscriber'
        super().__init__('hello_world_subscriber')

        # Create a subscription to the '/new' topic
        self.subscription = self.create_subscription(
            String,
            '/new',
            self.listener_callback,
            10
        )

    # Callback function that gets executed every time a message is received on the '/new' topic
    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)  

    # Create node
    node = HelloWorldSubscriber()  

    # Use node
    rclpy.spin(node)  

    # Destroy node
    node.destroy_node()  
    rclpy.shutdown() 

if __name__ == '__main__':
    main()
