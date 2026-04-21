from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class ProductPage(BasePage):
    # Locators

    def __init__(self, driver):
        self.driver = driver


    close_btn = (By.XPATH, "//button[@class='close']")
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
    CHOSE_MEN=(By.XPATH, "//a[@href='#Men']")
    CHOSE_WOMEN=(By.XPATH, "//a[@href='#women]")
    CHOSE_KID=(By.XPATH, "//a[@href='#kids]")

    T_SHART=(By.XPATH,"//a[contain(text(),'Tshirts')]")
    CLICK_ADD_TO_CART=(By.CLASS_NAME,"btn.btn-default.add-to-cart")
    ALERT_POPUP=(By.XPATH, "//button[contain(text(),Continue Shopping]")
    CART=(By.XPATH,"//a[@href='/product_details/2']")
    products = (By.XPATH, "//td[@class='cart_description']//a")
    t_shart_present=(By.CLASS_NAME,'class="product_image"')


    # Actions
    def close_alert(self):
        self.click(self.close_btn)
    # def open_products_page(self):

    #     self.click(self.PRODUCTS_BUTTON)
    def click_product(self):
        self.click(self.PRODUCTS_BUTTON)
    def click_search_product(self,product_name):
        self.click(self.SEARCH_BUTTON)
        self.send_keys(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)
    def chose_catogery(self):
        self.click(self.CHOSE_MEN)
        self.click(self.T_SHART)
    # def search_product(self, product_name):
    #     self.send_keys(self.SEARCH_INPUT, product_name)
    #     self.click(self.SEARCH_BUTTON)
    #
    def click_add_to_cart_icon(self):
        self.click(self.CLICK_ADD_TO_CART)

    def click_allert(self):
        self.click(self.ALERT_POPUP)

    def is_added_popup_displayed(self):
        try:
            popup = self.driver.find_element(By.XPATH, "//div[@class='modal-content']")
            return popup.is_displayed()
        except:
            return False


    def check_cart(self):
        self.click(self.CART)

    def is_product_in_cart(self, product_name):
        products = (By.XPATH, "//td[@class='cart_description']//a")

        for p in products:
            if product_name.lower() in p.text.lower():
                return True
        return False


    # def get_search_results_count(self):
    #     return len(self.driver.find_elements(*self.SEARCH_RESULTS))
    #
    # def click_first_view_product(self):
    #     self.click(self.VIEW_PRODUCT_LINK)
    #
    # def get_product_name(self):
    #     return self.get_text(self.PRODUCT_NAME)
    #
    # def set_quantity(self, quantity):
    #     element = self.find_element(self.QUANTITY_INPUT)
    #     element.clear()
    #     element.send_keys(str(quantity))
    #
    # def click_add_to_cart(self):
    #     self.click(self.ADD_TO_CART_BUTTON)
    #
    # def click_continue_shopping(self):
    #     self.click(self.CONTINUE_SHOPPING_BUTTON)
    #
    # def add_review(self, name, email, review_text):
    #     self.send_keys(self.ADD_REVIEW_NAME, name)
    #     self.send_keys(self.ADD_REVIEW_EMAIL, email)
    #     self.send_keys(self.ADD_REVIEW_TEXT, review_text)
    #     self.click(self.SUBMIT_REVIEW_BUTTON)
    #
    # def is_review_success_message_displayed(self):
    #     return self.is_element_visible(self.REVIEW_SUCCESS_MSG)


