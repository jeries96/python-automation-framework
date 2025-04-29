import allure
from selenium.webdriver.common.by import By

from logger import get_logger
from pages.base_page import BaseElement

logger = get_logger(__name__)


class LoginPage(BaseElement):
    username_input_locator = (By.ID, "user-name")
    password_input_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")
    login_error_text_alert = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def fill_username(self, username: str):
        logger.info("Filling username")
        self.send_keys(self.username_input_locator, value=username)

    @allure.step
    def fill_password(self, password: str):
        logger.info("Filling password")
        self.send_keys(self.password_input_locator, value=password)

    @allure.step
    def click_login(self):
        logger.info("Clicking login")
        self.click(self.login_button_locator)

    @allure.step
    def is_error_displayed(self):
        logger.info("Waiting for error")
        return self.wait_for_visibility(self.login_error_text_alert)

    @allure.step
    def login(self, username, password):
        logger.info("-- Start Login Step -- ")
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
