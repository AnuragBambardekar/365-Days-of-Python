# pip install pyttsx3

import pyttsx3 

engine = pyttsx3.init() 

engine.say("Hello There!") 
engine.runAndWait() 

# Why pyttsx?
"""
It works offline, unlike other text-to-speech libraries. 
Rather than saving the text as audio file, pyttsx actually speaks it there
"""