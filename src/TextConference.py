from .Conference import Conference
import zmq

class TextConference(Conference):
    def send(self):
      while True:
        message = input("Digite uma mensagem: ")
        self.send_socket.send_string(message)

    def receive(self):
      for friend in self.friends:
        self.receive_socket.connect(f"tcp://{friend}:{self.port}")
        self.receive_socket.setsockopt_string(zmq.SUBSCRIBE, "")

        while True:
            message = self.receive_socket.recv_string()
            print("Mensagem recebida:", message)