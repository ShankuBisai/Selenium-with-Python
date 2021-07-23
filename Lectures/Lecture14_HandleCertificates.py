from Lecture2_WebDriverManager_CrossBrowser import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class Certificates:

    def __init__(self):
        self.driver = WebDriverManager.webDriverManager(browser="chrome",headless="false")

    def invokeWebSite(self):
        self.driver.get("https://expired.badssl.com/")



object =Certificates()
object.invokeWebSite()