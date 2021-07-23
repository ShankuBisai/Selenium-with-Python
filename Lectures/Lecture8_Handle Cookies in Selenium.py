from Lecture2_WebDriverManager_CrossBrowser import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class Cookies:

    def __init__(self):
        self.driver = WebDriverManager.webDriverManager("chrome")


    def invokeWebSite(self):
        self.driver.get("https://www.reddit.com/")

    def getCookies(self):
        cookies=self.driver.get_cookies()
        for cookie in cookies:
            print(cookie)


object = Cookies()
object.invokeWebSite()
object.getCookies()