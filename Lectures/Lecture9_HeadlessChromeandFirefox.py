from Lecture2_WebDriverManager_CrossBrowser import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class Headless:

    def __init__(self):
        self.driver = WebDriverManager.webDriverManager(browser="firefox",headless="true")

    def invokeWebSite(self):
        self.driver.get("https://www.google.com/")
        print(self.driver.title)


object = Headless()
object.invokeWebSite()