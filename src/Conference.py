#código responsável por chamar a comunição Pub / Subscribe

from abc import ABC, abstractmethod
import zmq
from threading import Thread 


#Super classe responsável por instanciar todos os parâmretros de comunicação
class Conference(ABC):
    
    #função responsável por instanciar todos os parâmetros de comunicação de pub/sub por meio de zmq
    def __init__(self, port, friends, member):
        self.port = port
        if member == 1:
          self.port = self.port + 1000
        elif member == 2:
          port = port + 1000
        self.send_context = zmq.Context()
        self.send_socket = self.send_context.socket(zmq.PUB)
        self.send_socket.bind(f"tcp://*:{port}")
        self.receive_context = zmq.Context()
        self.friends = friends
        self.receive_sockets = []
        for friend in self.friends:
          receive_socket = self.receive_context.socket(zmq.SUB)
          receive_socket.connect(f"tcp://{friend}:{self.port}")
          receive_socket.setsockopt_string(zmq.SUBSCRIBE, "")
          self.receive_sockets.append(receive_socket)

    def start(self):
      send_thread = Thread(target=self.send)
      receive_thread = Thread(target=self.receive)
      send_thread.start()
      receive_thread.start()

    @abstractmethod
    def send(self):
      pass

    @abstractmethod
    def receive(self):
      pass