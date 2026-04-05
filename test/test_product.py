import pytest
from pages.productpage import ProductPage
import time

def test_product_page(driver):
    product=ProductPage(driver)
    product.open_products_page()
    time.sleep(5)
    assert "All product" in driver.page_source,"fail to open productpage"

    product_name="shirt"
    product.search_product(product_name)
    time.sleep(5)
    assert product.get_search_results_count()>0,"no search found"

    product.click_first_view_product()
    time.sleep(5)
    assert product_name.lower() in product.get_product_name(),"name missmatch"

    product.set_quantity(2)
    product.click_add_to_cart()
    time.sleep(4)
    product.click_continue_shopping()
    time.sleep(4)

def test_submit_review(driver):
    product=ProductPage(driver)

    product.open_products_page()
    time.sleep(1)
    product.click_first_view_product()
    time.sleep(2)

    name="kanhu"
    email="kanhu@example.com"
    review_text="nice product"

    product.add_review(name,email,review_text)
    time.sleep(3)
    assert product.is_review_success_message_displayed(),"review not succesfully"


