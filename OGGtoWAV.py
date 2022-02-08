from subprocess import Popen
from speech_recognition import (Recognizer, AudioFile)
from speech_recognition import (UnknownValueError, RequestError)

class SpeechOggAudioFileToText:
    def __init__(self):
        self.recognizer = Recognizer()

    def ogg_to_wav(self, file,dest):
        args = ['ffmpeg','-i', file, dest]
        process = Popen(args)
        process.wait()
   
