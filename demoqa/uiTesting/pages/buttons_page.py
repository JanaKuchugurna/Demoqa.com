from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from demoqa.uiTesting.locators.locators_buttons import CLICK_ME_BUTTON_LOCATOR, RIGHT_CLICK_ME_BUTTON_LOCATOR, \
    DOUBLE_CLICK_ME_BUTTON_LOCATOR, RESULT_DOUBLE_CLICK_TEXT, RESULT_RIGHT_CLICK_ME_TEXT, RESULT_CLICK_ME_TEXT


class ButtonsPage:
    url = "https://demoqa.com/buttons"

    def __init__(self, driver):
        self.driver = driver
        self.click_me_button = CLICK_ME_BUTTON_LOCATOR
        self.right_click_me_button = RIGHT_CLICK_ME_BUTTON_LOCATOR
        self.double_click_me = DOUBLE_CLICK_ME_BUTTON_LOCATOR
        self.double_click_text = RESULT_DOUBLE_CLICK_TEXT
        self.right_click_me_text = RESULT_RIGHT_CLICK_ME_TEXT
        self.click_me_text = RESULT_CLICK_ME_TEXT

    def open(self):
        self.driver.get(self.url)

    def perform_double_click(self):
        button_element = self.driver.find_element(By.XPATH, self.double_click_me)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(button_element).perform()
        text_result = self.driver.find_element(By.XPATH, self.double_click_text)
        return text_result.text

    def perform_right_click(self):
        button_element = self.driver.find_element(By.XPATH, self.right_click_me_button)
        action_chains = ActionChains(self.driver)
        action_chains.context_click(button_element).perform()
        text_result = self.driver.find_element(By.XPATH, self.right_click_me_text)
        return text_result.text

    def perform_click_me(self):
        button_element = self.driver.find_element(By.XPATH, self.click_me_button)
        action_chains = ActionChains(self.driver)
        action_chains.click(button_element).perform()
        text_result = self.driver.find_element(By.XPATH, self.click_me_text)
        return text_result.text





