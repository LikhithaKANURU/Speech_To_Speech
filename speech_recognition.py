import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_for_command(self):
        with sr.Microphone() as source:
            self.recognizer.energy_threshold = 10000
            self.recognizer.adjust_for_ambient_noise(source, duration=1.2)
            print("Listening...")
            try:
                audio = self.recognizer.listen(source)
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                return ""
            except sr.RequestError:
                print("Sorry, there was an error with the speech recognition service.")
                return ""
