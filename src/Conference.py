from abc import ABC, abstractmethod
import zmq
from threading import Thread 

class Conference(ABC):
    def __init__(self, port, friends):
        self.port = port
        self.send_context = zmq.Context()
        self.send_socket = self.send_context.socket(zmq.PUB)
        self.send_socket.bind(f"tcp://*:{port}")
        self.receive_context = zmq.Context()
        self.receive_socket = self.receive_context.socket(zmq.SUB)
        self.friends = friends

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