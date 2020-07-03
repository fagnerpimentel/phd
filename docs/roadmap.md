# TODO :





* 1 **Texto** - Refazer referencia bibliografica
* 1 **Texto** - Organizar introducao
* 1 **Quali** - regras sociais no simulador
* 1 **Quali** - ontologia
  * implementar a cora no agente
  * espandir a cora para o projeto
  * 1 **Quali** - realizar aprendizado com ontologia
    * implemetar o openai nosimulador (treinamento offline e teste)
    * aplicar em ambiente real (treinamento online e teste)
  * 2 **Quali** - preparar questionario para ambiente real
  * 2 **Quali** - percepção? (simulado/real)
  * 2 **Quali** - mapeamento semantico
mo foi otimizado e cada variavel utilizada fora do padrão
* 2 **hera_nav** - add imagens con diferenças da otimização antes e depois
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

* 5 **Experimentos** - adicionar população
* 5 **Experimentos** - interface gráfica

* 5 **hera_description** - rethink the design - see another robots)
* 5 **hera_description** - update sizes and weights
* 5 **hera_description** - remove magical numbers
* 5 **hera_description** - review parameters ins sensors plugins
* 5 **hera_description** - add robot prefix (to allow multi robots)
* 5 **hera_description** - publish cameras whit tho different resolutions
* 5 **hera_bringup** - remover resources (?)
* 5 **Todos os pacotes** - adicionar licença
* 5 **Todos os pacotes** - dev-ops?


legenda:
1. Alta prioridade.
2. Média prioridade.
3. Baixa prioridade texto.
4. Baixa prioridade repositório.
5. Não é necessário, mas é bom fazer.

#####################################################

* trabalho futuros
  * melhorar gráficos dos resultados
  * apresentar p-value dos resultados
  * migrar para ROS 2
  * otimizar a localização
  * Base circular (design)
  * laser giratório (design)
  * Usar navigation omnidirecional  (Planejadores local)
  * Fazer combinações dos sesores para construir os costmaps de obstáculos (clearing, marking)
  * implementar navegação sem lasers, ultrasom ou IR (usar percepção para criar um modelo de mundo e posteriormente um mapa de custocamada de mapa de custo)
