from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class ContactUsPage(BasePage):
    #locarator
    CONTACT_LINK = (By.XPATH, "//a[contains(text(),'Contact us')]")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    SUBJECT_INPUT = (By.NAME, "subject")
    MESSAGE_BOX = (By.ID, "message")
    SUBMIT_BUTTON = (By.NAME, "submit")
    SUCCESS_ALERT = (By.XPATH, "//div[@class='status alert alert-success']")

def go_to_contact_page(self):
    self.clicks(self.CONTACT_LINK)
def fill_content_form(self,name,email,subject,message):
    self.send_keys(self.NAME_INPUT,name)
    self.send_keys(self.EMAIL_INPUT, email)
    self.send_keys(self.SUBJECT_INPUT, subject)
    self.send_keys(self.MESSAGE_BOX, message)
def submit_form(self):
    self.click(self.SUBMIT_BUTTON)
    try:
        self.driver.switch_to.alert.accept()
    except:
        pass
def is_success_msg_display(self):
    return self.is_element_visiable(self. SUCCESS_ALERT )

