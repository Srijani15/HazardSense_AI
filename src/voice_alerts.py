import pyttsx3

def speak_warnings(hazards):
    """
    hazards: list of tuples (message, score)
    """
    engine = pyttsx3.init()
    for message, score in hazards:
        engine.say(message)
    engine.runAndWait()
