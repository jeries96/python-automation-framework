import allure
from playwright.sync_api import Page


class LoginPagePlayWright:

    def __init__(self, page: Page):
        self.username_input_locator = page.get_by_placeholder("Username")
        self.password_input_locator = page.get_by_placeholder("Password")
        self.login_button_locator = page.get_by_role("button", name="Login")
        self.error_text_locator = page.locator("css=h3[data-test='error']")

    @allure.step
    def fill_username(self, username: str):
        self.username_input_locator.fill(username)

    @allure.step
    def fill_password(self, password: str):
        self.password_input_locator.fill(password)

    @allure.step
    def click_login(self):
        self.login_button_locator.click()

    @allure.step
    def is_error_displayed(self):
        return self.error_text_locator.is_visible()

    @allure.step
    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
