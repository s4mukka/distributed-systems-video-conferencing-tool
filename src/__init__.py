import os
from dotenv import load_dotenv
from pathlib import Path

from .TextConference import TextConference
from .VideoConference import VideoConference
from .AudioConference import AudioConference

DOTENV_PATH = Path(__file__).resolve().parent / '..' / '.env'
load_dotenv(dotenv_path=DOTENV_PATH)

if __name__ == '__main__':
    TEXT_PORT = os.getenv('TEXT_PORT')
    VIDEO_PORT = os.getenv('VIDEO_PORT')
    AUDIO_PORT = os.getenv('AUDIO_PORT')
    friends = os.getenv('ADDRESS_FRIENDS').split(',')
    text_conference = TextConference(port=TEXT_PORT, friends=friends)
    text_conference.start()
    video_conference = VideoConference(port=VIDEO_PORT, friends=friends)
    video_conference.start()
    audio_conference = AudioConference(port=AUDIO_PORT, friends=friends)
    audio_conference.start()
