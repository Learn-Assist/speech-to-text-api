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
    @property
    def text(self,dest):
        AUDIO_FILE = dest
        with AudioFile(AUDIO_FILE) as source:
            audio = self.recognizer.record(source)
        try:
            text = self.recognizer.recognize_google(audio, language='RU')
            return text
        except UnknownValueError:
            print("Error msg1")
        except RequestError as error:
            print("Error msg2: {0}".format(error))
