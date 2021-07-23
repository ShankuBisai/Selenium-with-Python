from Lecture2_WebDriverManager_CrossBrowser import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class JavaScript:

    def __init__(self):
        self.driver = WebDriverManager.webDriverManager(browser="chrome",headless="false")

    def invokeWebSite(self):
        self.driver.get("https://www.makemytrip.com/")

    #using javascript
    def clickElement(self):
        element=self.driver.find_element(By.XPATH,"//li[text()='Student Fare']")
        self.driver.execute_script("arguments[0].click();",element)


    #using javascript
    def getPageTitle(self):
        title=self.driver.execute_script("return document.title;")
        print(title)


    #using javascript
    def pageRefresh(self):
        self.driver.execute_script("history.go(0);")


    #using javascript
    def generateAlert(self):
        self.driver.execute_script("alert('hello Shanku');")


    #using javascript
    def getPageText(self):
        print(self.driver.execute_script("return document.documentElement.innerText;"))


    #using javascript
    def changeBorder(self):
        element = self.driver.find_element(By.XPATH, "//li[text()='Student Fare']")
        self.driver.execute_script("arguments[0].style.border = '3px solid red';", element)


    def scrollByPixel(self):
        # scroll down page by pixel
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        time.sleep(5)


    def scrollToTop(self):
        self.driver.execute_script("scroll(0, 0);")
        time.sleep(5)


    def scrollByElement(self):
        element = self.driver.find_element(By.XPATH, "//li[text()='Student Fare']")
        self.driver.execute_script("arguments[0].scrollIntoView()",element)
        time.sleep(5)


    def scrollToEnd(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(5)


    #We can also send data to an element usibg javascript
    def sendData(self):
        self.driver.execute_script("document.getElementbyId('username').value='shanku';")



object = JavaScript()
object.invokeWebSite()
object.clickElement()
object.getPageTitle()
object.pageRefresh()
#object.generateAlert()
object.getPageText()
object.changeBorder()

object.scrollByPixel()

object.scrollToTop()
object.scrollByElement()

object.scrollToTop()
object.scrollToEnd()
        