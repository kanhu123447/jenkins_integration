# pages/home_page.py

from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class HomePage(BasePage):

    # Locators
    LOGO = (By.XPATH, "//img[@alt='Website for automation practice']")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    CONTACT_US_LINK = (By.XPATH, "//a[contains(text(),'Contact us')]")
    TEST_CASES_LINK = (By.XPATH, "//a[@href='/test_cases']")
    PRODUCTS_LINK = (By.XPATH, "//a[@href='/products']")
    CART_LINK = (By.XPATH, "//a[@href='/view_cart']")
    SUBSCRIPTION_EMAIL_INPUT = (By.ID, "susbscribe_email")
    SUBSCRIBE_BUTTON = (By.ID, "subscribe")
    SUBSCRIPTION_SUCCESS_MSG = (By.XPATH, "//div[@class='alert-success alert']")
    RECOMMENDED_ITEMS = (By.XPATH, "//h2[contains(text(),'recommended items')]")
    SCROLL_UP_ARROW = (By.ID, "scrollUp")

    # Actions
    def click_login(self):
        self.click(self.LOGIN_LINK)

    def click_contact_us(self):
        self.click(self.CONTACT_US_LINK)

    def click_test_cases(self):
        self.click(self.TEST_CASES_LINK)

    def click_products(self):
        self.click(self.PRODUCTS_LINK)

    def click_cart(self):
        self.click(self.CART_LINK)

    def subscribe_email(self, email):
        self.send_keys(self.SUBSCRIPTION_EMAIL_INPUT, email)
        self.click(self.SUBSCRIBE_BUTTON)

    def is_subscription_success_visible(self):
        return self.is_element_visible(self.SUBSCRIPTION_SUCCESS_MSG)

    def scroll_to_recommended_items(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_scroll_up_arrow(self):
        self.click(self.SCROLL_UP_ARROW)

    def is_logo_visible(self):
        return self.is_element_visible(self.LOGO)
