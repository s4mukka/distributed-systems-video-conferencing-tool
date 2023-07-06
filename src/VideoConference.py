#código responsável pela interface de vídeo da stream

from .Conference import Conference
import cv2
import numpy as np
import base64
import zmq

class VideoConference(Conference):
    def send(self):
      video_capture = cv2.VideoCapture(0)
      while video_capture.isOpened():
        ret, frame = video_capture.read()
        if ret:
            # Redimensiona o frame, se necessário
            frame = cv2.resize(frame, (640, 480))
            encoded, buffer = cv2.imencode('.jpg', frame)
            # cv2.imshow("vid", frame)

            # Envia o frame como uma imagem JPEG
            self.send_socket.send(base64.b64encode(buffer))

    def receive(self):
      while True:
        for receive_socket in self.receive_sockets:
          frame = receive_socket.recv()
          img = cv2.imdecode(np.fromstring(base64.b64decode(frame), dtype=np.uint8), 1)
          # Código para exibir o frame recebido
          cv2.imshow(receive_socket.getsockopt(zmq.LAST_ENDPOINT).decode(), img)
          if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
              break