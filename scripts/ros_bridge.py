########### NOTICE ###########
# pose handling is not yet implemented on the receiving side!

### ros_bridge.py
# Bouncer to break out incoming joint/pose data for MoveIt
# Input: ROS network joint angles or desired poses
# Output: actionable data for MoveIt!

import rospy
import moveit_commander
import sys
from std_msgs.msg import Float64MultiArray

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface', anonymous=True)

robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()
# scene.add_mesh("OBSTACLES", pose, "./planning_scene.scene")

group_name = "panda_arm"
group = moveit_commander.MoveGroupCommander(group_name)
group.set_max_velocity_scaling_factor(0.05)
group.set_max_acceleration_scaling_factor(0.05)


########### OBJ AVOIDANCE ###########
import geometry_msgs
box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = "panda_link0"
box_pose.pose.orientation.w = 1.0
box_pose.pose.position.z = -0.2 #-0.43
box_name = "box"
scene.add_box(box_name, box_pose, size=(5, 5, 1))
########### OBJ AVOIDANCE ###########


def listener():
	rospy.Subscriber("/bridge/joint_angles", Float64MultiArray, joint_angles)
	rospy.spin()

def joint_angles(joint_goals):
	print("MESSAGE!")
	group.go(joint_goals.data, wait=True)
	group.stop()

if __name__ == '__main__':
    listener()