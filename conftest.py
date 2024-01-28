import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    yield driver
    driver.quit()


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def hello():
    print("hello")

