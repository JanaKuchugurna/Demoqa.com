from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from demoqa.uiTesting.locators import locators_login_page
from demoqa.uiTesting.locators.locators_login_page import CURRENT_ADDRESS_LOCATOR, PERMANENT_ADDRESS_LOCATOR, EMAIL_LOCATOR, \
    FULL_NAME_LOCATOR, SUBMIT_BUTTON_LOCATOR, RESULT_NAME, RESULT_EMAIL, RESULT_CURRENT_ADDRESS, \
    RESULT_PERMANENT_ADDRESS
from demoqa.uiTesting.pages.basepage import BasePage


class LoginPage:
    url = "https://demoqa.com/text-box"

    def __init__(self, driver):
        self.driver = driver
        self.user_name_field = FULL_NAME_LOCATOR
        self.password_field = EMAIL_LOCATOR
        self.current_address_text_aria = CURRENT_ADDRESS_LOCATOR
        self.permanent_address_text_aria = PERMANENT_ADDRESS_LOCATOR
        self.submit_button = SUBMIT_BUTTON_LOCATOR
        self.output_name = RESULT_NAME
        self.output_email = RESULT_EMAIL
        self.output_current_address = RESULT_CURRENT_ADDRESS
        self.output_permanent_address = RESULT_PERMANENT_ADDRESS

    def open(self):
        self.driver.get(self.url)

    def fill_user_name(self, username):
        self.driver.find_element(*self.user_name_field).send_keys(username)

    def fill_email(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def fill_current_address(self, current_address):
        self.driver.find_element(*self.current_address_text_aria).send_keys(current_address)

    def fill_permanent_address(self, permanent_address):
        self.driver.find_element(*self.permanent_address_text_aria).send_keys(permanent_address)

    def enter_credentials(self, username, email, current_address, permanent_address):
        self.fill_user_name(username)
        self.fill_email(email)
        self.fill_current_address(current_address)
        self.fill_permanent_address(permanent_address)

    def submit(self):
        element: WebElement = self.driver.find_element(*self.submit_button)
        _ = element.location_once_scrolled_into_view
        element.click()

    def get_result_name(self):
        return self.driver.find_element(*self.output_name).text.split(':')[1]

    def get_result_email(self):
        return self.driver.find_element(*self.output_email).text.split(':')[1]

    def get_result_current_address(self):
        return self.driver.find_element(*self.output_current_address).text.split(':')[1]

    def get_result_permanent_address(self):
        return self.driver.find_element(*self.output_permanent_address).text.split(':')[1]
