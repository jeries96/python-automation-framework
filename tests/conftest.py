import pytest
from playwright.sync_api import Page, sync_playwright
from selenium import webdriver


@pytest.fixture(scope='class')
def selenium_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def playwright_driver(page: Page):
    """
    launching the browser handled by the plugin -> Playwright-Pytest plugin (pytest-playwright).
    No browser close logic is needed, Playwright handles it under the hood.
    """
    page.goto("https://www.saucedemo.com/")
    yield


@pytest.fixture(scope="class")
def browser_instance():
    """
    here we manually manage the browser lifecycle
    - Creates a Chromium browser instance manually.
    - Returns a page object after navigation.
    - Need to close the browser after the tests.

     when to use manual setup?
     when u want more control over the browser, like setting options or custom browser contexts.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        yield page
        browser.close()
