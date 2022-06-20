import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi


try:
    from math import pi, tau, dist, fabs, cos
except:  # For Python 2 compatibility
    from math import pi, fabs, cos, sqrt

    tau = 2.0 * pi

    def dist(p, q):
        return sqrt(sum((p_i - q_i) ** 2.0 for p_i, q_i in zip(p, q)))

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface', anonymous=True)

robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group_name = "panda_arm"
group = moveit_commander.MoveGroupCommander(group_name)

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory, queue_size=20)

# To print the reference frame of robot:
planning_frame = group.get_planning_frame()
print("\n\n", planning_frame)
# To print the name of the end-effector link for this group:
eef_link = group.get_end_effector_link()
print(eef_link)
# To print a list of all the groups in the robot:
group_names = robot.get_group_names()
print(group_names)
# To print the entire state of the robot:
robot_state = robot.get_current_state()
print(robot_state, "\n \n")


# group_name = "panda_arm"
# move_group = moveit_commander.MoveGroupCommander(group_name)

joint_goal = group.get_current_joint_values()
print("\n \n joint goal is: ", joint_goal, "\n \n")
# joint_goal[0] = 0
# joint_goal[1] = 0
# joint_goal[2] = 0
# joint_goal[3] = -tau/4
# joint_goal[4] = 0
# joint_goal[5] = tau/4
# joint_goal[6] = tau/8

# joint_goal[0] = 0
# joint_goal[1] = 0
# joint_goal[2] = 0
# joint_goal[3] = -tau/2
# joint_goal[4] = 0
# joint_goal[5] = tau/2
# joint_goal[6] = tau/4

joint_goal[0] = 0
joint_goal[1] = -pi/4
joint_goal[2] = 0
joint_goal[3] = -pi/2
joint_goal[4] = 0
joint_goal[5] = pi/3
joint_goal[6] = 0

group.go(joint_goal, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
group.stop()

# for i in range(10):
#     joint_goal[0] += 0.05
#     joint_goal[1] += 0.05
#     joint_goal[2] += 0.05
#     joint_goal[3] += 0.05
#     joint_goal[4] += 0.05
#     joint_goal[5] += 0.05
#     joint_goal[6] += 0.05
#     move_group.go(joint_goal, wait=False)
#     move_group.stop()

# pose_goal = geometry_msgs.msg.Pose()
# pose_goal.orientation.w = 0.5
# pose_goal.position.x = 0.4
# pose_goal.position.y = 0.1
# pose_goal.position.z = 0.4
# group.set_pose_target(pose_goal)
# plan = group.go(wait=True)
# group.stop()
# group.clear_pose_targets() # clear targets after planning


# group_name = "hand"
# group = moveit_commander.MoveGroupCommander(group_name)

# display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

# joint_goal = group.get_current_joint_values()
# joint_goal[0] = 0.03
# joint_goal[1] = 0.03
# group.go(joint_goal, wait=True)
# group.stop()

# joint_goal = group.get_current_joint_values()
# joint_goal[0] = 0.00
# joint_goal[1] = 0.00
# group.go(joint_goal, wait=True)
# group.stop()
