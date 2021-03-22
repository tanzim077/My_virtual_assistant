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
import os

warnings.filterwarnings('ignore')

#  Function for record audio and convert it to string

def recordAudio ():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening .....')
        audio = r.listen(source, timeout=5)

        data = ''
        try:
            # data = r.recognize_google(audio)      # This is for default English language
            data = r.recognize_google(audio, language= "bn-BD") # This is for Bengali language
            print('You said ' + '"' + data + '"')
        except sr.UnknownValueError:
            print('There is an unknown error')
        except sr.RequestError:
            print('Service error')

        return data

# recordAudio()

def assistantrRespnse(text):
    print(text)
    myobj = gTTS(text=text, lang='en', slow=False)
    # myobj = gTTS(text=text, lang='fr', slow=False) # Unfortunately Bengali not supported in gTTS 'lang'
    myobj.save('Assistant_response.mp3')
    os.system('start Assistant_response.mp3')

# text = 'This is a test'
# text = "আমার সোনার বাংলা "
# assistantrRespnse(text)

def wakeWords(text):
    WAKE_WORDS = ['hey pc', 'hey system']
    text = text.lower()
    for item in WAKE_WORDS:
        if item in text:
            return True
    return False

def getDate():
    now = datetime.datetime.now()
    today = datetime.datetime.today()
    weekday = calendar.day_name[today.weekday()]
    monthNum = now.month
    dayNum = now.day

    months_name = ['January', 'February','March', 'April','May','June', 'July','August',
                   'September','October','November','December']
    ordinal_numbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th',
                       '11th','12th','13th','14th','15th','16th','17th','18th','19th','20th',
                       '21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th' '31st']
    return 'Today is ' + weekday + ' ' + months_name[monthNum - 1] + ' ' + 'the' + ' ' + ordinal_numbers[dayNum-1] + '.'

# print(getDate())

def gretting(text):
    GREETING_INPUTS = ['Hey', 'Hello', 'Hola', 'Whats Up', 'Hey Welcome']
    GREETING_RESPONSE = ['howdy', 'What\'s good', 'hello too', 'thanks']

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSE) +'.'

        return '...'
# Need to customize more
def getPerson(text):
    wordlist = text.split()

    for i in range(0, len(wordlist)):
        if i + 3 <= len(wordlist) - 1 and wordlist[i].lower() == 'who' and wordlist[i + 1].lower() == 'is':
            return wordlist[i +2] + ' ' + wordlist[i+3]