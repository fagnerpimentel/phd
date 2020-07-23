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
cd hera_nav           ; git checkout -q c9ca3fc4a9625ab402a370898bec6332b09f7d3f ; cd ..
cd hera_bringup       ; git checkout -q 83670467485f8acb1062de0bfab44589db42c6ba ; cd ..
cd social_worlds      ; git checkout -q 93492748e0f85b720adcd2976155e52275990f65 ; cd ..
cd social_experiments ; git checkout -q 06fe76ee31328145a5b057439c6af5ef0c62268e ; cd ..

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
