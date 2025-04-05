from pages.login_page import LoginPage
from pages.login_page_pw import LoginPagePlayWright


class TestLogin:

    # Selenium
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        assert 'inventory' in driver.current_url

    # Playwright
    def test_login_pw(self, driver):
        login_page = LoginPagePlayWright(driver)
        login_page.login("standard_user", "secret_sauce")
        assert 'inventory' in driver.url

    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standarduser", "secret_sauce")
        assert login_page.is_error_displayed(), "Error Should be visible"

    def test_invalid_login_pw(self, driver):
        login_page = LoginPagePlayWright(driver)
        login_page.login("standarduser", "secret_sauce")
        assert login_page.is_error_displayed(), "Error Should be visible"
