from selenium import webdriver

from main.pages.auth_page import AuthPage
from main.pages.main_page import MainPage
from main.pages.page import Page
from utils.data import CORRECT_EMAIL, CORRECT_PASSWORD, INCORRECT_EMAIL

if __name__ == "__main__":
    driver = webdriver.Firefox()

    driver.get(Page.FEEDBURNER_PAGE)
    # driver.get(Page.SIGNUP_PAGE)
    auth = AuthPage(driver)
    auth.login(CORRECT_EMAIL, CORRECT_PASSWORD)

    # auth.register("ddd", "dfsd", "dddnn.ddas", "!00kdm321&", "1", "ноябрь", "1992 ", "Муж.")

    main = MainPage(driver)
    print(main.get_feed_number())

    main.create_new_proxy("https://myblogblogblog12.blogspot.com/feeds/posts/default?alt=rss", "name11")

    print(main.get_feed_number())
    # print(main.delete_feed("dddddddd"))

    # main = MainPage(driver)
    #
