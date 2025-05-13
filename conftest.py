import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope='function')
def browserInstance(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
    elif browser_name == 'firefox':
        driver_path = GeckoDriverManager().install()
        service = Service(driver_path)
        driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.wait = WebDriverWait(driver, timeout=10)
    yield driver # before test function execution
    driver.close() # after your test function execution