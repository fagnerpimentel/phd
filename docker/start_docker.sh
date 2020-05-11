#!/bin/bash

catkin_path="/catkin_ws"

now="$(date +'%H_%M_%S-%d_%m_%Y')"
container_name="social-"$now

docker run -it -d \
  --env CATKIN_PATH=/$catkin_path \
  --env GAZEBO_MODEL_PATH='/home/catkin_social/src/social_worlds/models/:/home/catkin_social/src/social_worlds/models/3dparty/' \
  --name $container_name osrf/ros:melodic-desktop-full-bionic

docker exec -it                     $container_name bash -c 'mkdir "$CATKIN_PATH"'
docker cp install_packages.sh       $container_name:$catkin_path
docker cp ../start_experiments.sh   $container_name:$catkin_path
docker cp ../plot_result.py         $container_name:$catkin_path
docker cp ../plot_maps.py           $container_name:$catkin_path
docker exec -w $catkin_path -it     $container_name bash -c './install_packages.sh'
docker exec -w $catkin_path -it     $container_name bash -c 'source /opt/ros/melodic/setup.bash; catkin_make'
docker exec -w $catkin_path -it     $container_name bash -c './start_experiments.sh'

docker cp $container_name:$catkin_path/result  ../result_$container_name

docker container kill $container_name
