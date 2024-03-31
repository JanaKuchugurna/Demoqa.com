from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from demoqa.uiTesting.locators.locators_dynamic_properties import ENABLE_FIVE_SECONDS_BUTTON, COLOR_CHANGE_BUTTON, \
    VISIBLE_AFTER_FIVE_SECONDS_BUTTON


class DynamicPropertiesPage:
    url = "https://demoqa.com/dynamic-properties"

    def __init__(self, driver):
        self.driver = driver
        self.enable_button = ENABLE_FIVE_SECONDS_BUTTON
        self.color_button = COLOR_CHANGE_BUTTON
        self.visible_button = VISIBLE_AFTER_FIVE_SECONDS_BUTTON

    def open(self):
        self.driver.get(self.url)

    def is_enable_button_visible(self, timeout=5):
        element: WebElement = WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(self.enable_button))
        return element.is_displayed()

    def click_color_button(self):
        button = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(self.color_button))
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(button))
        button.click()

    def is_color_danger_for_button(self):
        button = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(self.color_button))
        class_attribute = button.get_attribute("class")
        return "text-danger" in class_attribute and "btn-primary" in class_attribute
