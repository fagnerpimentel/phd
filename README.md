
./install_docker.sh

./create_docker.sh

./experiments_docker.sh

./finish_docker.sh


<!-- # sudo docker stop $(sudo docker ps -aq) -->
<!-- # sudo docker system prune -->

export CATKIN_PATH=~/catkin_social/

# Problemas:
* O robô pende para frente (influencia da distribuição de peso e inercia no robô)
* o base replaneja mais rápido e é melhor em situações onde precisa replanejar
Simplificar a geração dos graficos (influencia dos parametros dos planejadores)
* o xtion apontado para frente não é adequado, ainda acontecem colisões com mesas, talvez o ideal seja colocar apontado para cima ou usar o kinect apontado para baixo
(gerar um artigo com estudo de caso sobre posicionamento e fusão de sensores)
* muitos parametos, alguns depreciados, fortemente dependentes dos recursos do robo (sensores, processamento), falta atualização na documentação,
* simples mudançanos parametros muda muito os resultados

# Grandes problemas do mundo real:
* sensor calibration (position on robot)
* localization
* Human perception

<!-- TODO: -->
<!-- * testar todos os comandos (dev-ops?) -->
<!-- * verificar todas as dependencias (launchs) -->
<!-- * dar exemplos dos usos dos pacotes -->
* experiments GUI
* remover pasta 'map' de social_experiments
* pegar uso de cpu

# Works
* environment
  * [X] simple_room
  * [X] simple_room__boxes
  * [X] simple_room__corridors
  * [X] simple_room__boxes_small  
  * [X] simple_room__tables
  * [X] simple_room__mix
  * [ ] simple_room__static_people
  * [ ] simple_room__dynamic_people
  * [ ] fei_k5
* robot design
  * base
    * [X] square
    * [ ] circle
  * sensors
    * [X] laser base front fixed
    * [ ] laser base front roll
    * [X] laser base back fixed
    * [X] camera depth base front fixed  
    * [ ] camera depth torso front pitch
    * [ ] camera color torso front pitch
* localization
  * [X] fake_localization
  * [ ] amcl_localization
* costmap layers optimization
  * [X] static_map
  * [X] obstacles
  * [ ] proxemics
  * [X] inflation
* global planners optimization
  * [ ] carot
  * [ ] navfn/NavfnROS
  * [X] global_planner/GlobalPlanner
* local planners optimization
  * [X] base_local_planner/TrajectoryPlannerROS
  * [X] dwa_local_planner/DWAPlannerROS
  * [X] eband_local_planner/EBandPlannerROS
  * [X] teb_local_planner/TebLocalPlannerROS
* recovery behaviors optimization
  * [ ] clear_costmap_recovery
  * [ ] rotate_recovery

# Others Possibilities:
* base circular (desing)
* stageros (simulator?)
* Use omni navigation (local planners)
* fazer combinações dos sesores p construir os costmaps de obstáculos (clearing, marking)
* sensor giratório


# comentarios:
* explicar cada alteração e diferenças nos parametros em relação ao defout na otimização.
* existem muitos parametros para serem otimizados e a solução atual pode não ser otima, mas é uma sub otima aceitável.
* p-value
* o robo tenta achar outro caminho sempre, na presença de humanos ele pode esperar o humano passar antes de seguir o caminho
* otimização é feita com series de testes continuas em diversos ambientes e configurações de forma incremental.

# Experiments:
* robot design
  * base
    * square
* localization
  * fake_localization
* costmap layers
  * static_map
  * obstacles
  * inflation
* global planners
  * global_planner/GlobalPlanner

## Set 1
* environment
  * simple_room
  * simple_room__boxes
  * simple_room__narrow_corridors
* sensors
  * S2
* local planners
  * base_local_planner/TrajectoryPlannerROS

## Set 2
* environment
  * simple_room
  * simple_room__boxes
  * simple_room__narrow_corridors
* sensors
  * S2
* local planners
  * dwa_local_planner/DWAPlannerROS
  * eband_local_planner/EBandPlannerROS
  * teb_local_planner/TebLocalPlannerROS

## Set 3
* environment
  * simple_room__boxes_small  
  * simple_room__tables
  * simple_room__mix
* sensors
  * S3
* local planners
  * teb_local_planner/TebLocalPlannerROS

## Set 4
* environment
  * simple_room__static_people
  * simple_room__dynamic_people
  * fei_k5
* sensors
  S4
* local planners
  * teb_local_planner/TebLocalPlannerROS

## Set 5
* environment
  * simple_room__static_people
  * simple_room__dynamic_people
  * fei_k5
* sensors
  S4
* local planners
  * teb_local_planner/TebLocalPlannerROS
* costmap layers
  * proxemics
