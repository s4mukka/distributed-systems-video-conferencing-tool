
# Video Conference Tool

Esta é uma ferramenta de videoconferência simples que permite a comunicação de vídeo, áudio e texto entre vários participantes simultâneos. A ferramenta foi desenvolvida em Python 3 e utiliza a biblioteca 0MQ para comunicação assíncrona entre os participantes.

## Instalação

Antes de executar o programa, certifique-se de ter todas as dependências instaladas. Para instalar as dependências, execute o seguinte comando no terminal:
```python
pip install -r requirements.txt
```
Esse comando irá instalar todas as bibliotecas necessárias listadas no arquivo requirements.txt.

## Uso

Para iniciar a videoconferência, execute o seguinte comando no terminal:
```python
python -m src.__init__
```
Isso iniciará o programa e você será solicitado a inserir o número de participantes desejado e os endereços IP dos participantes. Certifique-se de que todos os participantes estejam na mesma rede para que possam se conectar corretamente.

Durante a videoconferência, você terá a opção de compartilhar vídeo, áudio e também trocar mensagens de texto com os participantes. Siga as instruções apresentadas na interface do programa para utilizar esses recursos.

Para encerrar a videoconferência, pressione a tecla "q" na janela de vídeo ou pressione Ctrl+C no terminal onde o programa está sendo executado.

## Funcionamento

A ferramenta utiliza a biblioteca 0MQ para comunicação entre os participantes. Os participantes se conectam uns aos outros utilizando o modelo PUB/SUB do 0MQ, o que permite a troca de mensagens de forma assíncrona.

A comunicação de vídeo é realizada através do OpenCV, que captura os frames de vídeo da câmera e os envia aos participantes através dos sockets PUB. Os participantes recebem os frames de vídeo e os exibem em uma janela utilizando o OpenCV.

A comunicação de áudio é realizada utilizando a biblioteca SoundDevice, que captura o áudio do microfone e o envia aos participantes através dos sockets PUB. Os participantes recebem o áudio e reproduzem o som utilizando o SoundDevice.

A comunicação de texto é realizada através dos sockets PUB/SUB, onde as mensagens de texto são enviadas e recebidas pelos participantes.
