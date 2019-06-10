import pyttsx3
import webbrowser
import smtplib
import random
import wikipedia
import datetime
import os
import sys
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am (_your bot_name_)')
speak('How may I help you?')


def myCommand():

     try:
        query = r.recognize_google(query, language='en-in')
        print('User: ' + query + '\n')
        
     except: 
        query = str(input('Command: '))

     return query
        

if __name__ == '__main__':

    while True:
   
        
    
        
        query = str(input('command: '))
        query = myCommand()
        query = query.lower()
        
        if 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('www.google.com') 

        elif 'abort' in query:
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = Your_music_path_or_location
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            
            

        else:
            query = query
            
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                
                    print ('results')
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                   
                    print ('results')
        
            except:
                webbrowser.open('www.instagram.com')
        


        
