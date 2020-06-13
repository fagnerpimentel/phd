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
cd hera_bringup       ; git checkout -q 50319705d2968de54ab674eea3a49576d55c419f ; cd ..
cd social_worlds      ; git checkout -q c7d4cd54a9b382e4e1a05c906a70ef647ff7831c ; cd ..
cd social_experiments ; git checkout -q efcf29311420a56b9270ccd5e34c750b80d8d302 ; cd ..

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
