import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.pages.auth_page import AuthPage
from main.pages.page import Page
from test.base import browser_fixture, auth_page
from utils.data import CORRECT_EMAIL, CORRECT_PASSWORD, INCORRECT_EMAIL, INCORRECT_PASSWORD


@pytest.fixture(params=[
    ("John", "Doe", "naanbdndmj213@email.com", "pdjhj!37hh", "01", "январь", "2000", "Муж."),
    ("Ivan", "Ivanov", "ivan.ivanov623@email.com", "pdjhj!37hh", "01", "январь", "2000", "Жен.")
])
def valid_user_data(request):
    return request.param


@pytest.fixture(params=[
    ("John", "Doe", "", "password", "01", "январь", "2000", "Муж."),
    ("Ivan", "Ivanov", "ivan.ivanov623@email.com", "77hhj2!fndsn", "99", "январь", "2000", "Жен.")
])
def invalid_user_data(request):
    return request.param


@pytest.mark.usefixtures("browser")
class TestAuthPage:
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_register_with_valid_data(self, valid_user_data, auth_page: AuthPage):
        auth_page.driver.get(Page.SIGNUP_PAGE)
        auth_page.register(*valid_user_data)

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_register_with_invalid_data(self, invalid_user_data, auth_page: AuthPage):
        auth_page.driver.get(Page.SIGNUP_PAGE)
        with pytest.raises(InterruptedError):
            auth_page.register(*invalid_user_data)

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_login_with_valid_credentials(self, auth_page: AuthPage):
        auth_page.driver.get(Page.FEEDBURNER_PAGE)
        auth_page.login(CORRECT_EMAIL, CORRECT_PASSWORD)

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_login_with_invalid_credentials(self, auth_page):
        with pytest.raises(InterruptedError):
            auth_page.driver.get(Page.FEEDBURNER_PAGE)
            auth_page.login(INCORRECT_EMAIL, INCORRECT_PASSWORD)

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_logout(self, auth_page: AuthPage):
        auth_page.driver.get(Page.FEEDBURNER_PAGE)
        auth_page.logout()
