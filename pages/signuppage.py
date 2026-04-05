# pages/signup_page.py

from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class SignupPage(BasePage):

    # Locators
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")

    TITLE_RADIO_MR = (By.ID, "id_gender1")
    PASSWORD_INPUT = (By.ID, "password")
    DAY_DROPDOWN = (By.ID, "days")
    MONTH_DROPDOWN = (By.ID, "months")
    YEAR_DROPDOWN = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OFFERS_CHECKBOX = (By.ID, "optin")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS1 = (By.ID, "address1")
    ADDRESS2 = (By.ID, "address2")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")

    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")

    # Actions
    def enter_signup_details(self, name, email):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)

    def fill_account_info(self, password, day, month, year):
        self.click(self.TITLE_RADIO_MR)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.send_keys(self.DAY_DROPDOWN, day)
        self.send_keys(self.MONTH_DROPDOWN, month)
        self.send_keys(self.YEAR_DROPDOWN, year)
        self.click(self.NEWSLETTER_CHECKBOX)
        self.click(self.OFFERS_CHECKBOX)

    def fill_address_info(self, first_name, last_name, company, address1, address2,
                          country, state, city, zipcode, mobile):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.COMPANY, company)
        self.send_keys(self.ADDRESS1, address1)
        self.send_keys(self.ADDRESS2, address2)
        self.send_keys(self.COUNTRY, country)
        self.send_keys(self.STATE, state)
        self.send_keys(self.CITY, city)
        self.send_keys(self.ZIPCODE, zipcode)
        self.send_keys(self.MOBILE_NUMBER, mobile)

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)
