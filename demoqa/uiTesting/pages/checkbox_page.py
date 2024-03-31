from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from demoqa.uiTesting.locators.locators_check_boxes import EXPAND_COLLAPSE_BUTTON_LOCATOR, CHECK_UNCHECK_LABEL_LOCATOR, \
    OUTPUT_RESULT, ITEM_LIST_LOCATOR


class CheckBoxPage:
    url = "https://demoqa.com/checkbox"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.expand_button_locator = EXPAND_COLLAPSE_BUTTON_LOCATOR
        self.check_uncheck_label = CHECK_UNCHECK_LABEL_LOCATOR
        self.output_result = OUTPUT_RESULT
        self.item_list = ITEM_LIST_LOCATOR

    def open(self):
        print(f'opening page: {self.url}')
        self.driver.get(self.url)
        return self

    def __expand_or_collapse_folder(self, name, expand=True):
        if expand:
            state = "close"
        else:
            state = "open"
        element = self.driver.find_element(By.XPATH, self.expand_button_locator.format(name))
        if f'expand-{state}' in element.get_attribute('class'):
            element.click()

    def expand_folder(self, name):
        self.__expand_or_collapse_folder(name, expand=True)

    def collapse_folder(self, name):
        self.__expand_or_collapse_folder(name, expand=False)

    def expand_nodes_from_list(self, *nodes):
        for node in nodes:
            self.expand_folder(node)

    def check_folders(self, *names):
        for name in names:
            self.__check_or_uncheck_folder(name, check=True)

    def uncheck_folders(self, *names):
        for name in names:
            self.__check_or_uncheck_folder(name, check=False)

    def __check_or_uncheck_folder(self, name: str, check=True):
        name = name.lower()
        check_uncheck_input = f"//label[@for='tree-node-{name}']/input"
        check_uncheck_label = f"//label[@for='tree-node-{name}']/."
        _input = self.driver.find_element(By.XPATH, check_uncheck_input)
        _label = self.driver.find_element(By.XPATH, check_uncheck_label)
        if check:
            if not _input.is_selected():
                _label.click()
        else:
            if _input.is_selected():
                _label.click()

    def get_item_check_box_list(self):
        label_elements = self.driver.find_elements(By.XPATH, self.item_list)
        names = [item.text for item in label_elements]
        item_names = [name.replace(' ', '').replace('doc', '').replace('.', '').lower() for name in
                      names]
        return item_names

    def get_checkbox_text_below(self):
        label_elements = self.driver.find_elements(By.XPATH, self.output_result)
        checkbox_text_below = [item.text.replace(' ', '').lower() for item in label_elements]
        return checkbox_text_below



