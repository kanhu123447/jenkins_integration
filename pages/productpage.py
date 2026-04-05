from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class ProductPage(BasePage):
    # Locators
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCH_RESULTS = (By.XPATH, "//div[@class='features_items']//div[contains(@class, 'productinfo')]")
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[@class='btn btn-default add-to-cart']")  # first visible one
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[contains(text(),'Continue Shopping')]")
    VIEW_PRODUCT_LINK = (By.XPATH, "//a[contains(text(),'View Product')]")
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']//h2")
    QUANTITY_INPUT = (By.ID, "quantity")
    ADD_REVIEW_NAME = (By.ID, "name")
    ADD_REVIEW_EMAIL = (By.ID, "email")
    ADD_REVIEW_TEXT = (By.ID, "review")
    SUBMIT_REVIEW_BUTTON = (By.ID, "button-review")
    REVIEW_SUCCESS_MSG = (By.XPATH, "//span[contains(text(),'Thank you for your review.')]")

    # Actions
    def open_products_page(self):
        self.click(self.PRODUCTS_BUTTON)

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_search_results_count(self):
        return len(self.driver.find_elements(*self.SEARCH_RESULTS))

    def click_first_view_product(self):
        self.click(self.VIEW_PRODUCT_LINK)

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def set_quantity(self, quantity):
        element = self.find_element(self.QUANTITY_INPUT)
        element.clear()
        element.send_keys(str(quantity))

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def add_review(self, name, email, review_text):
        self.send_keys(self.ADD_REVIEW_NAME, name)
        self.send_keys(self.ADD_REVIEW_EMAIL, email)
        self.send_keys(self.ADD_REVIEW_TEXT, review_text)
        self.click(self.SUBMIT_REVIEW_BUTTON)

    def is_review_success_message_displayed(self):
        return self.is_element_visible(self.REVIEW_SUCCESS_MSG)


