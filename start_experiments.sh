#!/bin/bash

if [[ -z "${CATKIN_PATH}" ]]; then
  echo "You need to set the CATKIN_PATH env variable before start!"
  exit
fi

if [[ -z "${RESULT_PATH}" ]]; then
  echo "You need to set the RESULT_PATH env variable before start!"
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

params_file=$1
source $params_file
max_experiments="10"

######################################################################

path=${RESULT_PATH}/${params_file}
mkdir -p $path/

for world in ${!worlds[@]};
do

  for planner in ${!planners[@]};
  do

    map_name=${worlds[${world}]}
    local_planner=${planners[${planner}]}

    path_storage=$path/$world-$planner

    mkdir $path_storage

    echo "world: " $map_name
    echo "observation: " $observation_sources
    echo "global planner: " $global_planner
    echo "local planner: " $local_planner

    roslaunch social_experiments experiment.launch \
      use_fake_localization:="$use_fake_localization" \
      max_experiments:="$max_experiments" \
      xy_goal_tolerance:="$xy_goal_tolerance" \
      yaw_goal_tolerance:="$yaw_goal_tolerance" \
      map_name:="$map_name" \
      global_planner:="$global_planner" \
      local_planner:="$local_planner" \
      observation_sources:="$observation_sources" \
      path_storage:="$path_storage"

  done
done

cp `rospack find hera_bringup`/resources/map/simple_room/map.pgm $path
python3 plot_result.py $path
python3 plot_maps.py $path
