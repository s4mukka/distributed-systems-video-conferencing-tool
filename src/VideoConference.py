from .Conference import Conference
import cv2
import numpy as np
import zmq

class VideoConference(Conference):
    def send(self):
      video_capture = cv2.VideoCapture(0)
      while video_capture.isOpened():
        ret, frame = video_capture.read()
        if ret:
            # Redimensiona o frame, se necessário
            frame = cv2.resize(frame, (640, 480))
            # cv2.imshow("vid", frame)

            # Envia o frame como uma imagem JPEG
            self.send_socket.send_string(frame.tobytes())

    def receive(self):
      while True:
        for receive_socket in self.receive_sockets:
          frame_bytes = receive_socket.recv()
          frame = np.frombuffer(frame_bytes, dtype=np.uint8)
          frame = np.reshape(frame, (640, 480, 3))  # Restaura as dimensões do frame
          # Código para exibir o frame recebido
          cv2.imshow(self.getsockopt(zmq.LAST_ENDPOINT).decode(), frame)
          if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
              break