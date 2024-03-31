from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from demoqa.uiTesting.locators.locators_web_tables import SEARCH_BOX, INPUT_SEARCHING_BUTTON, FIRST_NAME_LOCATOR, \
    LAST_NAME_LOCATOR, EMAIL_LOCATOR, AGE_LOCATOR, SALARY_LOCATOR, DEPARTMENT_LOCATOR, SUBMIT_BUTTON_LOCATOR, \
    ADD_BUTTON, PREVIOUS_AND_NEXT_BUTTON, EDIT_LOCATOR, LOCATOR_SALARY_KIERRA, EDIT_SUBMIT_BUTTON, ROW_PARENT, \
    DELETE_BUTTON, COUNT_ROW_LIST, VALUE_ROW_LIST, ROW_LOCATOR


class WebTablesPage:
    url = "https://demoqa.com/webtables"

    def __init__(self, driver):
        self.driver = driver
        self.add_button = ADD_BUTTON
        self.first_name = FIRST_NAME_LOCATOR
        self.last_name = LAST_NAME_LOCATOR
        self.email = EMAIL_LOCATOR
        self.age = AGE_LOCATOR
        self.salary = SALARY_LOCATOR
        self.department = DEPARTMENT_LOCATOR
        self.submit_button = SUBMIT_BUTTON_LOCATOR
        self.search_box_input = SEARCH_BOX
        self.search_button = INPUT_SEARCHING_BUTTON
        self.previous_and_next_button = PREVIOUS_AND_NEXT_BUTTON
        self.edit_button = EDIT_LOCATOR
        self.salary_kierra = LOCATOR_SALARY_KIERRA
        self.edit_submit_button = EDIT_SUBMIT_BUTTON
        self.row_parent = ROW_PARENT
        self.delete_button = DELETE_BUTTON
        self.count_row_list = COUNT_ROW_LIST
        self.value_list = VALUE_ROW_LIST
        self.row_options = ROW_LOCATOR

    def open(self):
        self.driver.get(self.url)

    def fill_table_row(self, data_list):
        for data in data_list:
            self.click_add_button()
            self.driver.find_element(By.XPATH, self.first_name).send_keys(data['FIRST_NAME'])
            self.driver.find_element(By.XPATH, self.last_name).send_keys(data['LAST_NAME'])
            self.driver.find_element(By.XPATH, self.email).send_keys(data['EMAIL'])
            self.driver.find_element(By.XPATH, self.age).send_keys(str(data['AGE']))
            self.driver.find_element(By.XPATH, self.salary).send_keys(str(data['SALARY']))
            self.driver.find_element(By.XPATH, self.department).send_keys(data['DEPARTMENT'])
            self.submit_button_registration_form()

    def click_add_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, self.add_button)
        _ = element.location_once_scrolled_into_view
        element.click()

    def submit_button_registration_form(self):
        element: WebElement = self.driver.find_element(By.XPATH, self.submit_button)
        _ = element.location_once_scrolled_into_view
        element.click()

    @property
    def next_button(self):
        return self.driver.find_element(By.XPATH, "//div[@class='-next']//button[@class='-btn' and text()='Next']")

    @property
    def previous_button(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='-previous']//button[@class='-btn' and text()='Previous']")

    def click_previous_or_next_button_if_active(self):
        previous_button = self.previous_button
        next_button = self.next_button
        if not previous_button.is_enabled():
            next_button.click()
        else:
            previous_button.click()

    def enter_search_query(self, query):
        search_box = self.driver.find_element(By.XPATH, self.search_box_input)
        search_box.send_keys(query)
        return search_box

    def click_search_button(self):
        search_button = self.driver.find_element(By.XPATH, self.search_button)
        search_button.click()

    def click_edit_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, self.edit_button)
        _ = element.location_once_scrolled_into_view
        element.click()

    def update_salary_field(self, new_salary):
        field = self.driver.find_element(By.XPATH, self.salary_kierra)
        field.clear()
        field.send_keys(str(new_salary))
        return str(new_salary)

    def click_update_edit_submit_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, self.edit_submit_button)
        _ = element.location_once_scrolled_into_view
        element.click()

    def check_update_salary_field(self):
        edit_button = self.driver.find_element(By.XPATH, self.edit_button)
        salary = edit_button.find_element(By.XPATH, self.row_parent)
        return salary.text.split()

    def delete_person(self):
        button = self.driver.find_element(By.XPATH, self.delete_button)
        button.click()

    def click_row_menu(self):
        row_menu_element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, self.count_row_list)))
        row_menu_element.click()

    @property
    def row_dropdown(self):
        return Select(self.driver.find_element(By.XPATH, "//select[@aria-label='rows per page']"))

    def select_option_in_row_dropdown_by_value(self, value):
        self.row_dropdown.select_by_value(value)
