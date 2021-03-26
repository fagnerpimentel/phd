#!/bin/bash

export CATKIN_PATH=/home/alunos/fpimentel/catkin_fagner
export RESULT_PATH=/home/alunos/

cd ../scripts/

./start_simulation.sh experiments_sets/real_simulation/common-static
./start_simulation.sh experiments_sets/real_simulation/social-static

# ./start_simulation.sh experiments_sets/real_simulation/common-dynamic
# ./start_simulation.sh experiments_sets/real_simulation/social-dynamic
