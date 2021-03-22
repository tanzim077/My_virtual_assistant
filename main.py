# First run this command in your terminal
    # pip install pyaudio
    # pip install SpeechRecognition
    # pip install gTTS
    # pip install wikipedia


# Import the Libraries
import speech_recognition as sr
import pyaudio
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

warnings.filterwarnings('ignore')

#  Function for record audio and convert it to string

def recordAudio ():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening .....')
        audio = r.listen(source, timeout=5)

        data = ''
        try:
            data = r.recognize_google(audio)      # This is for default English language
            # data = r.recognize_google(audio, language= "bn-BD") # This is for Bengali language
            print('You said ' + '"' + data + '"')
        except sr.UnknownValueError:
            print('There is an unknown error')
        except sr.RequestError:
            print('Service error')

        return data

recordAudio()

