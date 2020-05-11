#!/bin/bash

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

declare -A worlds
worlds["sr"]="simple_room"
worlds["sr_b"]="simple_room__boxes"
# worlds["sr_bs"]="simple_room__boxes_small"
worlds["sr_t"]="simple_room__tables"
# # worlds["sr_sp"]="simple_room__static_people"
# # worlds["sr_dp"]="simple_room__dynamic_people"

declare -A observations
# observations["s1"]="laser_scan_front_observation"
# observations["s2"]="laser_scan_front_observation laser_scan_back_observation"
observations["s3"]="laser_scan_front_observation laser_scan_back_observation point_cloud_base_front_observation"
# observations["s4"]="laser_scan_front_observation laser_scan_back_observation point_cloud_base_front_observation point_cloud_torso_front_observation"

declare -A planners
planners["base"]="base_local_planner/TrajectoryPlannerROS"
planners["dwa"]="dwa_local_planner/DWAPlannerROS"
planners["eband"]="eband_local_planner/EBandPlannerROS"
planners["teb"]="teb_local_planner/TebLocalPlannerROS"

######################################################################


path=$PWD/result
mkdir $path/

# killall roscore
# killall rosmaster
# roscore &
# sleep 2

for world in ${!worlds[@]};
do

  for observation in ${!observations[@]};
  do

    for planner in ${!planners[@]};
    do

      use_fake_localization="true"
      max_experiments="100"
      xy_goal_tolerance="0.1"
      yaw_goal_tolerance="3.1415"

      map_name=${worlds[${world}]}
      observation_sources=${observations[${observation}]}
      global_planner="global_planner/GlobalPlanner"
      local_planner=${planners[${planner}]}
      path_storage=$path/$world-$observation-$planner

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

      # rosbag compress -f $path_storage/*
      # rm $path_storage/*.orig.bag

    done
  done
done

cp `rospack find hera_bringup`/resources/map/simple_room/map.pgm $path
python3 plot_result.py $path
python3 plot_maps.py $path
