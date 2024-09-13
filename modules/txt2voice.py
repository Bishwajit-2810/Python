import pyttsx3
import pyjokes

jokes =pyjokes.get_joke()

engine =pyttsx3.init()
engine.setProperty('rate', 120)
engine.say(jokes)
engine.runAndWait()
