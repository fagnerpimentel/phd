#!/bin/bash

export CATKIN_PATH=/home/alunos/fpimentel/catkin_fagner
export RESULT_PATH=/home/alunos/

# permissions for ports
sudo chmod 777 /dev/ttyACM*
sudo chmod 777 /dev/ttyUSB*
sudo chmod 777 /dev/opencm

cd ../scripts/

./start_experiment.sh experiments_sets/real/common_1

#./start_experiment.sh experiments_sets/real/social_0
# ./start_experiment.sh experiments_sets/real/social_1
# ./start_experiment.sh experiments_sets/real/social_2
