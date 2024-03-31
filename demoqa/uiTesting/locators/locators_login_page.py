from selenium.webdriver.common.by import By

FULL_NAME_LOCATOR = (By.ID, 'userName')
EMAIL_LOCATOR = (By.ID, 'userEmail')
CURRENT_ADDRESS_LOCATOR = (By.XPATH, "//textarea[@id='currentAddress']")
PERMANENT_ADDRESS_LOCATOR = (By.XPATH, "//textarea[@id='permanentAddress']")
SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[@id='submit']")

RESULT_NAME = (By.XPATH, "//div[@id='output']//p[@id='name']")
RESULT_EMAIL = (By.XPATH, "//div[@id='output']//p[@id='email']")
RESULT_CURRENT_ADDRESS = (By.XPATH, "//div[@id='output']//p[@id='currentAddress']")
RESULT_PERMANENT_ADDRESS = (By.XPATH, "//div[@id='output']//p[@id='permanentAddress']")
