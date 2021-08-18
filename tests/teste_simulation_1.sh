#!/bin/bash

export CATKIN_PATH=/home/alunos/fpimentel/catkin_fagner
export RESULT_PATH=/home/alunos/

cd ../scripts/

# ./start_experiment.sh experiments_sets/1_simulation_social_navigation_static/I-common-passive
# ./start_experiment.sh experiments_sets/1_simulation_social_navigation_static/I-common-active
#
./start_experiment.sh experiments_sets/1_simulation_social_navigation_static/II-social-passive
./start_experiment.sh experiments_sets/1_simulation_social_navigation_static/II-social-active
#
# ./start_experiment.sh experiments_sets/1_simulation_social_navigation_static/marathon-common
# ./start_experiment.sh experiments_sets/1_simulation_social_navigation_static/marathon-social
