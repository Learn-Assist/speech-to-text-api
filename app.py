from flask import Flask
from flask import request, make_response
from flask_cors import CORS
import speech_recognition as sr
from  OGGtoWAV import SpeechOggAudioFileToText 
import helper_functions as hf
import subprocess
app = Flask(__name__)
r = sr.Recognizer()
CORS(app)



@app.route('/')
def index():
    print("Get home")
    return 'Hello from LearnAssist text to speech API!'

@app.route('/exec', methods=['POST'])
def route_exec():
    print("route_exec")
    command = request.data.decode('utf-8')
    try:
        completedProcess = subprocess.run(command.strip(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=10, universal_newlines=True)
        response = make_response(completedProcess.stdout, 200)
        response.mimetype = "text/plain"
        return response
    except subprocess.TimeoutExpired:
        response = make_response("Timedout", 400)
        response.mimetype = "text/plain"
        return response

@app.route('/audio', methods=['POST'])
def speech_to_text():
    result =''
    print('Request received')
    try:
        filename = 'audio/audio{}.ogg'.format(hf.makeId(12))
        with open(filename, 'wb+') as destination:
            destination.write(request.files['file'].stream.read())
        SpeechOggAudioFileToText().ogg_to_wav(filename,filename.replace('.ogg','.wav'))
        with sr.AudioFile(filename.replace('.ogg','.wav')) as source:
            audio_text = r.listen(source)
            text = r.recognize_google(audio_text)
            result = make_response(text,201)
            print("\n\n\nResult: {}\n\n\n".format(text))
    except Exception as e:
        result = make_response(str(e),400)
        print('Sorry.. try again...')
        print(e)
    
    return result

if __name__ == '__main__':
    print('Server started @PORT 3005...')
    app.run(port=3005,host='0.0.0.0')


