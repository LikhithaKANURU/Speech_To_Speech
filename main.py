# main.py
from text_to_speech import TextToSpeech
from speech_recognition_module import SpeechRecognizer
from web_scraping import Infow

def main():
    tts = TextToSpeech()
    recognizer = SpeechRecognizer()

    tts.speak("Hello Madam, I am your voice assistant. How are you?")
    text = recognizer.listen_for_command()

    if "what" in text and "about" in text and "you" in text:
        tts.speak("I am also having a good day Madam")

    tts.speak("What can I do for you Madam?")
    text2 = recognizer.listen_for_command()

    if "information" in text2:
        tts.speak("You need information related to which topic?")
        infor = recognizer.listen_for_command()
        if infor:
            tts.speak(f"Searching in Wikipedia for {infor}")
            assist = Infow()
            assist.get_info(infor)

if __name__ == "__main__":
    main()
