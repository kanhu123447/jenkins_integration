from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class AccountPage(BasePage):

    # Locators
    LOGOUT_LINK = (By.XPATH, "//a[contains(text(),'Logout')]")

    # Actions
    def click_logout(self):
        self.click(self.LOGOUT_LINK)
