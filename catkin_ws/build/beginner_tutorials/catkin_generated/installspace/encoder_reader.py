#!/usr/bin/env python3

import rospy
import serial
from std_msgs.msg import Float32

# Initialize ROS node
rospy.init_node('encoder_reader')

# Create a publisher
pub = rospy.Publisher('encoder_angle', Float32, queue_size=10)

# Setup serial connection
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

def read_from_serial():
    while not rospy.is_shutdown():
        try:
            # Read a line from the serial port and strip off the newline character
            line = ser.readline().rstrip()
            
            # Convert the line from a string to a float
            angle = float(line)
            
            # Publish the angle
            pub.publish(angle)
            
        except ValueError:
            # Handles the case where the float conversion fails
            rospy.loginfo("Received a non-float value")
        except rospy.ROSInterruptException:
            # Allows the node to be cleanly stopped
            break

if __name__ == '__main__':
    try:
        read_from_serial()
    except rospy.ROSInterruptException:
        pass
    finally:
        ser.close()
