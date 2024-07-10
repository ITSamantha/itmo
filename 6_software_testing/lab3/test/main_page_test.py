import pytest
from main.pages.auth_page import AuthPage
from main.pages.main_page import MainPage
from main.pages.page import Page
from test.base import browser_fixture, auth_page, main_page
from utils.data import CORRECT_EMAIL, CORRECT_PASSWORD


@pytest.fixture(params=[
    ("https://myblogblogblog12.blogspot.com/feeds/posts/default?alt=rss", "my blog1"),
    ("https://dsvxdxsvdvsxdvd122.blogspot.com/feeds/posts/default?alt=rss", "my blog2")
])
def blogs(request):
    return request.param


@pytest.mark.usefixtures("browser")
class TestMainPage:

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_main_page(self, auth_page: AuthPage):
        auth_page.driver.get(Page.FEEDBURNER_PAGE)
        assert ("Google FeedBurner" == auth_page.driver.title)

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_login_page(self, auth_page: AuthPage):
        auth_page.driver.get(Page.FEEDBURNER_PAGE)
        auth_page.login(CORRECT_EMAIL, CORRECT_PASSWORD)
        assert ("Feedburner - Home" == auth_page.driver.title)

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_view_feed_info_by_name(self, feed_name, auth_page: AuthPage, main_page: MainPage):
        auth_page.driver.get(Page.FEEDBURNER_PAGE)
        auth_page.login(CORRECT_EMAIL, CORRECT_PASSWORD)

        feed_info = main_page.view_feed_info_by_name(feed_name)

        assert feed_info is not None, "Feed info should not be None"
        assert "title" in feed_info, "Title should be present in feed info"
        assert "last_build_date" in feed_info, "Last build date should be present in feed info"
        assert "description" in feed_info, "Description should be present in feed info"
        assert "managing_editor" in feed_info, "Managing editor should be present in feed info"

    def test_delete_feed(self, feed_name, auth_page: AuthPage, main_page: MainPage):
        auth_page.driver.get(Page.FEEDBURNER_PAGE)
        auth_page.login(CORRECT_EMAIL, CORRECT_PASSWORD)

        initial_feed_count = main_page.get_feed_number()

        main_page.delete_feed(feed_name)
        new_feed_count = main_page.get_feed_number()

        assert new_feed_count == initial_feed_count - 1, "Feed count should decrease after deletion"
