from datetime import time
from demoqa.uiTesting.pages.login_page import LoginPage


class TestLoginPage:
    def test_login_page(self, driver):
        login_page = LoginPage(driver, "https://demoqa.com/text-box")
        login_page.open()
        login_page.enter_all_elements_to_login_page()
        login_page.click_submit_button()

