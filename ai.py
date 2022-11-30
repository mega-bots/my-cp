import time
import speech_recognition as sr
from google_speech import Speech as gs
import pocketsphinx
from os import system as s
r = sr.Recognizer()

def spell(text):
        gs(text,"en").play()
def main(text):
        if 'hi' in text:
                spell("hello sir, what is your name")
        if "name" in text:
                spell(f"nice to meet you {text.split()[-1]}")
        if text.lower()=='open google':
                s('google-chrome &')
        if text.lower()=='open codechef':
                s('google-chrome "https://www.codechef.com" &')
        if text.lower()=='open youtube':
                s('google-chrome "https://www.youtube.com" &')
        if text.lower() == 'open whatsapp':
                s('google-chrome "https://web.whatsapp.com/" &')


r.energy_threshold = 100

#print(dir(r.recognize_google))
def listen():
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    try:
          print("Listening")
          audio_text = r.listen(source)
          print("Command Taken")
          text =r.recognize_google(audio_text)
          print("Text: "+text)
          main(text)
    except:
         print("Sorry, I did not get that")

while(1):
  listen()
