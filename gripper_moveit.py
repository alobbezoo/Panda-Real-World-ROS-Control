import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface', anonymous=True)

robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group_name = "panda_arm"
group = moveit_commander.MoveGroupCommander(group_name)

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory, queue_size=20)

# To print the reference frame of robot:
planning_frame = group.get_planning_frame()
print(planning_frame)
# To print the name of the end-effector link for this group:
eef_link = group.get_end_effector_link()
print(eef_link)
# To print a list of all the groups in the robot:
group_names = robot.get_group_names()
print(group_names)
# To print the entire state of the robot:
robot_state = robot.get_current_state()
print(robot_state)


group_name = "hand"
group = moveit_commander.MoveGroupCommander(group_name)

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

joint_goal = group.get_current_joint_values()
joint_goal[0] = 0.01
joint_goal[1] = 0.01
group.go(joint_goal, wait=True)
group.stop()

# joint_goal = group.get_current_joint_values()
# joint_goal[0] = 0.00
# joint_goal[1] = 0.00
# group.go(joint_goal, wait=True)
# group.stop()

