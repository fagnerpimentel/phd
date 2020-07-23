#!/bin/bash

# if [[ -z "${CATKIN_PATH}" ]]; then
#   echo "You need to set the CATKIN_PATH env variable before start!"
#   exit
# fi

mkdir $CATKIN_PATH/src
cd $CATKIN_PATH/src

git clone https://github.com/Home-Environment-Robot-Assistant/hera_description.git
git clone https://github.com/Home-Environment-Robot-Assistant/hera_nav.git
git clone https://github.com/Home-Environment-Robot-Assistant/hera_bringup.git
git clone https://github.com/Social-Droids/social_worlds.git
git clone https://github.com/Social-Droids/social_experiments.git
git clone https://github.com/DLu/navigation_layers.git

cd hera_description   ; git checkout -q 9178e6eef807f61e03cb64cc4e13f6a77fbb8b8f ; cd ..
cd hera_nav           ; git checkout -q bea1e30a78cce8ce3c8284ef5ee676cc10c928f2 ; cd ..
cd hera_bringup       ; git checkout -q b294e08f0f8eb146351e81698b07d3324897e47d ; cd ..
cd social_worlds      ; git checkout -q b3de197678a95bf62f780ad70a3a77c3cd5cab1b ; cd ..
cd social_experiments ; git checkout -q 1794b82068dcdc091fe3bad3e2bf13a3ace8f5e3 ; cd ..

apt-get update
./hera_description/install_dependencies.sh
./hera_nav/install_dependencies.sh
./hera_bringup/install_dependencies.sh
./social_worlds/install_dependencies.sh

apt-get install -y iproute2
apt-get install -y python3-pip
pip3 install matplotlib
pip3 install seaborn
pip3 install pandas
pip3 install pyyaml
pip3 install pillow
