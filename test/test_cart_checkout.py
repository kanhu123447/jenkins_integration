import pytest
from pages.cartpage import CartPage
from pages.productpage import ProductPage
import time

def test_and_add_remove_product_from_cart(driver):
    product=ProductPage(driver)
    cart=CartPage(driver)

    product.open_products_page()
    time.sleep(4)

    product.open_products_page()
    time.sleep(3)

    product.set_quantity()
    time.sleep(2)

    product.click_add_to_cart()
    time.sleep(2)

    product.click_continue_shopping()
    time.sleep(3)

    cart.open_cart()
    time.sleep(2)

    product_name = cart.get_product_name()
    assert product_name != "", " No product name found in cart"

    cart.remove_product()
    time.sleep(2)
    assert cart.is_cart_empty(),"cart not empty after click remove product"
