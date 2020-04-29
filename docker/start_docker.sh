#!/bin/bash

catkin_path="/catkin_ws"

now="$(date +'%H_%M_%S-%d_%m_%Y')"
container_name="social-"$now

sudo docker run -it -d \
  --env CATKIN_PATH=/$catkin_path \
  --env GAZEBO_MODEL_PATH='/home/catkin_social/src/social_worlds/models/:/home/catkin_social/src/social_worlds/models/3dparty/' \
  --name $container_name osrf/ros:melodic-desktop-full-bionic

sudo docker exec -it                     $container_name bash -c 'mkdir "$CATKIN_PATH"'
sudo docker cp install_packages.sh       $container_name:$catkin_path
sudo docker cp ../start_experiments.sh   $container_name:$catkin_path
sudo docker cp ../plot_result.py         $container_name:$catkin_path
sudo docker cp ../plot_maps.py           $container_name:$catkin_path
sudo docker exec -w $catkin_path -it     $container_name bash -c './install_packages.sh'
sudo docker exec -w $catkin_path -it     $container_name bash -c 'source /opt/ros/melodic/setup.bash; catkin_make'
sudo docker exec -w $catkin_path -it     $container_name bash -c './start_experiments.sh'

sudo docker cp $container_name:$catkin_path/result  ../result_$container_name

sudo docker container kill $container_name
