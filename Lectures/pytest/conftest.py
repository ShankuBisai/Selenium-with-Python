from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.headless = False
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://www.google.com")
    if request.cls is not None:
        request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(params=["Chrome","Firefox"])
def setupWithParams(request):
    if request.param == "Chrome":
        options = Options()
        options.headless = False
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    if request.param == "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    #driver.get("https://www.google.com")
    driver.get("https://www.hubspot.com/")
    if request.cls is not None:
        request.cls.driver = driver  # this is making the driver available at the class level
    yield
    driver.quit()


@pytest.fixture(params=["Chrome","Firefox"])
def setupHubSpot(request):
    global driver
    if request.param == "Chrome":
        options = Options()
        options.headless = False
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    if request.param == "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.implicitly_wait(20)
    driver.maximize_window()

    if request.cls is not None:
        request.cls.driver = driver  # this is making the driver available at the class level
    yield
    driver.quit()

