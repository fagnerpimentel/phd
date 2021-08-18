#!/bin/bash

export CATKIN_PATH=/home/alunos/fpimentel/catkin_fagner
export RESULT_PATH=/home/alunos/

cd ../scripts/

./start_experiment.sh experiments_sets/2_simulation_social_navigation_dynamic/I-common-passive
# ./start_experiment.sh experiments_sets/2_simulation_social_navigation_dynamic/I-common-active

./start_experiment.sh experiments_sets/2_simulation_social_navigation_dynamic/II-social-passive
# ./start_experiment.sh experiments_sets/2_simulation_social_navigation_dynamic/II-social-active

./start_experiment.sh experiments_sets/2_simulation_social_navigation_dynamic/marathon-common
./start_experiment.sh experiments_sets/2_simulation_social_navigation_dynamic/marathon-social
