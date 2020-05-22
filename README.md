# PHD

[Este projeto](https://gitlab.com/fpimentel/phd) faz parte da pesquisa de doutodaro  no [Centro universitário FEI](https://portal.fei.edu.br/) realizada pelo aluno [Fagner Pimentel](mailto:fagnerpimentel@gmail.com), o qual é autor e mantenedor deste repositório. O repositório tem como objetivo automatizar experimentos de navegação social utilizando um robô social em ambiente simulado.

# Table of Contents
1. [Requisitos](#requisitos)
2. [Experimentos](#experimentos)
3. [Resultados](docs/results.md)
5. [Como reproduzir os experimentos utilizando este repositório](#como-reproduzir-os-experimentos-utilizando-este-repositório)

# Requisitos

## [Gazebo](http://gazebosim.org/)
Um simulador dinâmico 3D com habilidade de eficientemente e corretamente simular populações de robôs em ambientes complexos internos e externos.

## [ROS](http://www.ros.org/)
Um *framework* que auxilia na escrita de software para robôs.

## [HERA](https://gitlab.com/fpimentel/hera)
Robô desenvolvido pela equipe [RoboFEI@home](http://robofei.aquinno.com/athome/) no [Centro universitário FEI](https://portal.fei.edu.br/). O HERA é utilizado como estudo de caso neste projeto.


1. [hera_description](https://gitlab.com/fpimentel/hera/hera_description) - Modelo de descrição e simulação escrito em [URDF](http://wiki.ros.org/urdf).
2. [hera_nav](https://gitlab.com/fpimentel/hera/hera_nav) - Implementação do Stack de Navegação do ROS ([ROS Navigation Stack - RNS](http://wiki.ros.org/navigation)).
2. [hera_bringup](https://gitlab.com/fpimentel/hera/hera_bringup) - Arquivos de inicialização para operar o robô.

## [Social Robot](https://gitlab.com/fpimentel/social_robot)
Um conjunto de ferramentas implementadas para facilitar o desenvolvimento e avaliação de robôs sociais.

1. [social_words](https://gitlab.com/fpimentel/social_robot/social_words) - Ambientes de simulação modelados no Gazebo utilizados para explorar as capacidades de atuação de um robô social em diversos cenários.
2. [social_experiments](https://gitlab.com/fpimentel/social_robot/social_experiments) - Roteiros de teste e avaliação que podem ser aplicados em um robô social.

## Ferramentas para visuaização de dados
1. [matplotlib](https://matplotlib.org/)
2. [seaborn](https://seaborn.pydata.org/)
3. [pandas](https://pandas.pydata.org/)
4. [pyyaml](https://pypi.org/project/PyYAML/)
5. [pillow](https://pypi.org/project/Pillow/)

# Experimentos

## Infraestrutura

Para a realização dos experimentos foi utilizado um [computador *desktop* DELL XPS 8500](https://www1.la.dell.com/br/pt/corp/Computadores/xps-8500/pd.aspx?refid=xps-8500&s=corp) com 8 processadores i7-3770 CPU @ 3.40GHz, 12GB de memória RAM e placa gráfica NVIDEA GeForce GT640.


## Preparação da navegação
* Otimização dos mapas de custo
  * static_map
  * obstacles
  * proxemics
  * inflation
* Otimização dos comportamentos de recuperação
  * clear_costmap_recovery
  * rotate_recovery
* Otimização e seleção de sistema de localização
  * Adaptive Monte Carlo localization (amcl)
  * Fake Localization (fl)
* Otimização e seleção de planejadores globais
  * navfn_planner
  * carrot_planner
  * global_planner
* Otimização e seleção de planejadores locais
  * base_local_planner
  * dwa_local_planner
  * eband_local_planner
  * teb_local_planner

# Resultados

# Como reproduzir os experimentos utilizando este repositório

| WARNING: Este processo leva bastante tempo para ser realizado! (Dias, dependendo da quantidade de testes e do poder de processamento da máquina utilizada) |
| --- |

| WARNING: Os scripts estão programados para executar em uma máquina com SO [Ubuntu 18.04.4 LTS (Bionic Beaver)](https://releases.ubuntu.com/18.04.4/) e [ROS Melodic Morenia](http://wiki.ros.org/melodic)! |
| --- |

Exitem duas maneiras de utilizar este repositório. (1) Usando o ambiente de [docker](https://www.docker.com/) com todos os experimetos realizados de forma padrão e automática, ou (2) executando cada conjunto de teste separadamente.

## Com docker
Inicialmente, caso você não tenha o docker instalado em sua máquina, você pode seguir as instruções deste [link](https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04) ou entrar na pasta ```phd/docker/``` e utilizar o comando a seguir para instalar:
```bash
sudo ./install_docker.sh
```

Com o docker instalado, execute o seguinte comando para iniciar os experimentos:
```bash
sudo ./start_docker.sh
```

Ao final da realização dos experimentos, será criada uma pasta em ```/home/<user>/``` onde os resultados serão armazenados.

## Sem docker
Caso prefira não utilizar o docker, será preciso preparar o ambinete. Para isso, você deve [instalar o ros](http://wiki.ros.org/melodic/Installation), baixar as [dependências](#dependencias) deste projeto e instalar suas respectivas dependências, [compilar e carregar o catkin](http://wiki.ros.org/catkin/commands/catkin_make) e por fim carregar as seguintes variáveis de ambinete:

```bash
export CATKIN_PATH=<path_to_your_catkin_folder>
```

```bash
export RESULT_PATH=<path_to_folder_where_results_will_be_saved>
```
Para executar os experimentos, execute um destes comandos dentro da pasta ```phd```:
```bash
./start_experiment.sh ./start_experiments.sh experiments_sets/set_1-base
```
```bash
./start_experiment.sh ./start_experiments.sh experiments_sets/set_1-dwa
```
```bash
./start_experiment.sh ./start_experiments.sh experiments_sets/set_1-eband
```
```bash
./start_experiment.sh ./start_experiments.sh experiments_sets/set_1-teb
```
```bash
./start_experiment.sh ./start_experiments.sh experiments_sets/set_2-teb
```
```bash
./start_experiment.sh ./start_experiments.sh experiments_sets/set_1-eband
```
```bash
./start_experiment.sh ./start_experiments.sh experiments_sets/set_all
```
```bash
./start_experiment.sh ./start_experiments.sh experiments_sets/set_test
```

Ao final da realização dos experimentos, será criada uma pasta em ```RESULT_PATH``` onde os resultados serão armazenados.
