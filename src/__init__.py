import os
import sys
from dotenv import load_dotenv
from pathlib import Path

from .TextConference import TextConference
from .VideoConference import VideoConference
from .AudioConference import AudioConference

DOTENV_PATH = Path(__file__).resolve().parent / '..' / '.env'
load_dotenv(dotenv_path=DOTENV_PATH)

DEBUG = False

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
    text_conference = TextConference(port=TEXT_PORT, friends=friends, member=member)
    text_conference.start()
    video_conference = VideoConference(port=VIDEO_PORT, friends=friends, member=member)
    video_conference.start()
    audio_conference = AudioConference(port=AUDIO_PORT, friends=friends, member=member)
    audio_conference.start()
