# TODO :

* 1 **Texto** - falar sobre a [otimização](https://github.com/zkytony/ROSNavigationGuide/blob/master/main.pdf)
* 1 **Texto** - **Organizar metodologia**
* 1 **Texto** - **adicionar resultados**
* 1 **Texto** - **adicionar discursão**
* 1 **Texto** - Refazer referencia bibliografica
* 1 **Texto** - Organizar introducao
* 1 **Experimentos** - **otimizar eband**
* 1 **Experimentos** - **desviar de pequenos objetos**
* 1 **Experimentos** - preparar ambiente real
* 1 **Quali** - regras sociais no simulador
* 1 **Quali** - ontologia
  * implementar a cora no agente
  * espandir a cora para o projeto
* 1 **Quali** - realizar aprendizado com ontologia
  * implemetar o openai nosimulador (treinamento offline e teste)
  * aplicar em ambiente real (treinamento online e teste)
-
* 2 **Quali** - pegar dados sobre naturalidade
* 2 **Quali** - preparar questionario para ambiente real
* 2 **Quali** - percepção? (simulado/real)
* 2 **Quali** - mapeamento semantico
* 2 **hera_nav** - explicar como foi otimizado e cada variavel utilizada fora do padrão
* 2 **hera_nav** - add imagens con diferenças da otimização antes e depois
-
* 3 **Experimentos** - melhorar apresentação dos resultados
* 3 **Experimentos** - apresentar p-value dos resultados
-
* 4 **hera_description** - documantar a verificação de colisão
* 4 **hera_description** - documentar os parametros dos sensores simulados e verificar se são iguais ao real
* 4 **hera_control** - add joint control plugin
* 4 **hera_description** - add yaml file with robot measures
* 4 **hera_description** - falar sobre joint state gui no readme
* 4 **social_worlds** - iniciar documentação
* 4 **social_experiments** - iniciar documentação
* 4 **phd** - como usar os experimentos em outros robos?
* 4 **phd** - passar p ingles
* 4 **Todos os pacotes** - verificar consitencia de codigo/documentação
* 4 **Todos os pacotes** - dar exemplos dos usos dos pacotes
* 4 **Todos os pacotes** - Atualizar documentação
-
* 5 **Experimentos** - interface gráfica
* 5 **hera_description** - rethink the design - see another robots)
* 5 **hera_description** - update sizes and weights
* 5 **hera_description** - remove magical numbers
* 5 **hera_description** - review parameters ins sensors plugins
* 5 **hera_description** - add robot prefix (to allow multi robots)
* 5 **hera_description** - publish cameras whit tho different resolutions
* 5 **hera_bringup** - remover resources (?)
* 5 **social_experiments** - remover pasta 'map'
* 5 **Todos os pacotes** - adicionar licença
* 5 **Todos os pacotes** - dev-ops?


legenda:
1. Alta prioridade.
2. Média prioridade.
3. Baixa prioridade texto.
4. Baixa prioridade repositório.
5. Não é necessário, mas é bom fazer.


#####################################################

## Variáveis experimentais
* environment (ver [social_worlds](https://gitlab.com/fpimentel/social_robot/social_words))
  * [X] simple_room
  * [X] simple_room__boxes
  * [X] simple_room__corridors
  * [X] simple_room__boxes_small  
  * [X] simple_room__tables
  * [X] simple_room__mix_1
  * [ ] simple_room__static_people
  * [ ] simple_room__dynamic_people
  * [ ] simple_room__mix_2
  * [ ] fei_k5
* localization (ver [hera_nav](https://gitlab.com/fpimentel/hera/hera_nav))
  * [X] fake_localization
  * [ ] amcl_localization
* costmap layers (ver [hera_nav](https://gitlab.com/fpimentel/hera/hera_nav))
  * [X] static_map
  * [X] obstacles
  * [ ] VoxelLayer
  * [X] inflation
  * [ ] proxemics
* global planners (ver [hera_nav](https://gitlab.com/fpimentel/hera/hera_nav))
  * [ ] carot
  * [ ] navfn/NavfnROS
  * [X] global_planner/GlobalPlanner
* local planners (ver [hera_nav](https://gitlab.com/fpimentel/hera/hera_nav))
  * [X] base_local_planner/TrajectoryPlannerROS
  * [X] dwa_local_planner/DWAPlannerROS
  * [X] eband_local_planner/EBandPlannerROS
  * [X] teb_local_planner/TebLocalPlannerROS
* recovery behaviors (ver [hera_nav](https://gitlab.com/fpimentel/hera/hera_nav))
  * [ ] clear_costmap_recovery
  * [ ] rotate_recovery
  * [ ] move_slow_and_clear

#####################################################

# Trabalhos futuros
* Stageros (simulador?)
* Base circular (design)
* laser giratório (design)
* Usar navigation omnidirecional  (Planejadores local)
* Fazer combinações dos sesores para construir os costmaps de obstáculos (clearing, marking)
