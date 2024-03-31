import base64
import os
import random
from selenium.webdriver.common.by import By
from demoqa.uiTesting.locators.locators_download_upload_page import UPLOAD_LOCATOR, DOWNLOAD_LOCATOR, \
    UPLOADED_RESULT_TEXT


class DownloadUploadPage:
    url = "https://demoqa.com/upload-download"

    def __init__(self, driver):
        self.driver = driver
        self.upload_button_locator = UPLOAD_LOCATOR
        self.download_button_locator = DOWNLOAD_LOCATOR
        self.uploaded_result_text = UPLOADED_RESULT_TEXT

    def open(self):
        self.driver.get(self.url)

    def generate_new_file(self):
        path = rf'Z:\QA tester\Utest\filetest{random.randint(0, 999)}.txt'
        with open(path, 'w') as file:
            file.write("Hello, world!{random.randint(0, 999)}")
            file.close()
            return file.name, path

    def upload_file(self):
        file_name, path = self.generate_new_file()
        upload_input = self.driver.find_element(By.XPATH, self.upload_button_locator)
        upload_input.send_keys(path)
        os.remove(path)
        text = self.driver.find_element(By.XPATH, self.uploaded_result_text).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    def download_button(self):
        link = self.driver.find_element(By.XPATH, self.download_button_locator).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'Z:\QA tester\Utest\filetest{random.randint(0, 999)}.jpd'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
        check_file = os.path.exists(path_name_file)
        # f.close()
        return check_file
