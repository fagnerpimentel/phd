#!/bin/bash

if [[ -z "${CATKIN_PATH}" ]]; then
  echo "You need to set the CATKIN_PATH env variable before start!"
  exit
fi

######################################################################

# get machine ip
ip=$(ip route get 8.8.8.8 | awk -F"src " 'NR==1{split($2,a," ");print a[1]}')

# set ips
master_ip=$ip
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
# # REAL
#
# # permissions for ports
# sudo chmod 777 /dev/ttyACM*
# sudo chmod 777 /dev/ttyUSB*
# sudo chmod 777 /dev/opencm
#
# # find ports
# sudo python path_finder.py 15d1 0000     # laser
# sudo python path_finder.py 2341 003d     # Arduino base
# # sudo python path_finder.py 2341 0043   # Arduino head
# # sudo python path_finder.py fff1 ff48   # Dynamixel
#
# xterm -hold -e \
# 'roslaunch hera_bringup devices.launch' &
# sleep 5

######################################################################
# SIMULATION

world_name="$PWD/../resources/worlds/empty.world"
# world_name="$PWD/../resources/worlds/fei_k5__real_1.world"
xterm -hold -e \
'roslaunch social_worlds start_world.launch \
world_path:='$world_name' \
enable_gui:=true' &
sleep 5

######################################################################

rviz_file="$PWD/../config/experiment.rviz"
xterm -hold -e \
'roslaunch hera_bringup interface.launch \
rviz_file:='$rviz_file' \
enable_gui_gazebo:=false \
enable_gui_rviz:=true \
enable_gui_teleop:=false \
enable_gui_telegram:=true' &
sleep 5

######################################################################

params_file=$1
source $params_file

roslaunch hera_bringup bring_up.launch \
map_config:="$PWD/../resources/map/$map_config" \
database_input:="$PWD/../resources/database/$database" \
use_amcl:="$use_amcl" \
global_planner:="$global_planner" \
local_planner:="$local_planner" \
global_layers:="$global_layers" \
local_layers:="$local_layers" \
observation_sources:="$observation_sources" \
xy_goal_tolerance:="$xy_goal_tolerance" \
yaw_goal_tolerance:="$yaw_goal_tolerance"

unset ROS_MASTER_URI
unset ROS_IP
