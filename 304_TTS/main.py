from gtts import gTTS
language = "en"
text = "Hello world, I am a sentient machine!"

speech = gTTS(text=text, lang=language, slow=False, tld="com.au") # us
speech.save("textToSpeech.mp3")