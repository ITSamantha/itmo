import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.pages.auth_page import AuthPage
from main.pages.main_page import MainPage
from main.pages.page import Page


@pytest.fixture(name="browser", scope="class")
def browser_fixture(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-extensions')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("Unsupported browser: {}".format(request.param))
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def auth_page(browser):
    auth_page = AuthPage(browser)
    return auth_page


@pytest.fixture(scope="class")
def main_page(browser):
    main_page = MainPage(browser)
    return main_page
