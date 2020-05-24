# Problemas
* O robô pende para frente (influencia da distribuição de peso e inercia no robô)
* o base replaneja mais rápido e é melhor em situações onde precisa replanejar
Simplificar a geração dos graficos (influencia dos parametros dos planejadores)
* o xtion apontado para frente não é adequado, ainda acontecem colisões com mesas, talvez o ideal seja colocar apontado para cima ou usar o kinect apontado para baixo
(gerar um artigo com estudo de caso sobre posicionamento e fusão de sensores)
* muitos parametos, alguns depreciados, fortemente dependentes dos recursos do robo (sensores, processamento), falta atualização na documentação,
* simples mudançanos parametros muda muito os resultados
* o teb anda de costas em alguns momentos


-------
[ WARN] [1590193585.518363515, 58.101000000]: /move_base: The origin for the sensor at (6.49, -0.01, 0.11) is out of map bounds. So, the costmap cannot raytrace for it.

[ WARN] [1590193586.289962659, 58.795000000]: /move_base: Map update loop missed its desired rate of 5.0000Hz... the loop actually took 0.2310 seconds

[ WARN] [1590194946.970223429, 47.919000000]: /move_base: TebLocalPlannerROS: possible oscillation (of the robot or its local plan) detected. Activating recovery strategy (prefer current turning direction during optimization).
