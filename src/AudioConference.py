#código responsável pela interface de audio da stream

from .Conference import Conference
import base64
import sounddevice as sd
import numpy as np

class AudioConference(Conference):
    def send(self):
      audio_stream = sd.InputStream(
        channels=1,
        samplerate=44100,
        dtype='float32'
      )
      audio_stream.start()
      while audio_stream.active:
        audio_data, _ = audio_stream.read(1024)
        self.send_socket.send(base64.b64encode(audio_data.tobytes()))

    def receive(self):
      audio_stream = sd.OutputStream(
        channels=1,
        samplerate=44100
      )

      audio_stream.start()
      while True:
        for receive_socket in self.receive_sockets:
          audio_data_bytes = receive_socket.recv()
          audio_data = np.frombuffer(base64.b64decode(audio_data_bytes), dtype='float32')
          audio_stream.write(audio_data)

