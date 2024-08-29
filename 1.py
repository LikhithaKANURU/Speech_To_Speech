import pyttsx3 as p
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Define the Infow class
class Infow:
    def __init__(self):
        # Set up the ChromeDriver service and options
        chrome_options = Options()
        service = Service(ChromeDriverManager().install())

        # Initialize the WebDriver
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def get_info(self, query):
        self.query = query
        # Load the Wikipedia homepage
        self.driver.get("https://www.wikipedia.org")
        # Find the search input element and enter the query
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        # Find the search button and click it
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()

# Initialize the text-to-speech engine
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 120)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use the correct voice property

def speek(text):
    engine.say(text)
    engine.runAndWait()

# Initialize the recognizer
r = sr.Recognizer()

speek("Hello Madam I am your voice assistant. How are you?")
# Use the microphone as a source (note the parentheses after Microphone)
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, duration=1.2)
    print("Listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" in text and "about" in text and "you" in text:
    speek("I am also having a good day Madam")

speek("What can I do for you Madam?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speek("You need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speek("Searching in Wikipedia ".format(infor))
    assist = Infow()
    assist.get_info(infor)
