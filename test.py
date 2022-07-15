
import os
import playsound
import speech_recognition as sr
from gtts import gTTS




def speak(text):
    tts = gTTS(text=text, lang="hi") 
    Name = "voice"
    filename = Name + ".mp3"   
    tts.save(filename)
    playsound.playsound(filename)
    

   
    

speak("Hello, I am there to help you")
os.remove('voice.mp3')

speak("Important")



