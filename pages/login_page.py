from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class LoginPage(BasePage):
    usernameField = (By.ID, "user-name")
    passwordField = (By.ID, "password")
    loginButton = (By.ID, "login-button")
    errorMessage = (By.CSS_SELECTOR, "[data-test='error']")


    def open(self):
        super().open("/")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.usernameField)).send_keys(username)
        self.driver.find_element(*self.passwordField).send_keys(password)
        self.clickButton(self.loginButton)

    def loginButtonIsNotVisible(self) -> bool:
        return self.elementIsNotVisible(self.usernameField)

    def getErrorMessage(self) -> str:
        return self.getText(self.errorMessage)
        

