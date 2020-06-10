#!/bin/bash

# if [[ -z "${CATKIN_PATH}" ]]; then
#   echo "You need to set the CATKIN_PATH env variable before start!"
#   exit
# fi

mkdir $CATKIN_PATH/src
cd $CATKIN_PATH/src

git clone https://gitlab.com/fpimentel/hera/hera_description.git
git clone https://gitlab.com/fpimentel/hera/hera_nav.git
git clone https://gitlab.com/fpimentel/hera/hera_bringup.git
git clone https://gitlab.com/fpimentel/social_robot/social_worlds.git
git clone https://gitlab.com/fpimentel/social_robot/social_experiments.git
git clone https://github.com/DLu/navigation_layers.git

cd hera_description   ; git checkout -q 9178e6eef807f61e03cb64cc4e13f6a77fbb8b8f ; cd ..
cd hera_nav           ; git checkout -q a0cbf09bbd513424bd55947788160a191afb80fe ; cd ..
cd hera_bringup       ; git checkout -q 6c386c6ece86ef6e8f8554e38f862c3e27fa1aaf ; cd ..
cd social_worlds      ; git checkout -q 11d091fe4c4d6229bcff1f01d3ba3f5cd7c3fb5b ; cd ..
cd social_experiments ; git checkout -q 397977efecd31e2a60d8d842b157c5ec477186af ; cd ..

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
