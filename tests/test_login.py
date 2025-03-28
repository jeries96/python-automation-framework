from pages.login_page import LoginPage
from pages.login_page_pw import LoginPagePlayWright


class TestLogin:

    # Selenium
    def test_login(self, selenium_driver):
        login_page = LoginPage(selenium_driver)
        login_page.login("standard_user", "secret_sauce")
        assert 'inventory' in selenium_driver.current_url

    # Playwright
    def test_login_pw(self, browser_instance):
        login_page = LoginPagePlayWright(browser_instance)
        login_page.login("standard_user", "secret_sauce")
        assert 'inventory' in browser_instance.url
