#!/bin/bash

mkdir $CATKIN_PATH/src
cd $CATKIN_PATH/src



git clone https://fagnerpimentel@gitlab.com/fpimentel/hera/hera_description.git
git clone https://fagnerpimentel@gitlab.com/fpimentel/hera/hera_nav.git
git clone https://fagnerpimentel@gitlab.com/fpimentel/hera/hera_bringup.git

git clone https://fagnerpimentel@gitlab.com/fpimentel/social_robot/social_worlds.git
git clone https://fagnerpimentel@gitlab.com/fpimentel/social_robot/social_experiments.git

apt-get update
apt-get install -y iproute2
apt-get install -y ros-melodic-map-server
apt-get install -y ros-melodic-fake-localization
apt-get install -y ros-melodic-move-base
apt-get install -y ros-melodic-dwa-local-planner
apt-get install -y ros-melodic-eband-local-planner
apt-get install -y ros-melodic-teb-local-planner

apt-get install -y python3-pip
pip3 install matplotlib
pip3 install seaborn
pip3 install pandas
pip3 install pyyaml
pip3 install pillow
