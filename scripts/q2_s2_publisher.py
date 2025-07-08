#!/usr/bin/env python3

# Import required ROS 2 Python libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class S2Publisher(Node):
    def __init__(self):
        # Initialize the node with name 's2_publisher'
        super().__init__('s2_publisher')

        # Create a subscription to the /s1 topic
        self.subscription = self.create_subscription(
            String, 
            '/s1', 
            self.s1_callback, 
            10
        )

        # Create a publisher on the /s2 topic to publish the opposite signal
        self.publisher_ = self.create_publisher(String, '/s2', 10)

    # Callback function triggered when a new message is received on /s1
    def s1_callback(self, msg):
        s1_state = msg.data

        # Determine S2 state as the opposite of S1
        s2_state = 'red' if s1_state == 'green' else 'green'

        response = String()
        response.data = s2_state
        self.publisher_.publish(response)

        self.get_logger().info(f'S1 state = {s1_state} | Publishing S2 = {s2_state}')

def main(args=None):
    rclpy.init(args=args)  

    # Create node          
    node = S2Publisher()    

    # Use node         
    rclpy.spin(node)     

    # Destroy node           
    node.destroy_node()            
    rclpy.shutdown()               

if __name__ == '__main__':
    main()
