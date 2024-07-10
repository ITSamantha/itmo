from selenium.webdriver.remote.webdriver import WebDriver


class Page:
    AUTH_PAGE = "https://accounts.google.com"
    SIGNUP_PAGE = "https://accounts.google.com/signup"
    FEEDBURNER_PAGE = "https://feedburner.google.com/"

    def __init___(self, driver: WebDriver):
        self._driver: WebDriver = driver

    @property
    def driver(self):
        return self._driver

    @property
    def current_page_title(self):
        return self._driver.title

    """
    @driver.setter
    def driver(self, driver: BaseWebDriver):
        self._driver = driver

        def scrape_main_page(self, url):
            # Открытие страницы
            self.driver.get(url)
            # Получение HTML содержимого
            html_content = self.driver.page_source
            return html_content

        def close_driver(self):
            # Закрытие драйвера
            self.driver.quit()

    # Пример использования класса для получения главной страницы сайта
    if __name__ == "__main__":
        scraper = FeedBurnerScraper()
        url = "https://feedburner.google.com/"
        html_content = scraper.scrape_main_page(url)
        print(html_content)  # Вывод HTML содержимого
        scraper.close_driver()
    """
