from time import sleep
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import random


chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--mute-audio")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("disable-infobars")
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled') 

PATH = "C:\Program Files (x86)\chromedriver.exe"
URL = 'https://www.youtube.com/watch?v=oaKAdhKR4x8'


driver = webdriver.Chrome(PATH, chrome_options=chrome_options) 

additionalTime = 40 + random.randint(1, 9) 

# print(additionalTime)
def sleepNow():
    sleep(additionalTime) 
    # pass

def increaseViewCount():
    driver.get(URL)
    driver.maximize_window() 
    driver.find_element_by_class_name('ytp-large-play-button').click() 

    
def viewBot():
        increaseViewCount()
        while (True) :
            time.sleep(additionalTime)
            driver.refresh() 


viewBot() 