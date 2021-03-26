#!/bin/bash

export CATKIN_PATH=/home/alunos/fpimentel/catkin_fagner
export RESULT_PATH=/home/alunos/

cd ../scripts/

./start_simulation.sh experiments_sets/0_simulation_navigation/I-global
./start_simulation.sh experiments_sets/0_simulation_navigation/I-navfn
./start_simulation.sh experiments_sets/0_simulation_navigation/II-dwa
./start_simulation.sh experiments_sets/0_simulation_navigation/II-eband
./start_simulation.sh experiments_sets/0_simulation_navigation/II-teb
./start_simulation.sh experiments_sets/0_simulation_navigation/III-two
./start_simulation.sh experiments_sets/0_simulation_navigation/III-three
./start_simulation.sh experiments_sets/0_simulation_navigation/III-four
