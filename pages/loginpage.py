from selenium.webdriver.common.by import By

from pages.basepage import BasePage

class LoginPage(BasePage):
        EMAIL_INPUT = (By.NAME, "email")
        PASSWORD_INPUT = (By.NAME, "password")
        LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

        def login(self, email, password):
            self.send_keys(self.EMAIL_INPUT, email)
            self.send_keys(self.PASSWORD_INPUT, password)
            self.click(self.LOGIN_BUTTON)

