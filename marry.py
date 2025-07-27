import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    else:
        speak("I am Merry, your personal AI assistant")
        speak("What do you want me to do?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print("You: (query)\n")

    except Exception as e:
        print(e)
        print("Sorry, please say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "who the heck is" in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'date' in query:
            speak('sorry, I have a headache')
            
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%H:%M %p')
            print(time)
            speak('Current time is' + time)

        elif 'open youtube' in query:
            webbrowser.open("https:\\www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https:\\www.google.com")
            
        elif 'are you single' in query:
            speak('I am in a relationship with Bentong')

        elif 'Play a music' in query:
            music_dir = 'E:\\Music'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[3]))
            
while True:
    run_merry()
            
        