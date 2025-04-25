import allure
import pytest
from playwright.sync_api import sync_playwright
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--engine", action="store", default="selenium",
                     help="Choose between 'selenium' or 'playwright' as the browser engine.")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            try:
                if hasattr(driver, "get_screenshot_as_png"):
                    # Selenium
                    png = driver.get_screenshot_as_png()
                elif hasattr(driver, "screenshot"):
                    # Playwright
                    png = driver.screenshot()
                else:
                    png = None

                if png:
                    allure.attach(png, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"Could not attach screenshot: {e}")


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
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    return driver


def browser_instance(p):
    """
    Creates a Chromium browser instance manually using Playwright.
    Returns a page object and browser instance for more controlled management.
    """
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    return page, browser
