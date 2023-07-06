#Função principal onde todos os códigos são instanciadaods

import os
import sys
from dotenv import load_dotenv
from pathlib import Path

#importação dos códigos responsáveis pelo texto, video e audio

from .TextConference import TextConference
from .VideoConference import VideoConference
from .AudioConference import AudioConference

DOTENV_PATH = Path(__file__).resolve().parent / '..' / '.env'
load_dotenv(dotenv_path=DOTENV_PATH)

DEBUG = False

#condição para instanciar as portas onde o texto, video e audio irão se comunicar, junto 
#com os IPs que serão adicionados na comunicação

if __name__ == '__main__':
    TEXT_PORT = int(os.getenv('TEXT_PORT'))
    VIDEO_PORT = int(os.getenv('VIDEO_PORT'))
    AUDIO_PORT = int(os.getenv('AUDIO_PORT'))
    ADDRESS_FRIENDS = os.getenv('ADDRESS_FRIENDS')
    member=None
    if DEBUG:
        member = int(sys.argv[1])
        ADDRESS_FRIENDS = '127.0.0.1'
    friends = ADDRESS_FRIENDS.split(',')

    #chamada da comnunicação via texto

    text_conference = TextConference(port=TEXT_PORT, friends=friends, member=member)
    text_conference.start()

    #chamada da comnunicação via vídeo

    video_conference = VideoConference(port=VIDEO_PORT, friends=friends, member=member)
    video_conference.start()

    #chamada da comnunicação via audio

    audio_conference = AudioConference(port=AUDIO_PORT, friends=friends, member=member)
    audio_conference.start()

#em cada chamada, podemos observar que o parâmetro da função é a porta da comunicação, o ip responsável e o
#membro