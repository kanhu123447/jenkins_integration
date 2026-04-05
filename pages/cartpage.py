# pages/cart_page.py

from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class CartPage(BasePage):

    # Locators
    CART_BUTTON = (By.XPATH, "//a[@href='/view_cart']")
    PRODUCT_NAME = (By.XPATH, "//td[@class='cart_description']/h4/a")
    REMOVE_BUTTON = (By.CLASS_NAME, "cart_quantity_delete")
    EMPTY_MESSAGE = (By.XPATH, "//b[contains(text(),'Cart is empty')]")

    # Actions
    def open_cart(self):
        self.click(self.CART_BUTTON)

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def remove_product(self):
        self.click(self.REMOVE_BUTTON)

    def is_cart_empty(self):
        return self.is_element_visible(self.EMPTY_MESSAGE)
