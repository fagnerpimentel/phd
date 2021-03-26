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
max_experiments="100"

######################################################################

path=${RESULT_PATH}/${params_file}
mkdir -p $path/

for env in ${!environment[@]};
do

  env_params=(${environment[${env}]})
  world_name=${env_params[0]}
  scenario_name=${env_params[1]}

  path_storage=$path/$env

  rm -r $path_storage
  mkdir $path_storage

  export ROS_LOG_DIR=$path_storage/log
  roslaunch gym_social start1.launch \
    max_experiments:="$max_experiments" \
    path_storage:="$path_storage/" \
    use_amcl:="$use_amcl" \
    global_planner:="$global_planner" \
    local_planner:="$local_planner" \
    global_layers:="$global_layers" \
    local_layers:="$local_layers" \
    observation_sources:="$observation_sources" \
    map_config:="$PWD/../resources/maps/$map/map.yaml" \
    world_name:="$world_name" \
    world_path:="$PWD/../resources/worlds/$world_name.world" \
    scenario_path:="$PWD/../resources/scenarios/$scenario_name.xml" \
    database_input:="$PWD/../resources/databases/$database" \
    robot_waypoints:="$robot_path"
  unset ROS_LOG_DIR

  cp ../resources/map/"$map"/map.pgm $path_storage

done

unset ROS_MASTER_URI
unset ROS_IP

python3 plot_result.py $path
python3 plot_maps.py $path
