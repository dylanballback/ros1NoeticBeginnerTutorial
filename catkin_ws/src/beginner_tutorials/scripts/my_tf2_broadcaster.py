import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped

rospy.init_node('my_tf2_broadcaster')

br = tf2_ros.StaticTransformBroadcaster()

t = TransformStamped()

# Fill in the transform (assuming a static transform for example)
t.header.stamp = rospy.Time.now()
t.header.frame_id = "base_link" # The frame this transform is relative to
t.child_frame_id = "imu_link" # The frame being transformed

# Fill in the transformation details (static for this example)
t.transform.translation.x = 0.0
t.transform.translation.y = 0.0
t.transform.translation.z = 0.1
t.transform.rotation.x = 0.0
t.transform.rotation.y = 0.0
t.transform.rotation.z = 0.0
t.transform.rotation.w = 1.0

# Send this transform to the system
br.sendTransform(t)

rospy.spin()
