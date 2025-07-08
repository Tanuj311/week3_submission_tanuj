#!/usr/bin/env python3

# Import required ROS 2 Python libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class ClockNode(Node):
    def __init__(self):
        super().__init__('clock_node')
        
        # Publishers
        self.sec_pub = self.create_publisher(Int32, '/second', 10)
        self.min_pub = self.create_publisher(Int32, '/minute', 10)
        self.hour_pub = self.create_publisher(Int32, '/hour', 10)
        self.clock_pub = self.create_publisher(String, '/clock', 10)
        
        # Time counters
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        
        # Timer (1 second interval)
        self.timer = self.create_timer(1.0, self.timer_callback) # 1 Hz
        self.get_logger().info("Clock system started")

    def timer_callback(self):
        # Increment seconds
        self.seconds += 1
        
        # Publish seconds
        sec_msg = Int32()
        sec_msg.data = self.seconds
        self.sec_pub.publish(sec_msg)
        
        # Handle minute rollover
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
            
            # Publish minutes
            min_msg = Int32()
            min_msg.data = self.minutes
            self.min_pub.publish(min_msg)
            
            # Handling hour
            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1
                
                # Publish hours
                hour_msg = Int32()
                hour_msg.data = self.hours
                self.hour_pub.publish(hour_msg)
        
        # Format and publish time
        time_str = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        clock_msg = String()
        clock_msg.data = time_str
        self.clock_pub.publish(clock_msg)
        
        self.get_logger().info(f"Published time: {time_str}")

def main(args=None):
    rclpy.init(args=args)

    # Create node 
    node = ClockNode()

    # Use node 
    rclpy.spin(node)

    # Destroy node
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
