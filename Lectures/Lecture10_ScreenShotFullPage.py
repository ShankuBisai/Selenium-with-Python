from Lecture2_WebDriverManager_CrossBrowser import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class ScreenShot:

    def __init__(self):
        self.driver = WebDriverManager.webDriverManager(browser="firefox",headless="true")

    def invokeWebSite(self):
        self.driver.get("https://www.reddit.com/")
        print(self.driver.title)

    def takeScreenShot(self):
        self.driver.save_screenshot("reddit.png")
        self.driver.get_screenshot_as_png("reddit1.png")

    def takeScreenShotFull(self):
        """
        This function takes the screenshot of the webpage
        the browser should be in headless mode for that
        :return:
        """
        S = lambda X:self.driver.execute_script('return document.body.parentNode.scroll' +X)
        self.driver.set_window_size(S("Width"),S("Height"))
        self.driver.find_element(By.TAG_NAME,"body").screenshot("reddit_fullImage.png")


object = ScreenShot()
object.invokeWebSite()
object.takeScreenShot()
object.takeScreenShotFull()