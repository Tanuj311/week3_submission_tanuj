# week3_submission_tanuj

Python Codes are in scripts folder, msg folder is for Q3

Q 1) q1_publisher.py 

This node publishes the message "Hello World !" to the topic /new at a rate of 15 messages per second (15 Hz).
It uses the rclpy library to define a node named hello_world_publisher.
Inside the node, a timer is set up to call a callback function every 1/15 seconds.
The published message is also logged to the terminal for visibility.

q1_subscriber.py

This node subscribes to the topic /new and prints out any messages it receives.
It defines a node named hello_world_subscriber using the rclpy library.
It creates a subscriber to the /new topic. Whenever a message is received, the listener_callback() function is triggered.
The message is then logged to the terminal.

Q 2) q2_s1_publisher.py

This node simulates the signal S1 that alternates between "green" and "red" every 10 seconds.
The node is named s1_publisher. It publishes the current state ("green" or "red") on the /s1 topic once per second (1 Hz).
A counter is used to keep an eye on how many seconds have passed. After every 10 ticks, the state is toggled and published again.

q2_s2_publisher.py

This node simulates the signal S2 which behaves in opposition to signal S1.
The node is named s2_publisher.
It subscribes to the /s1 topic and listens for "green" or "red" values.
On receiving a message from /s1, it determines the opposite value ("red" if S1 is "green", and vice versa).
It publishes this opposite value on the /s2 topic.

Q 3) RoverStatus.msg

This is a custom message used to represent the status of a Mars rover. It contains the following fields:

geometry_msgs/Twist velocity: Represents both linear and angular velocities of the rover.

float64 distance_travelled: Total distance the rover has moved so far (in meters).

geometry_msgs/Pose coordinates: Current position of the rover in space.

float64 battery_power: Remaining battery percentage (e.g., 100.0 for full).

builtin_interfaces/Time time_of_travel: Total time the rover has been active or traveling.

Q 4) q4_clock_node.py

The node is named clock_node.
It publishes:
/second → second (0–59) as Int32
/minute → minute (0–59) as Int32
/hour → hour (infinite count) as Int32
/clock → complete time string in HH:MM:SS format as String
It uses a 1 Hz timer to increment time every second and handles rollover from seconds → minutes → hours.

![Screenshot 2025-07-08 230908](https://github.com/user-attachments/assets/70787daa-d04f-45da-82f1-839d75a282ad)
