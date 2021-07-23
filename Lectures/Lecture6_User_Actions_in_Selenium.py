from Lecture2_WebDriverManager_CrossBrowser import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class UserActions:

    def __init__(self):
        self.driver = WebDriverManager.webDriverManager("chrome")

    def invokeWebSite(self):
        self.driver.get("https://www.spicejet.com/")

    def moveToElement(self,**args):
        for x in args:
            print(args[x])
            actions = ActionChains(self.driver)
            actions.move_to_element(self.driver.find_element(By.XPATH,args[x])).perform()


object = UserActions()
object.invokeWebSite()
object.moveToElement(firstElement="//a[@id='ctl00_HyperLinkLogin']",secondElement="//a[text()='SpiceClub Members']",thirdElement="//*[@id='smoothmenu1']/ul/li[10]/ul/li[2]/ul")
