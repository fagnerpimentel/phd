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

world_name="$PWD/../worlds/fei_k5__marathon_1.world"
xterm -hold -e \
'roslaunch social_worlds start_world.launch \
world_path:='$world_name' \
enable_gui:=false' &
sleep 5

rviz_file="`rospack find social_experiments`/config/rviz/experiment.rviz"
xterm -hold -e \
'roslaunch hera_bringup interface.launch \
rviz_file:='$rviz_file' \
enable_gui_gazebo:=true \
enable_gui_rviz:=false \
enable_gui_teleop:=false \
enable_gui_telegram:=true' &
sleep 5

######################################################################

params_file=$1
source $params_file

roslaunch hera_bringup bring_up.launch \
map_config:="$map_config" \
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
