import os
from abc import ABCMeta

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement(metaclass=ABCMeta):
    timeout = 20

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=self.timeout)

    def click(self, by_locator) -> None:
        element = self.wait.until(expected_conditions.element_to_be_clickable(by_locator))
        element.click()

    def send_keys(self, by_locator, value) -> None:
        element = self.wait.until(expected_conditions.element_to_be_clickable(by_locator))
        element.clear()
        element.send_keys(value)

    def wait_for_visibility(self, by_locator) -> WebElement:
        return self.wait.until(expected_conditions.visibility_of_element_located(by_locator))

    def visibility_of_all_elements(self, by_locator):
        return self.wait.until(expected_conditions.visibility_of_all_elements_located(by_locator))
