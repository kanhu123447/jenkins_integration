import pytest
from pages.contactus import ContactUsPage
import time

def test_contact_us(driver):
    contact=ContactUsPage(driver)
    contact.go_to_contact_page()
    time.sleep()
    assert "get in touch"in driver.page_source,"contact page not loaded"

    contact.fill_contact_form(
        name="Kanhu",
        email="kanhu@example.com",
        subject="Test Subject",
        message="This is a test message from automation script."
    )
    time.sleep(1)

    contact.submit_form()
    time.sleep(3)


    assert contact.is_success_msg_displayed(),"success message not display"
