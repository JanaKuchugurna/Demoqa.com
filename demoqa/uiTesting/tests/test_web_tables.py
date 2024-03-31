from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from demoqa.uiTesting.pages.web_tables_page import WebTablesPage


class TestWebTables:
    def test_next_previous_button(self, enter_credential_in_table):
        enter_credential_in_table.click_previous_or_next_button_if_active()
        enter_credential_in_table.click_previous_or_next_button_if_active()

    def test_edit_button(self, driver):
        web_tables_page = WebTablesPage(driver)
        web_tables_page.open()
        web_tables_page.click_edit_button()
        new_salary = web_tables_page.update_salary_field(new_salary=4000)
        web_tables_page.click_update_edit_submit_button()
        row = web_tables_page.check_update_salary_field()[4]
        assert new_salary in row

    def test_row_menu(self, driver):
        web_tables_page = WebTablesPage(driver)
        web_tables_page.open()
        web_tables_page.click_row_menu()
        expected_value = '100'
        web_tables_page.select_option_in_row_dropdown_by_value(expected_value)
        selected_option = web_tables_page.row_dropdown.first_selected_option.text
        assert expected_value in selected_option, f"Expected {expected_value} but found {selected_option}"

    def test_search_field(self, driver):
        web_tables_page = WebTablesPage(driver)
        web_tables_page.open()
        search_box = web_tables_page.enter_search_query("Kierra")
        print(search_box)
        web_tables_page.click_search_button()
        assert search_box.get_attribute("value") == "Kierra"

    def test_delete_pearson_from_table(self, driver):
        web_tables_page = WebTablesPage(driver)
        web_tables_page.open()
        search_box = web_tables_page.enter_search_query("Alden")
        web_tables_page.delete_person()
        search_box.clear()
        try:
            name_element = driver.find_element(By.XPATH, f"//div[contains(text(), 'alden@example.com')]")
        except NoSuchElementException:
            person_deleted = True
        else:
            person_deleted = False

        assert person_deleted, "Person is still present in the table after deletion"


