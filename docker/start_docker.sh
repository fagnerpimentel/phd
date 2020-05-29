#!/bin/bash

catkin_path="/catkin_ws"
result_path="/result"

now="$(date +'%Y-%m-%d_%H-%M-%S')"
container_name="social-"$now

docker run -it -d \
  --env CATKIN_PATH=/$catkin_path/ \
  --env RESULT_PATH=/$result_path/ \
  --env GAZEBO_MODEL_PATH='/home/catkin_social/src/social_worlds/models/:/home/catkin_social/src/social_worlds/models/3dparty/' \
  --name $container_name osrf/ros:melodic-desktop-full-bionic

docker exec -it                     $container_name bash -c 'mkdir "$CATKIN_PATH"'
docker exec -it                     $container_name bash -c 'mkdir "$RESULT_PATH"'
docker cp install_packages.sh       $container_name:$catkin_path
docker cp ../experiments_sets       $container_name:$catkin_path
docker cp ../start_experiments.sh   $container_name:$catkin_path
docker cp ../plot_result.py         $container_name:$catkin_path
docker cp ../plot_maps.py           $container_name:$catkin_path
docker exec -w $catkin_path -it     $container_name bash -c './install_packages.sh'
docker exec -w $catkin_path -it     $container_name bash -c 'source /opt/ros/melodic/setup.bash; catkin_make'

docker exec -w $catkin_path -it     $container_name bash -c './start_experiments.sh experiments_sets/set_1-amcl'
docker exec -w $catkin_path -it     $container_name bash -c './start_experiments.sh experiments_sets/set_1-fl'
docker exec -w $catkin_path -it     $container_name bash -c './start_experiments.sh experiments_sets/set_2-global'
docker exec -w $catkin_path -it     $container_name bash -c './start_experiments.sh experiments_sets/set_3-dwa'
docker exec -w $catkin_path -it     $container_name bash -c './start_experiments.sh experiments_sets/set_3-eband'
docker exec -w $catkin_path -it     $container_name bash -c './start_experiments.sh experiments_sets/set_3-teb'
docker exec -w $catkin_path -it     $container_name bash -c './start_experiments.sh experiments_sets/set_4-eband'
docker exec -w $catkin_path -it     $container_name bash -c './start_experiments.sh experiments_sets/set_4-teb'
docker exec -w $catkin_path -it     $container_name bash -c './start_experiments.sh experiments_sets/set_5'
# docker exec -w $catkin_path -it     $container_name bash -c './start_experiments.sh experiments_sets/set_6'

docker cp $container_name:$result_path $HOME/result_$container_name

docker container kill $container_name
