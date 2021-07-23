from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class Test:

    def test_MMT(self):
        options = Options()
        options.headless = False
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("https://www.makemytrip.com/")
        self.driver.maximize_window()
        assert "MakeMyTrip" in self.driver.title
        self.driver.close()

    def test_Google(self):
        options = Options()
        options.headless = False
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()
        assert "Google" in self.driver.title
        self.driver.close()

    def test_Yatra(self):
        options = Options()
        options.headless = False
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("https://www.yatra.com/")
        self.driver.maximize_window()
        assert "Google" in self.driver.title
        self.driver.close()






