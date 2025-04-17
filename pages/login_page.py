import allure
from selenium.webdriver.common.by import By

from pages.base_page import BaseElement


class LoginPage(BaseElement):
    username_input_locator = (By.ID, "user-name")
    password_input_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")
    login_error_text_alert = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def fill_username(self, username: str):
        self.send_keys(self.username_input_locator, value=username)

    @allure.step
    def fill_password(self, password: str):
        self.send_keys(self.password_input_locator, value=password)

    @allure.step
    def click_login(self):
        self.click(self.login_button_locator)

    @allure.step
    def is_error_displayed(self):
        return self.wait_for_visibility(self.login_error_text_alert)

    @allure.step
    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
