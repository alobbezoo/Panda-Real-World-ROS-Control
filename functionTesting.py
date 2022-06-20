from motionFunctions import *

def main():
    
    controller = MoveGroupPythonInterface()
    # controller.go_to_joint_state()
    # controller.go_to_home_state()
    controller.go_to_pose_goal(pose_goal_position_x=0.6, pose_goal_position_y= 0, pose_goal_position_z= 0.5, pose_goal_orientation_x = -0.924, pose_goal_orientation_y = 3/8, pose_goal_orientation_z = 0, pose_goal_orientation_w = 0)
    # controller.print_current_state()
    # controller.print_current_state()
    
    #NOTE: Testing itterative grasping here
    # joint_goal0 = 0 
    # joint_goal1 = 0
    # joint_goal2 = 0
    # joint_goal3 = -tau/4
    # joint_goal4 = 0
    # joint_goal5 = tau/4
    # joint_goal6 = tau/8

    # for i in range(4):
    #     joint_goal0 += 0.05 
    #     joint_goal1 += 0.05 
    #     joint_goal2 += 0.05 
    #     joint_goal3 += 0.05 
    #     joint_goal4 += 0.05 
    #     joint_goal5 += 0.05 
    #     joint_goal6 += 0.05

    #     controller.go_to_joint_state(joint_goal0 = joint_goal0, joint_goal1 = joint_goal1, 
    #     joint_goal2 = joint_goal2, joint_goal3 = joint_goal3, joint_goal4 = joint_goal4, 
    #     joint_goal5 = joint_goal5, joint_goal6 = joint_goal6)
    
    controller.go_to_joint_state()

if __name__ == "__main__":
    main()

