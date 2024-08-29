import pyttsx3 as p

class TextToSpeech:
    def __init__(self):
        self.engine = p.init()
        self.engine.setProperty('rate', 120)  # Speed of speech (words per minute)
        self.engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
        voices = self.engine.getProperty('voices')
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)  # Set the second voice in the list
        else:
            print("Less than 2 voices available. Default voice will be used.")

    def speak(self, text):
        """Convert text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()
