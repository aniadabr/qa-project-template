from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 15)

    def open(self, path: str = ""):
        self.driver.get(f"{self.base_url}{path}")

    def clickButton(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def getText(self,locator) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def getElement(self, locator):
        return self.wait(EC.presence_of_element_located(locator))
    
    def elementIsNotVisible(self, locator) -> bool:
        return self.wait.until(EC.invisibility_of_element(locator))