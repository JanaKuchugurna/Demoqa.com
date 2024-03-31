import requests
from selenium.webdriver.common.by import By

from demoqa.uiTesting.locators.locators_link_page import HOME_LINK_LOCATOR, BAD_REQUEST_LINK_LOCATOR


class LinksPage:
    url = "https://demoqa.com/links"

    def __init__(self, driver):
        self.driver = driver
        self.home_link = HOME_LINK_LOCATOR
        self.bad_request_link_locator = BAD_REQUEST_LINK_LOCATOR

    def open(self):
        self.driver.get(self.url)

    def click_to_home_link(self):
        home_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Home")
        href_link = home_link.get_attribute('href')
        request = requests.get(f'{href_link}')
        if request.status_code == 200:
            home_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return href_link, url
        else:
            return request.status_code

    def click_bad_request_link(self):
        link = self.driver.find_element(By.XPATH, self.bad_request_link_locator)
        request = requests.get("https://demoqa.com/bad-request")
        if request.status_code == 200:
            link.click()
        else:
            return request.status_code

