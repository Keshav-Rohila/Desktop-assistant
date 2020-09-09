import datetime
import speech_recognition as sr
import pyttsx3
import socket
import wikipedia

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
    text = text.replace(n, "")
    text = text.replace("open", "")
    text = text.replace("search", "")
    text = text.replace("on google", "")
    text = text.replace("in chrome","")
    text = text.replace("in google", "")
    text = text.replace("search for", "")
    text = text.replace("google search", "")
    text = text.replace("wikipedia","")
    text = text.replace("tell me about", "")
    text = text.replace("who is", "")
    text = text.replace("what is","")
    text = text.replace("search on wikipedia", "")
    text = text.strip()

    return text



def time():
    time = datetime.datetime.now()
    time = time.strftime("%A  %I:%M %p" )
    return time

def date():
    date = datetime.datetime.today()
    date = date.strftime("%d %B,%Y")
    return date

def check_on_wikipedia(query):
    if check_internet_connection() == True:
        try:
            message = wikipedia.summary(query, sentences = 2)
        except:
            message = "Sorry Wikipedia has no information about this."

        return message
    else:
        message = "Not connected to internet please check your connection"
        return message
