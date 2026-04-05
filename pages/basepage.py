# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By




class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):
        """
        Wait for the element to be visible and return it.
        locator: tuple -> (By.ID, "element_id") or (By.XPATH, "//button[@type='submit']")
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element not found: {locator}")

    def click(self, locator):
        """
        Click on an element after waiting for it to be clickable.
        """
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        """
        Clear any existing text and send new input.
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Return the visible text of the element.
        """
        return self.find_element(locator).text

    def is_element_visible(self, locator):
        """
        Check if an element is visible.
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_title(self):
        """
        Return the current page title.
        """
        return self.driver.title

    def navigate_to(self, url):
        """
        Open a given URL in the browser.
        """
        self.driver.get(url)







