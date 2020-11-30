#!/bin/bash

apt-get update
apt-get install -y iproute2
apt-get install -y python3-pip

pip3 install matplotlib
pip3 install seaborn
pip3 install pandas
pip3 install pyyaml
pip3 install pillow
