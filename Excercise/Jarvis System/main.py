import speech_recognition as sr
import pyttsx3

# taking the male voice from my system

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

# speak function
def Speak(text):
    engine.say(text)
    engine.runAndWait()

Speak("Hello my name is shivam\n i am a data scientist")


# taking commands

def takecommands():
    r = sr.recognizers()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.litsen(source)

    try:
        pass
    except Exception as ex:
        
        