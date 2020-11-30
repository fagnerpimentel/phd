#!/bin/bash

now="$(date +'%Y-%m-%d_%H-%M-%S')"

experiment_id="social-"$now
experiment_path=$HOME/$experiment_id
catkin_path=$experiment_path/catkin_ws
result_path=$experiment_path/result

mkdir $experiment_path
mkdir $catkin_path
mkdir $catkin_path/src

cp -r S1/ $catkin_path/
cp ../start_gym.sh $catkin_path/
cp ../plot_result.py $catkin_path/
cp ../plot_maps.py $catkin_path/

cd $catkin_path/src

git clone https://github.com/Home-Environment-Robot-Assistant/hera_description.git
git clone https://github.com/Home-Environment-Robot-Assistant/hera_control.git
git clone https://github.com/Home-Environment-Robot-Assistant/hera_nav.git
git clone https://github.com/Home-Environment-Robot-Assistant/hera_bringup.git
git clone https://github.com/Social-Droids/social_msgs.git
git clone https://github.com/Social-Droids/social_reasoning.git
git clone https://github.com/Social-Droids/social_layers.git
git clone https://github.com/Social-Droids/social_worlds.git
git clone https://github.com/Social-Droids/gym-social.git

# apt-get update
# ./hera_description/install_dependencies.sh
# ./hera_control/install_dependencies.sh
# ./hera_nav/install_dependencies.sh
# ./hera_bringup/install_dependencies.sh
# ./social_worlds/install_dependencies.sh
# ./gym-social/install_dependencies.sh

cd ..
catkin_make
source /opt/ros/melodic/setup.bash
source devel/setup.bash

export CATKIN_PATH=$catkin_path
export RESULT_PATH=$result_path

# ./start_gym.sh S1/I-amcl
./start_gym.sh S1/II-global
./start_gym.sh S1/II-navfn
./start_gym.sh S1/III-dwa
./start_gym.sh S1/III-eband
./start_gym.sh S1/III-teb
./start_gym.sh S1/IV-three
./start_gym.sh S1/IV-four
./start_gym.sh S1/V-common
./start_gym.sh S1/V-social
./start_gym.sh S1/VI-marathon
# ./start_gym.sh S1/VI-marathon-amcl
