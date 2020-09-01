import datetime
import speech_recognition as sr
import pyttsx3
import socket

name = "Jarvis"

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12 or hour == 24:
        wish = "Good Morning"
    elif hour >= 12 and hour < 16:
        wish = "Good Afternoon"
    else:
        wish = "Good Evening"

    speak(wish)
    


def takeCommand(input_method):
    if input_method == "v":
        r = sr.Recognizer()

        with sr.Microphone() as sourse:
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 325
            audio = r.listen(sourse)

            try:
                command = r.recognize_google(audio, language='en-in')
                print("You: {}".format(command))

            except:
                speak("Couldn't recognize your voice please type your message")
                command = input("You : ")

    elif input_method == "t":
        speak("Type your message")
        command = input("You : ")


    return command


def speak(text):
    engine = pyttsx3.init()

    rate = engine.getProperty("rate")
    engine.setProperty("rate", 120)

    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[0].id)

    print(name + ": ",text)

    engine.say(text)
    engine.runAndWait()


def check_internet_connection():
    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        return False
    else:
        return True


def filter_string(text):
    n = name.lower()
    if n in text:
        text = text.replace(n," ")
        text = text.strip()
    if "open" in text:
        text = text.replace("open", " ")
        text = text.strip()
        if "on google" in text:
            text = text.replace("on google", " ")
            text = text.strip()
            return text
        elif "in google" in text:
            text = text.replace("in google", " ")
            text = text.strip()
        return text
        
    if "search" in text:
        text = text.replace("search", " ")
        text = text.strip()
        if "for" in text:
            text = text.replace("for"," ")
            text = text.strip()
        if "on google" in text:
            text =  text.replace("on google", " ")
            text = text.strip()
            return text
        elif "in google" in text:
            text = text.replace("in google", " ")
            text = text.strip()
        return text
    if "google search" in text:
        text = text.replace("google search", " ")
        text = text.strip()
        return text


