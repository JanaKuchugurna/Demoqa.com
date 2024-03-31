from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from demoqa.uiTesting.locators.locators_radio_buttons import INPUT, LABEL, LOCATOR, RESULT_NAME_LOCATOR


class RadioButtonPage:
    url = "https://demoqa.com/radio-button"

    def __init__(self, driver):
        self.driver = driver
        self.radio_button = LOCATOR
        self.radio_button_input = INPUT
        self.radio_button_label = LABEL
        self.result_name = RESULT_NAME_LOCATOR

    def open(self):
        self.driver.get(self.url)

    def is_radio_button_selected(self, name):
        element_input = f"//label[text()='{name}']//ancestor::div[contains(@class, 'radio')]/input"
        element: WebElement = self.driver.find_element(By.XPATH, element_input)
        return element.is_selected()

    def select_button_by_name(self, name):
        self.__select_radio_button(name)

    def __select_radio_button(self, name: str):
        element_input = f"//label[text()='{name}']//ancestor::div[contains(@class, 'radio')]/input"
        element_label = element_input.replace("input", "label")
        _input = self.driver.find_element(By.XPATH, element_input)
        _label = self.driver.find_element(By.XPATH, element_label)
        if not _input.is_enabled():
            self.driver.execute_script('arguments[0].removeAttribute("disabled")')
            _label.click()
        else:
            if not _input.is_selected():
                _label.click()

    def get_selected_radio_button_name(self, name):
        return self.driver.find_element(By.XPATH, self.radio_button.format(name)).text

    def target_radio_button_text(self, text):
        element_input = f"//span[@class='text-success' and text()='{text}']"
        self.driver.find_element(By.XPATH, element_input)
        return text
