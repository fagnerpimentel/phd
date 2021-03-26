#!/bin/bash

export CATKIN_PATH=/home/alunos/fpimentel/catkin_fagner
export RESULT_PATH=/home/alunos/

cd ../scripts/

./start_simulation.sh experiments_sets/2_simulation_social_navigation_dynamic/I-commom-passive
# ./start_simulation.sh experiments_sets/2_simulation_social_navigation_dynamic/I-commom-active

./start_simulation.sh experiments_sets/2_simulation_social_navigation_dynamic/II-social-passive
# ./start_simulation.sh experiments_sets/2_simulation_social_navigation_dynamic/II-social-active
