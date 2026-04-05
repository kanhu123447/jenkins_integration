import pytest
from pages.homepage import HomePage
import time
def test_home_page_action(driver):
    home=HomePage(driver)

    assert home.is_logo_visible(),"logo is not visiable on the home page"

    home.click_products()
    time.sleep(5)
    assert "All product" in driver.page_source,"failed the navigate page"
    home.click_test_cases()
    time.sleep(5)
    assert "Testcase" in driver.page_source,"failed testcase page"
    home.click_contact_us()
    time.sleep(5)
    assert "Get In Touch" in driver.page_source.upper(),"not found"
    home.click_scroll_up_arrow()
    time.sleep(5)
    assert home.is_logo_visible(),"logo not visiable"
    home.is_subscription_success_visible("test123@example.com")
    time.sleep(5)
    assert home.is_subscription_success_visible(),"not subscribed"