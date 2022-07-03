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

# To print the entire state of the robot:
robot_state = robot.get_current_state()
print(robot_state.joint_state.position)

group_name = "panda_arm"
group = moveit_commander.MoveGroupCommander(group_name)

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

joint_goal = group.get_current_joint_values()
print(joint_goal)
joint_goal = [-0.025697618025375523, 0.5220417501237169, -0.012493641642623897, -1.714366414478602, 0.009140908660269011, 2.2919725014255365, 2.2919725014255365]
group.go(joint_goal, wait=True)
group.stop()
joint_goal = [-0.08405481132257214, 0.5538246195862154, -0.03498251927096905, -1.7791462683755064, 0.015545781595959894, 2.1795890358162526, 2.1795890358162526]
group.go(joint_goal, wait=True)
group.stop()
joint_goal = [-0.12835519518063943, 0.6058810295675315, -0.041550745547381376, -1.7524370420085478, 0.026069160695111223, 2.2180609600513335, 2.2180609600513335]
group.go(joint_goal, wait=True)
group.stop()
joint_goal = [-0.17905011266739054, 0.6054458516943241, -0.04573970148656565, -1.865250368331465, 0.045364414514851605, 2.5118268340776297, 2.5118268340776297]
group.go(joint_goal, wait=True)
group.stop()
joint_goal = [-0.2406028780627805, 0.7597519481653286, -0.05088270600611002, -1.7637332761466993, 0.05537031606356738, 2.4706780990615105, 2.4706780990615105]
group.go(joint_goal, wait=True)
group.stop()


# joint_goal = group.get_current_joint_values()
# joint_goal[0] = 0.00
# joint_goal[1] = 0.00
# group.go(joint_goal, wait=True)
# group.stop()