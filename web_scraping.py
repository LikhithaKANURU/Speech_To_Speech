from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Infow:
    def __init__(self):
        chrome_options = Options()
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()
