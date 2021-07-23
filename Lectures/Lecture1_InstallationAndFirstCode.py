from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class Test:

    def invokeDriver(self,browserName):
        if(browserName == "chrome"):
            self.driver= webdriver.Chrome(executable_path="../browsers/chromedriver.exe")
        else:
            self.driver = webdriver.Firefox(executable_path="../browsers/geckodriver.exe")
        self.driver.maximize_window()


    def openWebPage(self):
        self.driver.get("https://www.google.com")
        print(self.driver.title)
        print(self.driver.current_url)
        print(self.driver.page_source)

if __name__ == "__main__":
    object = Test()
    object.invokeDriver("chrome")
    object.openWebPage()
