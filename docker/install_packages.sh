#!/bin/bash

# if [[ -z "${CATKIN_PATH}" ]]; then
#   echo "You need to set the CATKIN_PATH env variable before start!"
#   exit
# fi

mkdir $CATKIN_PATH/src
cd $CATKIN_PATH/src

git clone https://fagnerpimentel@gitlab.com/fpimentel/hera/hera_description.git
git clone https://fagnerpimentel@gitlab.com/fpimentel/hera/hera_nav.git
git clone https://fagnerpimentel@gitlab.com/fpimentel/hera/hera_bringup.git

git clone https://fagnerpimentel@gitlab.com/fpimentel/social_robot/social_worlds.git
git clone https://fagnerpimentel@gitlab.com/fpimentel/social_robot/social_experiments.git

apt-get update
./hera_description/install_dependencies.sh
./hera_nav/install_dependencies.sh
./hera_bringup/install_dependencies.sh

apt-get install -y iproute2
apt-get install -y python3-pip
pip3 install matplotlib
pip3 install seaborn
pip3 install pandas
pip3 install pyyaml
pip3 install pillow
