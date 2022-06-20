import sys
import rospy
# import moveit_commander
# import moveit_msgs.msg
# import geometry_msgs.msg

# moveit_commander.roscpp_initialize(sys.argv)
# rospy.init_node('move_group_python_interface', anonymous=True)

# robot = moveit_commander.RobotCommander()

# scene = moveit_commander.PlanningSceneInterface()

# group_name = "hand"
# group = moveit_commander.MoveGroupCommander(group_name)

# display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

# joint_goal = group.get_current_joint_values()
# joint_goal[0] = 0.03
# joint_goal[1] = 0.03
# group.go(joint_goal, wait=True)
# group.stop()

# joint_goal = group.get_current_joint_values()
# joint_goal[0] = 0.017
# joint_goal[1] = 0.017
# group.go(joint_goal, wait=True)
# group.stop()


from franka_gripper.msg import MoveGoal, MoveAction, GraspAction, GraspGoal
import actionlib

# if __name__ == '__main__':
#     rospy.init_node('Franka_gripper_move_action')
#     client = actionlib.SimpleActionClient('/franka_gripper/move', MoveAction)
#     client.wait_for_server()
#     goal = MoveGoal(width = 0.04, speed = 0.05)
#     client.send_goal(goal)
#     client.wait_for_result(rospy.Duration.from_sec(5.0))

# if __name__ == '__main__':
rospy.init_node('Franka_gripper_grasp_action')
client = actionlib.SimpleActionClient('/franka_gripper/grasp', GraspAction)
client.wait_for_server()
goal = GraspGoal()
#goal.width = 0.01749
goal.width = 0.05
goal.speed = 0.05
goal.force = 2
goal.epsilon.inner = 0.01
goal.epsilon.outer = 0.01
#goal = GraspGoal(width = 0.05, speed = 0.03, force = 10) # width = 0.04
client.send_goal(goal)
client.wait_for_result()#rospy.Duration.from_sec(10.0))

#GraspAction(width, epsilon inner, epsilon outer, speed, force)

