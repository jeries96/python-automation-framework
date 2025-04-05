import pytest

from pages.login_page import LoginPage
from pages.login_page_pw import LoginPagePlayWright


class TestLogin:

    @pytest.mark.selenium
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        assert 'inventory' in driver.current_url

    @pytest.mark.playwright
    def test_login_pw(self, driver):
        login_page = LoginPagePlayWright(driver)
        login_page.login("standard_user", "secret_sauce")
        assert 'inventory' in driver.url

    @pytest.mark.selenium
    def test_invalid_login(self, driver):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.login("standarduser", "secret_sauce")
        assert login_page.is_error_displayed(), "Error Should be visible"

    @pytest.mark.playwright
    def test_invalid_login_pw(self, driver):
        driver.goto("https://www.saucedemo.com/")
        login_page = LoginPagePlayWright(driver)
        login_page.login("standarduser", "secret_sauce")
        assert login_page.is_error_displayed(), "Error Should be visible"
