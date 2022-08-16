# text to speech conversion in python
from datetime import datetime
import pyttsx3
# sppech recognition
import speech_recognition as sr
import datetime
import os
import cv2
import time

engine = pyttsx3.init('sapi5')
# getting the voice for text to speech conversion
voices = engine.getProperty('voices')
# voice with 0 id is the david's voice and i can change it by changing the id
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 150)
# engine.setProperty('language', 'hi-In')

# text to speech


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# take command


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 3
        audio = r.listen(source,  phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-In')
        # print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query

# greetings


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("goodmorning boss")
    elif hour > 12 and hour <= 16:
        speak("good afternoon boss")
    # elif hour <= 20:
    #     speak("Good Evening! Boss")
    else:
        speak("good evening boss")
    speak("i am jarvis. how may i help you?")


if __name__ == "__main__":
    # takecommand()
    wish()
    goOn = True
    while goOn:
        # if 1:
        query = takecommand().lower()

        # logic building for tasks
        if "open notepad" in query:
            speak("opening notepad")
            npath = "C:\\Users\\Bhendi-Bazaar.Com\\Desktop\\burhan's stuff\\my secrets.txt"
            mySecrets = os.startfile(npath)
        elif "open command prompt" in query:
            speak("opening command prompt")
            os.system("start cmd")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            speak("opening camera")
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "exit" in query:
            break
        else:
            speak("is there anything else i can do?")
