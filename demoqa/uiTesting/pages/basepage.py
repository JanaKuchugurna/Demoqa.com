from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    url = "https://demoqa.com/text-box"

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locators, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locators))

    def element_are_visible(self, locators, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locators))

    def element_is_presence(self, locators):
        return WebDriverWait(self.driver, 6).until(ec.presence_of_element_located(locators))

    def elements_are_presence(self, locators, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locators))

    def element_is_not_visible(self, locators, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locators))

    def element_is_clickable(self, locators, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locators))

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)

    def click_element(self, selector, wait_time=5):
        element = WebDriverWait(self.driver, wait_time).until(
            ec.presence_of_element_located(selector)
        )
        element.click()

    def send_keys_to_element(self, selector, text, wait_time=5):
        element = WebDriverWait(self.driver, wait_time).until(
            ec.presence_of_element_located(selector)
        )
        element.send_keys(text)
