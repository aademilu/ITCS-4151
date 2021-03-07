   1 #!/usr/bin/env python  
   2 import rospy
   3 
   4 # Because of transformations
   5 import tf_conversions
   6 
   7 import tf2_ros
   8 import geometry_msgs.msg
   9 import turtlesim.msg
  10 
  11 
  12 def handle_turtle_pose(msg, turtlename):
  13     br = tf2_ros.TransformBroadcaster()
  14     t = geometry_msgs.msg.TransformStamped()
  15 
  16     t.header.stamp = rospy.Time.now()
  17     t.header.frame_id = "world"
  18     t.child_frame_id = turtlename
  19     t.transform.translation.x = msg.x
  20     t.transform.translation.y = msg.y
  21     t.transform.translation.z = 0.0
  22     q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
  23     t.transform.rotation.x = q[0]
  24     t.transform.rotation.y = q[1]
  25     t.transform.rotation.z = q[2]
  26     t.transform.rotation.w = q[3]
  27 
  28     br.sendTransform(t)
  29 
  30 if __name__ == '__main__':
  31     rospy.init_node('tf2_turtle_broadcaster')
  32     turtlename = rospy.get_param('~turtle')
  33     rospy.Subscriber('/%s/pose' % turtlename,
  34                      turtlesim.msg.Pose,
  35                      handle_turtle_pose,
  36                      turtlename)
  37     rospy.spin()