#código responsável pela interface de texto da stream
from .Conference import Conference
import zmq

class TextConference(Conference):
    def send(self):
      while True:
        message = input("Digite uma mensagem: \n")
        self.send_socket.send_string(message)

    def receive(self):
      while True:
        for receive_socket in self.receive_sockets:
          message = receive_socket.recv_string()
          print(f"Mensagem recebida {(receive_socket.getsockopt(zmq.LAST_ENDPOINT).decode())}:", message)