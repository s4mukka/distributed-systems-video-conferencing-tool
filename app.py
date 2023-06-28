import cv2
import zmq
import threading
import numpy as np

# Função para enviar o vídeo em um thread separado
def send_video():
    context = zmq.Context()
    video_socket = context.socket(zmq.PUB)
    video_socket.bind("tcp://*:5555")

    video_capture = cv2.VideoCapture(0)  # Captura o vídeo da webcam
    print(video_capture.isOpened())
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if ret:
            # Redimensiona o frame, se necessário
            frame = cv2.resize(frame, (640, 480))
            cv2.imshow("vid", frame)

            # Envia o frame como uma imagem JPEG
            video_socket.send(frame.tobytes())

            if cv2.waitKey(1) & 0xFF == ord('q'):
              break

# Função para enviar o áudio em um thread separado
def send_audio():
    context = zmq.Context()
    audio_socket = context.socket(zmq.PUB)
    audio_socket.bind("tcp://*:5556")

    # Código para capturar e enviar áudio

# Função para receber o vídeo em um thread separado
def receive_video():
    context = zmq.Context()
    video_socket = context.socket(zmq.SUB)
    video_socket.connect("tcp://localhost:5555")
    video_socket.setsockopt_string(zmq.SUBSCRIBE, "")

    while True:
        frame_bytes = video_socket.recv()
        frame = np.frombuffer(frame_bytes, dtype=np.uint8)
        frame = np.reshape(frame, (640, 480, 3))  # Restaura as dimensões do frame
        # Código para exibir o frame recebido
        # cv2.imshow("Video", frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
        #     break
    cv2.destroyAllWindows()

# Função para receber o áudio em um thread separado
def receive_audio():
    context = zmq.Context()
    audio_socket = context.socket(zmq.SUB)
    audio_socket.connect("tcp://localhost:5556")
    audio_socket.setsockopt_string(zmq.SUBSCRIBE, "")

    # Código para reproduzir o áudio recebido

# Inicia os threads para envio e recebimento de vídeo e áudio
video_thread = threading.Thread(target=send_video)
audio_thread = threading.Thread(target=send_audio)
video_thread.start()
audio_thread.start()

receive_video()
receive_audio()
