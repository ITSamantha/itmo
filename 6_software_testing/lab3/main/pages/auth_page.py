from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from main.pages.page import Page

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions

from utils.base import BASE_TIMEOUT


class AuthPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init___(driver)

    def login(self, email: str, password: str):
        try:
            email_input = self._driver.find_element(By.XPATH, "//input[@id='identifierId']")
            email_input.send_keys(email)
            email_input.send_keys(Keys.RETURN)

            password_input = WebDriverWait(self._driver, BASE_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='Passwd']"))
            )

            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
        except Exception as e:
            raise InterruptedError("Incorrect login or password.")

    def register(self, first_name: str, last_name: str, email: str, password: str, birth_day: str, birth_month: str,
                 birth_year: str, gender: str):
        try:
            first_name_input = WebDriverWait(self.driver, BASE_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='firstName']"))
            )
            first_name_input.send_keys(first_name)

            last_name_input = WebDriverWait(self.driver, BASE_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='lastName']"))
            )
            last_name_input.send_keys(last_name)
            last_name_input.send_keys(Keys.RETURN)

            birth_day_input = WebDriverWait(self.driver, BASE_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='day']"))
            )
            birth_day_input.send_keys(birth_day)

            birth_month_input = WebDriverWait(self.driver, BASE_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//select[@id='month']"))
            )
            birth_month_input.send_keys(birth_month)

            birth_year_input = WebDriverWait(self.driver, BASE_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='year']"))
            )
            birth_year_input.send_keys(birth_year)

            gender_option = WebDriverWait(self.driver, BASE_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//select[@id='gender']"))
            )
            gender_option.send_keys(gender)
            birth_year_input.send_keys(Keys.RETURN)

            email_input = WebDriverWait(self.driver, BASE_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='Username']"))
            )
            email_input.send_keys(email)
            email_input.send_keys(Keys.RETURN)

            password_input = WebDriverWait(self.driver, BASE_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='Passwd']"))
            )
            password_input.send_keys(password)

            confirm_password_input = WebDriverWait(self.driver, BASE_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='PasswdAgain']"))
            )
            confirm_password_input.send_keys(password)
            confirm_password_input.send_keys(Keys.RETURN)
        except Exception as e:
            raise InterruptedError(str(e))

    def logout(self):
        try:
            logout_button = WebDriverWait(self.driver, BASE_TIMEOUT).until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, "//button[@class='mat-focus-indicator sign-out-button mat-button mat-button-base']"))
            )
            logout_button.click()
        except Exception as e:
            raise InterruptedError(str(e))
