import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes
import pyautogui
import sys
import os
import random
import pywhatkit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

todo_list = ['Go Shopping', 'Clean Room']
hello =  ["hi", "how are you", "hai", "hello", "Good day", "what's up", "hey", "greetings"]
gr_resp = ["Hello!", "Good to see you again!", "Hi there, how can I help?"]    
exit=["cya", "See you later", "Goodbye", "I am Leaving", "bye", "cao", "see ya","Bye","bhai","exit","quit","I want to exit"]
exit_resp=["Sad to see you go :(", "Talk to you later", "Goodbye!"]
note=["new note", "create an note"]
todo=["add a new todo", "add a new todo to my list"]
show_todos=["show my todo","what are my todo"]

def input_query():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('recognition is on....')
        recognizer.pause_threshold = 0.7
        voice = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(voice).lower()
            print('this is the query that was made....', query)
            return query
        except Exception as ex:
            print('An exception occurred', ex)


def report_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    return current_time


def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()

def create_note():
  recognizer = sr.Recognizer()
  speak_va("What do you want to write as note?")
  done = False
  while not done:
        try:
            with sr.Microphone() as source:
                
                recognizer.pause_threshold = 0.7
                voice = recognizer.listen(source)

                note = recognizer.recognize_google(voice).lower()


                speak_va("Choose a file name")
                

                recognizer.pause_threshold = 0.7
                voice = recognizer.listen(source)

                filename = recognizer.recognize_google(voice).lower()

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speak_va(f"created the note")
                
        except sr.UnknownValueError:
                recognizer=sr.Recognizer()
                speak_va("I did not get it")
                

def add_todo():
    recognizer = sr.Recognizer()
    speak_va("What do you want add")
    done = False

    while not done:
        try:

            with sr.Microphone() as source:
                recognizer.pause_threshold = 0.7
                voice = recognizer.listen(source)

                item = recognizer.recognize_google(voice).lower()

                todo_list.append(item)
                done = True

                speak_va(item+" was added to the list!")
                 

        except sr.UnknownValueError:
            speak_va("I'm sorry, can you repeat it again!")
             



def show_todos():

    speak_va("list is")
    for item in todo_list:
        print(item+"\n")
        speak_va(item)

def quit():
    speak_va(random.choice(exit_resp))
    sys.exit(0)  


def activate_va():
    user_query = input_query()
    print('user query ....', user_query)
    if user_query in hello:
        speak_va(random.choice(gr_resp))
    elif 'time' in user_query:
        current_time = report_time()
        print(f"the current time is {current_time}")
        speak_va(f"the current time is {current_time}")
    elif 'open' in user_query: 
        user_query = user_query.replace('open', '')
        user_query = user_query.replace(' ', '')
        print('https://www.'+user_query+'.com/')
        webbrowser.open('https://www.'+user_query+'.com/')
        speak_va(f"{user_query} opened.")
    elif 'wikipedia' in user_query:
        speak_va("Searching on Wikipedia")
        user_query = user_query.replace('wikipedia', ' ')
        result = wikipedia.summary(user_query, sentences=2)
        print(result)
        speak_va(result)
    elif 'joke' in user_query:
        random_joke = pyjokes.get_joke()
        print(random_joke)
        speak_va(random_joke)
    elif 'screenshot' in user_query:
        image = pyautogui.screenshot()
        image.save('screenshot.png')
        speak_va('Screenshot taken.')
    elif 'search' in user_query:
        user_query = user_query.replace('search', ' ')
        search_url = f"https://www.google.com/search?q={user_query}"
        webbrowser.open(search_url)
        speak_va(f"here are the results for the search term: {user_query}")
    elif user_query in note:
        create_note()
    elif user_query in todo:
        add_todo()
    elif user_query in exit:
        quit()
    elif "play" in user_query:
        user_query = user_query.replace('play', ' ')
        pywhatkit.playonyt(user_query)
    else :
        pywhatkit.info(user_query,lines=2)
        speak_va(f"here are the results for the search term: {user_query}")

      
while True:
    activate_va()