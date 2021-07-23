from Lecture2_WebDriverManager_CrossBrowser import *

class JqueryMultiSelectDropdown:

    def __init__(self):
        self.driver = WebDriverManager.webDriverManager("chrome")

    def invokeWebSite(self):
        self.driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

    def multiSelectDropDown(self,element="span.comboTreeItemTitle",textToClick=["choice 5","choice 6","choice 6 1"]):
        self.driver.find_element(By.ID,"justAnInputBox").click()
        webElement = self.driver.find_elements(By.CSS_SELECTOR,element)
        if not textToClick[0] == "all":
            for ele in webElement:
               for text in textToClick:
                   if ele.text == text:
                       ele.click()
                       break
        else:
            try:
                for ele in webElement:
                    ele.click()
            except Exception as e :
                print(e)


object = JqueryMultiSelectDropdown()
object.invokeWebSite()
object.multiSelectDropDown(textToClick=["all"])




