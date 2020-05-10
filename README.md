
./install_docker.sh

./create_docker.sh

./experiments_docker.sh

./finish_docker.sh


<!-- # sudo docker stop $(sudo docker ps -aq) -->
<!-- # sudo docker system prune -->

export CATKIN_PATH=~/catkin_social/

Problemas:
* O robô pende para frente (influencia da distribuição de peso e inercia no robô)
* o base replaneja mais rápido e é melhor em situações onde precisa replanejar
Simplificar a geração dos graficos (influencia dos parametros dos planejadores)
* o xtion apontado para frente não é adequado, ainda acontecem colisões com mesas, talvez o ideal seja colocar apontado para cima ou usar o kinect apontado para baixo
(gerar um artigo com estudo de caso sobre posicionamento e fusão de sensores)
* muitos parametos, alguns depreciados, fortemente dependentes dos recursos do robo (sensores, processamento), falta atualização na documentação,


<!-- TODO: -->
<!-- * testar todos os comandos (dev-ops?) -->
<!-- * verificar todas as dependencias (launchs) -->
<!-- * dar exemplos dos usos dos pacotes -->
* rotating laser in front of he robot
* experiments GUI
* add omni navigation


# Future Works
* usar navegação ominidirecional
* robot design optimization (base shape and sensors position)
* localization optimization
* costmap layers optimization
  * costmap_2d::StaticLayer
  * costmap_2d::VoxelLayer
  * costmap_2d::InflationLayer
* global planners optimization
  * carot
  * navfn/NavfnROS
  * global_planner/GlobalPlanner
* local planners optimization
  * base_local_planner/TrajectoryPlannerROS
  * dwa_local_planner/DWAPlannerROS
  * eband_local_planner/EBandPlannerROS
  * teb_local_planner/TebLocalPlannerROS
* environment optimization
  * simple_room
  * simple_room__corridor
  * simple_room__boxes
  * simple_room__boxes_small  
  * simple_room__tables
  * simple_room__static_people
  * simple_room__dynamic_people
* recovery behaviors optimization
  * clear_costmap_recovery
  * rotate_recovery

# Others Possibilities
* stageros (simulator?)


# comentarios:
* explicar cada alteração e diferenças nos parametros em relação ao defout na otimização.

* existem muitos parametros para serem otimizados e a solução atual pode não ser otima, mas é uma sub otima aceitável.
* p-value
