import random

import pytest
from paramiko import file

from demoqa.uiTesting.pages.buttons_page import ButtonsPage
from demoqa.uiTesting.pages.web_tables_page import WebTablesPage
from demoqa.uiTesting.tests.data.data_web_tables import data_list


@pytest.fixture(scope='class')
def click_page_buttons(driver):
    buttons_page = ButtonsPage(driver)
    buttons_page.open()
    yield buttons_page


@pytest.fixture(scope='class')
def enter_credential_in_table(driver):
    web_tables_page = WebTablesPage(driver)
    web_tables_page.open()
    web_tables_page.fill_table_row(data_list)
    yield web_tables_page

# def generate_file():
#     path = rf'Z:\QA tester\Utest\filetest{random.randint(0, 999)}.txt'
#     with open(path, 'w') as file:
#         file.write("Hello, world!{random.randint(0, 999)}")
#         file.close()
#         return file.name, path