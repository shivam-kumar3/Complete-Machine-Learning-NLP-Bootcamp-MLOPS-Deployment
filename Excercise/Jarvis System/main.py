import speech_recognition as sr
import pyttsx3
import logging
import os

# Logger for the application
LOG_DIR = 'logs'
LOG_FILE_NAME = 'application.log'

if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format= '[%(asctime)s] %(name)s %(levelname)s %(message)s',
    level = logging.INFO
)

# taking the male voice from my system

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speak function
def Speak(text):
    engine.say(text)
    engine.runAndWait()

Speak("Hello my name is shivam\n i am a data scientist")


# taking commands

def takecommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language = 'en-in')
        print(f'User Said:{query}\n')
    except Exception as e:
        logging.info(e)
        print("Say that again please")
        return None
    return query

text = takecommands()
print(text)