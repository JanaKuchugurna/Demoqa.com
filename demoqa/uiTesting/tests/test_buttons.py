
class TestButtonsPage:

    def test_double_buttons_page(self, click_page_buttons):
        double = click_page_buttons.perform_double_click()
        assert double == "You have done a double click"

    def test_right_buttons_page(self, click_page_buttons):
        right = click_page_buttons.perform_right_click()
        assert right == "You have done a right click"

    def test_click_me_buttons_page(self, click_page_buttons):
        click_me = click_page_buttons.perform_click_me()
        assert click_me == "You have done a dynamic click"

