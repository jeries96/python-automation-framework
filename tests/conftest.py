import pytest
from playwright.sync_api import sync_playwright
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--engine", action="store", default="selenium",
                     help="Choose between 'selenium' or 'playwright' as the browser engine.")


def pytest_collection_modifyitems(config, items):
    engine = config.getoption("--engine")

    if engine == "playwright":
        skip_selenium = pytest.mark.skip(reason="Skipped because engine is playwright")
        for item in items:
            if "playwright" not in item.keywords:
                item.add_marker(skip_selenium)

    elif engine == "selenium":
        skip_playwright = pytest.mark.skip(reason="Skipped because engine is selenium")
        for item in items:
            if "selenium" not in item.keywords:
                item.add_marker(skip_playwright)


@pytest.fixture(scope="class", autouse=True)
def driver(request):
    engine = request.config.getoption("--engine")

    if engine == "selenium":
        driver = selenium_driver()
        yield driver
        driver.close()
        driver.quit()
    elif engine == "playwright":
        with sync_playwright() as p:
            driver, browser = browser_instance(p)
            yield driver
            driver.close()
            browser.close()
    else:
        raise ValueError(f"Unsupported engine '{engine}'. Please use 'selenium' or 'playwright'.")


def selenium_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    return driver


def browser_instance(p):
    """
    Creates a Chromium browser instance manually using Playwright.
    Returns a page object and browser instance for more controlled management.
    """
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    return page, browser
