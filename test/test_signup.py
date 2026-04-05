import pytest
from pages.signuppage import SignupPage
import time


@pytest.mark.parametrize(
    "name,email,password,day,month,year,first_name,last_name,company,address1,address2,country,state,city,zipcode,mobile",
    [
        (
                "Kanhu", "kanhu_test1234@example.com", "Password@123",
                "10", "June", "1998",
                "Kanhu", "Nayak", "QSpiders",
                "Street 123", "Near Temple", "India",
                "Odisha", "Bhubaneswar", "751007", "9876543210"
        )
    ])
def test_signup(driver, name, email, password, day, month, year,
                first_name, last_name, company, address1, address2,
                country, state, city, zipcode, mobile):
    signup = SignupPage(driver)

    # Navigate to Signup/Login page
    driver.find_element("link text", "Signup / Login").click()

    # Step 1: Enter basic signup info (name, email)
    signup.enter_signup_details(name, email)
    time.sleep(1)

    # Step 2: Fill account info
    signup.fill_account_info(password, day, month, year)
    time.sleep(1)

    # Step 3: Fill address info
    signup.fill_address_info(first_name, last_name, company, address1, address2,
                             country, state, city, zipcode, mobile)
    time.sleep(1)

    # Step 4: Submit form
    signup.click_create_account()

    # Assertion: Check for "Account Created!" message
    assert "Account Created!" in driver.page_source
