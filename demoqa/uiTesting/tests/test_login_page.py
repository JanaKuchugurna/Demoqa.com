from demoqa.uiTesting.pages.login_page import LoginPage
from demoqa.uiTesting.tests.data.data_login import NAME, EMAIL, C_ADDRESS, P_ADDRESS


class TestLoginPage:
    def test_login_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_credentials(username=NAME, email=EMAIL, current_address=C_ADDRESS,
                                     permanent_address=P_ADDRESS)
        login_page.submit()
        result_name = login_page.get_result_name()
        result_email = login_page.get_result_email()
        result_current_address = login_page.get_result_current_address()
        result_permanent_address = login_page.get_result_permanent_address()
        assert NAME == result_name
        assert EMAIL == result_email
        assert C_ADDRESS == result_current_address
        assert P_ADDRESS == result_permanent_address


