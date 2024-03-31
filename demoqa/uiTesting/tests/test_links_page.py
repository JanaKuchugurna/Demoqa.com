from demoqa.uiTesting.pages.links_page import LinksPage


class TestLinksPage:

    def test_bad_request_link(self, driver):
        links_page = LinksPage(driver)
        links_page.open()
        response_code = links_page.click_bad_request_link()
        assert response_code == 400

    def test_home_link(self, driver):
        links_page = LinksPage(driver)
        links_page.open()
        href_link, current_url = links_page.click_to_home_link()
        assert href_link == current_url

