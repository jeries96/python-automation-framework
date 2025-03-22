from pages.login_page import LoginPage


class TestLogin:

    def test_login(self, selenium_driver):
        login_page = LoginPage(selenium_driver)
        login_page.login("standard_user", "secret_sauce")
        assert 'inventory' in selenium_driver.current_url
