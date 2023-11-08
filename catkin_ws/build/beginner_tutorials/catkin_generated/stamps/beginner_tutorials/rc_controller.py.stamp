#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Joy

# This is the callback function that gets called
# when a new message is received on the /joy topic
def joy_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.axes)

def listener():
    # Initialize the node
    rospy.init_node('joy_listener', anonymous=True)

    # Subscribe to the /joy topic with the callback function 'joy_callback'
    rospy.Subscriber("/joy", Joy, joy_callback)

    # spin() keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
