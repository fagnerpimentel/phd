# Infraestrutura utilizada nos experimentos reais

O Robô utilizado neste projeto é o robô de serviço [HERA (versão 2020)](http://robofei.aquinno.com/athome/wp-content/uploads/2020/01/TDP2020ROBOFEI.pdf) visto na figura a seguir.
O HERA foi desenvolvido pela equipe [RoboFEI@home](http://robofei.aquinno.com/athome/) no [Centro universitário FEI](https://portal.fei.edu.br/).

<figure align="center">
<img src=images/HERA.png>
<p>O Robô HERA.</p>
</figure>

O robô é composto pelas seguintes partes:


||||
|:-:|:-|:-|
| Controle: | [Mini PC Zotac ZBOX-EN1060K](https://www.zotac.com/us/product/mini_pcs/magnus-en1060k), intel&reg; Core&trade; i5 7500 CPU, 8GB de memoria RAM, placa gráfica GeForce GTX 1060. ||
|-|Sensores:| Atuadores:|
| Base: | 1 *laser* [Hokuyo UTM-30LX](https://www.hokuyo-aut.jp/search/single.php?serial=169). <br> 1 *laser* [Hokuyo URG-04LX-UG01](https://www.hokuyo-aut.jp/search/single.php?serial=166). <br> 1 câmera de profundidade [Asus Xtion pró](https://www.asus.com/3D-Sensor/Xtion_PRO/).| 1 base omnidirecional [Mecanum Wheel Vectoring Robot - IG52 DB](https://www.superdroidrobots.com/shop/item.aspx/programmable-mecanum-wheel-vectoring-robot-ig52-db/1788/). |
| Torso: | 1 botão de emergência. | 1 manipulador com 7 graus de liberdade. |
| Cabeça: | 1 câmera rgb e de profundidade -  [Microsoft Kinect](https://developer.microsoft.com/en-us/windows/kinect/). <br> 1 [Multi-sensor Matrix Creator](https://www.matrix.one/products/creator). <br> 2 microfones direcionais [RODE VideoMic GO](http://www.rode.com/microphones/videomicgo). | [Apple Ipad](https://www.apple.com/ipad/) (3ª geração) para interação. |


# Problemas no ambiente real
* Calibração dos sensores
* Localização
* Percepção de pessoas
