import time
import pytest
from pages.basepage import BasePage
from pages.loginpage import LoginPage
from pages.productpage import ProductPage

def test_add_to_cart_a_product(driver):
    product=ProductPage(driver)
    login=LoginPage(driver)

    login.login()
    time.sleep(5)
    product.close_alert()
    product.chose_catogery()

    assert product.is_added_popup_displayed(), "Add to cart popup not displayed"
    product.click_add_to_cart_icon()

    product.check_cart()
    assert product.is_product_in_cart("tshart").lower(),"item not added"

    # product.click_product()
    # product.click_search_product("mobile")
    # assert "mobile" in product.get_product_name().lower(),"not mobile searched"
    # old_url=driver.current_url()
    # product.click_add_to_cart()
    # assert driver.current_url !=old_url,"not navigate to other page"

