from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from main.pages.page import Page
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions

from utils.base import BASE_TIMEOUT


class MainPage(Page):

    def __init__(self, driver: WebDriver):
        super().__init___(driver)

    def get_feed_number(self):
        proxies = self._driver.find_elements(By.XPATH, "//div[@class='class=proxy-list-item ng-star-inserted']")
        return len(proxies)

    def delete_feed(self, name):
        # Находим элемент "actions" с нужным "title" по XPath
        actions_element = self._driver.find_element(By.XPATH,
                                                    f"//div[@class='proxy-list-item ng-star-inserted']//div[@class='actions' and preceding-sibling::div[@class='proxy-container']//div[@class='proxy-title' and text()='{name}']]")

        delete_button = actions_element.find_element(By.XPATH,
                                                     ".//button[@class='mat-focus-indicator mat-stroked-button mat-button-base mat-primary' and span[contains(text(), 'Delete')]]")

        delete_button.click()

    def view_feed_info_by_name(self, feed_name):
        # Формируем XPath для поиска ссылки на RSS-фид по имени
        xpath = f"//a[@aria-label='Ссылка на RSS-фид прокси' and contains(@href, '{feed_name}')]"

        # Находим элемент ссылки на RSS-фид по имени
        rss_link = WebDriverWait(self._driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath))
        )
        rss_link.click()

        # Ждем загрузки страницы с фидом
        WebDriverWait(self._driver, 10).until(
            expected_conditions.presence_of_element_located((By.TAG_NAME, "channel"))
        )

        # Извлекаем информацию с загруженной страницы
        channel_element = self._driver.find_element(By.TAG_NAME, "channel")
        title = channel_element.find_element(By.TAG_NAME, "title").text
        last_build_date = channel_element.find_element(By.TAG_NAME, "lastBuildDate").text
        description = channel_element.find_element(By.TAG_NAME, "description").text
        managing_editor = channel_element.find_element(By.TAG_NAME, "managingEditor").text

        # Возвращаем извлеченную информацию
        return {
            "title": title,
            "last_build_date": last_build_date,
            "description": description,
            "managing_editor": managing_editor
        }

    def watch_post(self, number):
        proxies = self._driver.find_elements(By.XPATH, "//div[@class='proxy-title']")

    def send_feedback(self, report: str):
        feedback_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[@mattooltip='Отправить отзыв']"))
        )
        feedback_button.click()

        url_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//textarea"))
        )
        url_input.send_keys(report)

        feedback_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[@span='Send']"))
        )
        feedback_button.click()

    def create_new_proxy(self, url: str, name: str, own_url: str = None):
        next_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH,
                                                         "//button[@class='mat-focus-indicator create-proxy-button mat-raised-button mat-button-base mat-primary']"))
        )
        next_button.click()

        url_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "mat-input-0"))
        )
        url_input.send_keys(url)

        next_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH,
                                                         "/html/body/div[2]/div[2]/div/mat-dialog-container/app-create-proxy-dialog/mat-dialog-actions/progress-button/div/button"))
        )
        next_button.click()

        url_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "mat-input-1"))
        )
        url_input.send_keys(name)

        next_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH,
                                                         "/html/body/div[2]/div[2]/div/mat-dialog-container/app-create-proxy-dialog/mat-dialog-actions/progress-button/div/button"))
        )
        next_button.click()
