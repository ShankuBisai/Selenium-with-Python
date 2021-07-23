from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
class WebDriverManager:

    driver = None

    @classmethod
    def webDriverManager(cls,browser,headless="false"):
        if browser == "chrome":
            if(headless == "false"):
                cls.driver = webdriver.Chrome(ChromeDriverManager().install())
            else:
                options = Options()
                options.headless = True
                options.add_argument('--allow-running-insecure-content')
                options.add_argument('--ignore-certificate-errors')
                cls.driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        elif browser == "firefox":
            if(headless == "false"):
                cls.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            else:
                options = webdriver.FirefoxOptions()
                options.headless = True
                cls.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
        else:
            print("please pass the correct browser name")
            raise Exception("Driver is not found")

        cls.driver.maximize_window()
        return cls.driver


if __name__ == '__main__':
    driver=WebDriverManager.webDriverManager("chrome")

