"""
This node would read raw imu data. 
"""

#!/usr/bin/env python
import rospy
import serial
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion, Vector3

# Open the serial port
ser = serial.Serial('/dev/ttyACM0', 115200) # Adjust as necessary

def talker():
    pub = rospy.Publisher('imu_data', Imu, queue_size=10)
    rospy.init_node('imu_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        if ser.in_waiting:
            line = ser.readline().decode('utf-8').rstrip()
            parts = line.split(',')

            if parts[0] == "IMU" and len(parts) == 7:
                imu_msg = Imu()
                imu_msg.header.stamp = rospy.Time.now()
                imu_msg.header.frame_id = "imu_frame"
                
                # accelerometer data
                imu_msg.linear_acceleration = Vector3(float(parts[1]), float(parts[2]), float(parts[3]))
                # gyroscope data
                imu_msg.angular_velocity = Vector3(float(parts[4]), float(parts[5]), float(parts[6]))
                # publish the IMU data
                pub.publish(imu_msg)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
