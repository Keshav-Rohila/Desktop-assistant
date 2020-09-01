from functions import *
import webbrowser
import os
import subprocess

if __name__ == "__main__":
    wishMe()
    speak("Press v to give voice input and t for text input")
    input_method = input("You: ").lower()
    while input_method != "v" and input_method != "t":
        speak("Improper input method please enter again")
        input_method = input("You: ").lower()
    speak("Hi I am " + name + " How may I help you")

    while True:
        query = takeCommand(input_method).lower()

        if "open google" in query:
            status = check_internet_connection()
            if status == True:
                chromedir= 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe'
                subprocess.call(chromedir)
            else:
                speak("Not connected to internet please check your connection")

        
        elif "open youtube" in query:
            status = check_internet_connection()
            if status == True:
                chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chromedir).open_new_tab("youtube.com")
            else:
                speak("Not connected to internet please check your connection")

        
        elif "open calculator" in query:
            subprocess.call("calc.exe")

        
        elif "check internet connection" in query:
            status = check_internet_connection()
            if status == True:
                speak("Connected")
            else:
                speak("Not connected")

        
        elif "quit" in query:
            speak("Have a nice time")
            quit()

        
        elif (("open" or "search") and ("on google" or "in google")) or "google search" in query:
            status = check_internet_connection()
            if status == True:
                 message = filter_string(query)
                 chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'                    
                 webbrowser.get(chromedir).open_new_tab("https://www.google.com/search?q={}".format(message))
            else:
                speak("Not connected to internet please check your connection")

        
        else:
            speak("Can't help you with this do you wanna go with the web search")
            need = takeCommand(input_method).lower()
            if "yes" in need:
                status = check_internet_connection()elif "quit" in query:
            speak("Have a nice time")
            quit()
                if status == True:
                    chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'                    
                    webbrowser.get(chromedir).open_new_tab("https://www.google.com/search?q={}".format(query))
                else:
                    speak("Not connected to internet please check your connection")

            elif "no" in need:
                speak("Have a nice time")
                quit()