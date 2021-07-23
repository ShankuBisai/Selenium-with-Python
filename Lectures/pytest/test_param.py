import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setupHubSpot")
class TestParamterization:

    @pytest.mark.parametrize(

                               "username,password",
                               [
                                    ("abc@gmail.com","abc"),
                                    ("xyz@gmail.com","xyz"),
                               ]

                            )
    def test_login(self,username,password):
        """
        THis method is used to login to hub spot application
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://www.zoho.com")
        self.driver.find_element(By.XPATH,"//a[@class='zh-login']").click()
        self.driver.find_element(By.ID,"login_id").send_keys(username)
        self.driver.find_element(By.ID,"nextbtn").click()
        self.driver.find_element(By.ID,"password").send_keys(password)
















