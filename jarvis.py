import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis sir. Please teell me sir how can I help u")

def takeCommand():
    # It takes microphone input from user and return string output
    # r= sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     r.pause_threshold=1
    #     audio=r.listen(source)
        
    # try:
    #     print("Recognizing...")
    #     query=r.recognize_google_cloud(audio,language='en-in')
    #     print(f"User said: {query}\n")
        
    # except Exception as e:
    #     # print(e)
    #     print("Say again please...")
    #     return "None"
    
    # return query

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        print("Say that again, please.")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
    
        #Logic for executing task based on query
        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open telegram' in query:
            webbrowser.open("https://web.telegram.org/k/#-4051548285")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'play music' in query:
            music_dir='E:\\music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
            
        elif 'open vs code' in query:
            codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
                    
        
