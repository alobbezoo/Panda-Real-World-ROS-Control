import os
import time

def mycmd():
    # os.system('cd /home/hjkwon/franka_ws')
    # time.sleep(1)
    os.system('source /home/hjkwon/franka_ws/devel/setup.bash')
    time.sleep(1)
    os.system('gnome-terminal -e "roslaunch franka_control franka_control.launch robot_ip:=172.16.0.2 load_gripper:=true"')
    time.sleep(2)
    os.system('gnome-terminal -e "roslaunch panda_moveit_config panda_moveit.launch controller:=position"')
    time.sleep(1)
    os.system('gnome-terminal -e "roslaunch panda_moveit_config moveit_rviz.launch"')

mycmd()
