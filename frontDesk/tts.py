import pyttsx3

def speak(text, speech_flag):
    if speech_flag == True:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
