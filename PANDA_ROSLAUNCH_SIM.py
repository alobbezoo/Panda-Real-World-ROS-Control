import os
import time
def mycmd():
    os.system('gnome-terminal -e "roslaunch panda_gazebo start_pick_and_place_world.launch"')
    time.sleep(2)
    os.system('gnome-terminal -e "roslaunch panda_gazebo put_robot_in_world.launch "')

mycmd()
