import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
import copy

scale = 0.1

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface', anonymous=True)

robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group_name = "panda_arm"
group = moveit_commander.MoveGroupCommander(group_name)

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory, queue_size=20)

waypoints = []
wpose = group.get_current_pose().pose
# print(wpose)
print("===Current Pose Position===")
print("x: ", wpose.position.x)
print("y: ", wpose.position.y)
print("z: ", wpose.position.z)
print("===Current Pose Orientation===")
print("x: ", wpose.orientation.x)
print("y: ", wpose.orientation.y) 
print("z: ", wpose.orientation.z)
print("w: ", wpose.orientation.w)
wpose.position.x = 0.2246856432133212
wpose.position.y = 0.045878607857137974
wpose.position.z = 0.38869054753383253
wpose.orientation.x = 0.9984790905355542
wpose.orientation.y = -0.03282857520321604
wpose.orientation.z = 0.043722058225772846
wpose.orientation.w = 0.00708322228378105
waypoints.append(copy.deepcopy(wpose))

# wpose.position.x += scale * 0.1  # Second move forward/backwards in (x)
# waypoints.append(copy.deepcopy(wpose))

# wpose.position.y -= scale * 0.1  # Third move sideways (y)
# waypoints.append(copy.deepcopy(wpose))

# We want the Cartesian path to be interpolated at a resolution of 1 cm
# which is why we will specify 0.01 as the eef_step in Cartesian
# translation.  
# Jump threshold is critical for smooth operation! https://thomasweng.com/moveit_cartesian_jump_threshold/
(plan, fraction) = group.compute_cartesian_path(
                                   waypoints,   # waypoints to follow
                                   0.001,        # eef_step
                                   5.0)         # jump_threshold

# Note: We are just planning, not asking move_group to actually move the robot yet:
print(plan)
group.execute(plan, wait=True)
#group.stop()