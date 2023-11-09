"""
This ros node would read imu roll, pitch, and yaw data from an IMU on an arduino.

"""


#!/usr/bin/env python
import rospy
import serial
import math
import tf
from sensor_msgs.msg import Imu

# Open the serial port
ser = serial.Serial('/dev/ttyACM0', 115200)  # Adjust as necessary

def talker():
    pub = rospy.Publisher('imu_data', Imu, queue_size=10)
    rospy.init_node('imu_talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        if ser.in_waiting:
            line = ser.readline().decode('utf-8').rstrip()
            parts = line.split(',')

            if parts[0] == "IMU" and len(parts) == 4:  # Ensure we have exactly 4 parts
                imu_msg = Imu()
                imu_msg.header.stamp = rospy.Time.now()
                imu_msg.header.frame_id = "imu_link"  # Change to your frame

                # Roll, pitch, and yaw (in degrees) from the serial port
                roll = math.radians(float(parts[1]))  # Convert to radians
                pitch = math.radians(float(parts[2]))
                yaw = math.radians(float(parts[3]))

                # Convert roll, pitch, yaw to quaternion
                quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)

                # Set the orientation of the IMU message to the quaternion
                imu_msg.orientation.x = quaternion[0]
                imu_msg.orientation.y = quaternion[1]
                imu_msg.orientation.z = quaternion[2]
                imu_msg.orientation.w = quaternion[3]

                # Since we don't have linear acceleration or angular velocity, we'll leave those out.
                # They can be added here if your IMU provides them.

                # Publish the IMU data
                pub.publish(imu_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
