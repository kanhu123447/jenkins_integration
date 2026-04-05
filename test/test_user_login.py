import pytest
from pages.loginpage import LoginPage
import time

@pytest.mark.parametrize("email, password, expected_result", [
    ("123@123k", "Kanhu@1043", "success"),
    ("wronguser@example.com", "wrongpass", "failure")
])
def test_login(driver,email,password,expected_result):
    Login=LoginPage(driver)
    driver.find_element("link text", "Signup / Login").click()
    time.sleep(5)
    Login.login(email,password)

    time.sleep(5)
    if expected_result=="success":
        print("login success full")
    else:
        print("un successful login ")
