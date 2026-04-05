import pytest

from pages.homepage import HomePage
from pages.logout import AccountPage
from pages.loginpage import LoginPage
import time

@pytest.mark.parametrize("email, password", [
    ("kanhu_test1234@example.com", "Password@123")
])
def test_logout(driver,email,password):
    home=HomePage(driver)
    login=LoginPage(driver)

    home.click_login()
    time.sleep(2)

    login.login(email,password)
    time.sleep(2)
    assert "logout" in driver.page_source,"login failed-logout linl not found"

    home.click_logout()
    time.sleep(1)

    assert "login to your account" in driver.page_source,"logout failed"