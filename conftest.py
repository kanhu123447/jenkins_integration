
# import pytest
# from selenium import webdriver
# from utils.config import Config
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()  # You can replace with Firefox if you want
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get(Config.BASE_URL)
#     yield driver
#     driver.quit()
import pytest
import os
import time
from selenium import webdriver
from utils.config import Config


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()

    # 🔹 Headless mode (optional)
    if Config.HEADLESS:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    # 🔹 Browser setup
    driver.maximize_window()
    driver.implicitly_wait(Config.TIMEOUT)

    # 🔥 Load application
    driver.get(Config.BASE_URL)

    yield driver

    driver.quit()


# 🔥 Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot if test fails
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            # Create folder if not exists
            os.makedirs(Config.SCREENSHOTS_PATH, exist_ok=True)

            # Screenshot name with timestamp
            file_name = f"{item.name}_{int(time.time())}.png"
            file_path = os.path.join(Config.SCREENSHOTS_PATH, file_name)

            # 📸 Take screenshot
            driver.save_screenshot(file_path)