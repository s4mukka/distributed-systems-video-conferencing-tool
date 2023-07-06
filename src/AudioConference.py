from .Conference import Conference
import cv2
import numpy as np
# import base64
import zmq
import pyaudio

class AudioConference(Conference):
    def __init__(self, port, friends):
        super().__init__(port, friends)
        self.audio_chunk_size = 1024  # Tamanho do chunk de áudio
        self.audio_format = pyaudio.paInt16  # Formato de áudio
        self.audio_channels = 1  # Número de canais de áudio
        self.audio_sample_rate = 44100  # Taxa de amostragem de áudio
        self.audio_buffer = []

    def send(self):
      audio_stream = self.init_audio_stream()

      while audio_stream.is_active():
        audio_data = audio_stream.read(self.audio_chunk_size)
        audio_stream.write(audio_data)
        self.send_socket.send(audio_data)

    def receive(self):
      audio_stream = self.init_audio_stream()

      while True:
        for receive_socket in self.receive_sockets:
          audio_data = receive_socket.recv()
          audio_stream.write(audio_data)

    def init_audio_stream(self):
        p = pyaudio.PyAudio()
        audio_stream = p.open(
            # input_device_index=0,
            # output_device_index=0,
            format=self.audio_format,
            channels=self.audio_channels,
            rate=self.audio_sample_rate,
            output=True
        )
        return audio_stream
