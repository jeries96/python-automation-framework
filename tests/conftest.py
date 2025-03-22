import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def selenium_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver
    driver.quit()
