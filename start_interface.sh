#!/bin/bash

######################################################################

# get machine ip
ip=$(ip route get 8.8.8.8 | awk -F"src " 'NR==1{split($2,a," ");print a[1]}')

# set ips
master_ip=${1:-$ip}
my_ip=$ip
echo "robot_ip: " $master_ip
echo "my_ip: " $my_ip

# export robot
export ROS_MASTER_URI=http://${master_ip}:11311
# export my_ip
export ROS_IP=${my_ip}

######################################################################

# change rosconsole format
export ROSCONSOLE_FORMAT='[${severity}] [${time}]: ${node}: ${message}'

# source catkin
source $CATKIN_PATH/devel/setup.bash

######################################################################

rviz_file="`rospack find social_experiments`/config/rviz/experiment.rviz"
enable_gui_gazebo="true"
enable_gui_rviz="true"
enable_gui_teleop="false"

# start interface
roslaunch hera_bringup interface.launch rviz_file:=$rviz_file enable_gui_gazebo:=$enable_gui_gazebo enable_gui_rviz:=$enable_gui_rviz enable_gui_teleop:=$enable_gui_teleop
