from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from demoqa.uiTesting.locators.locators import TextBoxLocators
from demoqa.uiTesting.pages.basepage import BasePage
from demoqa.uiTesting.locators import locators


class LoginPage(BasePage):
    locators = TextBoxLocators()

    def enter_all_elements_to_login_page(self):
        self.element_is_visible(self.locators.FULL_NAME_LOCATOR).send_keys("Yana")
        self.element_is_visible(self.locators.EMAIL_LOCATOR).send_keys("iana.kuchugurna@gmail.com")
        self.element_is_visible(self.locators.CURRENT_ADDRESS_LOCATOR).send_keys("Lehovecka 1145")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS_LOCATOR).send_keys("Bulachovskeho 34")

    def click_submit_button(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON_LOCATOR).click()


