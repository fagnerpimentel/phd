#!/bin/bash

export CATKIN_PATH=/home/alunos/fpimentel/catkin_fagner
export RESULT_PATH=/home/alunos/

cd ../scripts/

./start_experiment.sh experiments_sets/0_simulation_navigation/I-global
./start_experiment.sh experiments_sets/0_simulation_navigation/I-navfn
./start_experiment.sh experiments_sets/0_simulation_navigation/II-dwa
./start_experiment.sh experiments_sets/0_simulation_navigation/II-eband
./start_experiment.sh experiments_sets/0_simulation_navigation/II-teb
./start_experiment.sh experiments_sets/0_simulation_navigation/III-two
./start_experiment.sh experiments_sets/0_simulation_navigation/III-three
./start_experiment.sh experiments_sets/0_simulation_navigation/III-four
./start_experiment.sh experiments_sets/0_simulation_navigation/marathon
