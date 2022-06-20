import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi


from franka_gripper.msg import MoveGoal, MoveAction, GraspAction, GraspGoal
import actionlib


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface', anonymous=True)

robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group_name = "panda_arm"
group = moveit_commander.MoveGroupCommander(group_name)

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory, queue_size=20)

# To print the reference frame of robot:
planning_frame = group.get_planning_frame()
print("planning_frame is: ", planning_frame)
# To print the name of the end-effector link for this group:
eef_link = group.get_end_effector_link()
print("eef_link is: ", eef_link)
# To print a list of all the groups in the robot:
group_names = robot.get_group_names()
print("group_names are: ", group_names)
# To print the entire state of the robot:
robot_state = robot.get_current_state()
print("\nrobot_state is: \n ", robot_state)

# # #rospy.init_node('Franka_gripper_grasp_action')
# client = actionlib.SimpleActionClient('/franka_gripper/grasp', GraspAction)
# client.wait_for_server()
# goal = GraspGoal()
# goal.width = 0.01749
# #goal.width = 0.03
# goal.speed = 0.05
# goal.force = 2
# goal.epsilon.inner = 0.01
# goal.epsilon.outer = 0.01
# #goal = GraspGoal(width = 0.05, speed = 0.03, force = 10) # width = 0.04
# client.send_goal(goal)
# client.wait_for_result()#rospy.Duration.from_sec(10.0))

# # Grasp position
# joint_goal2 = group.get_current_joint_values()
# joint_goal2[0] = 0.41334735036105436
# #joint_goal2[0] = 1.1
# joint_goal2[1] = 0.5953334149645086
# joint_goal2[2] = -0.25627281372896016
# joint_goal2[3] = -2.1269377079344634
# joint_goal2[4] = 0.2012767646229929
# joint_goal2[5] = 2.6208488211631775
# joint_goal2[6] = -0.4251947451697455
# group.go(joint_goal2, wait=True)
# group.stop() # makes sure no residual movements left

# # Grasp position
# joint_goal2 = group.get_current_joint_values()
# joint_goal2[0] = 0.41334735036105436
# joint_goal2[0] = 1
# joint_goal2[1] = 0.5953334149645086
# joint_goal2[2] = -0.25627281372896016
# joint_goal2[3] = -2.1269377079344634
# joint_goal2[4] = 0.2012767646229929
# joint_goal2[5] = 2.6208488211631775
# joint_goal2[6] = -0.4251947451697455
# group.go(joint_goal2, wait=True)
# group.stop() # makes sure no residual movements left


# # #rospy.init_node('Franka_gripper_grasp_action')
# client = actionlib.SimpleActionClient('/franka_gripper/grasp', GraspAction)
# client.wait_for_server()
# goal = GraspGoal()
# goal.width = 0.01749
# #goal.width = 0.03
# goal.speed = 0.05
# goal.force = 2
# goal.epsilon.inner = 0.01
# goal.epsilon.outer = 0.01
# #goal = GraspGoal(width = 0.05, speed = 0.03, force = 10) # width = 0.04
# client.send_goal(goal)
# client.wait_for_result()#rospy.Duration.from_sec(10.0))

# Top Position
joint_goal1 = group.get_current_joint_values()
joint_goal1[0] = 0.0002956538604605093
joint_goal1[1] = -0.7852994204019492
joint_goal1[2] = -0.0003258829146784897
joint_goal1[3] = -1.5710869377658905
joint_goal1[4] = 0.0007795814467934191
joint_goal1[5] = 0.5242273213149147
joint_goal1[6] = -0.0005237119993032998
group.go(joint_goal1, wait=True)
group.stop() # makes sure no residual movements left



# joint_goal2 = group.get_current_joint_values()
# joint_goal2 = [1.7583151177626548, -0.3323775173530244, 2.2950410289652856, -2.302952336753129, -2.4502814057581883, 1.9585690123375048, -2.3938593574656113] # 0.03952542319893837, 0.03952542319893837]
# group.go(joint_goal2, wait=True)
# group.stop() 
