import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import pyaudio
import requests
import time
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
# 1 = Female Voice
# 0 = Male Voice

def speak(audio):
    '''speak output'''
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Friday. What can I do for you.")       

def joke():
	'''joke function'''
    res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
    if res.status_code == requests.codes.ok:
            speak('Here is an awesome joke for you- ')
            speak(str(res.json()['joke']))
    else:
        speak('oops!I ran out of jokes')

def playgame():
	'''game function'''
    speak('Tell me which game should open on web')
    query = takeCommand().lower()
    if 'power line' in query:
        webbrowser.open("powerline.io")
        
    elif 'gartic' in query:
		    webbrowser.open("gartic.io")
    elif 'slither' in query:
            webbrowser.open("slither.io")
    elif 'hexar' in query:
            webbrowser.open("hexar.io")    
    
    else:
        speak('Sorry sir i am facing some issue')


def areminder():
	'''set a remainder function'''
    speak("What shall I remind you about?")
    text = str(takeCommand())
    speak("In how many minutes?")
    local_time = float(takeCommand())
    local_time = local_time * 60
    time.sleep(local_time)
    speak(text)

def takeCommand():
	'''takes voice commands from the user'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Please repeat...")  
        return "None"
    return query

def sendEmail(to, content):
	'''send mail function'''
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.login('youremail@gmail.com', 'your-password')
     server.sendmail('youremail@gmail.com', to, content)
     server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
      

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        
        elif 'tell me a joke' in query:
             joke()
       
        elif 'open game' in query:
             playgame()
        
        elif 'reminder' in query:
             areminder()

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir could not complete the task.")    
       
        elif 'Friday shutdown' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
