from selenium.webdriver.common.by import By


class TextBoxLocators:

    FULL_NAME_LOCATOR = (By.ID, "input[@id='userName']")
    EMAIL_LOCATOR = (By.ID, "input[@id='userEmail']")
    CURRENT_ADDRESS_LOCATOR = (By.XPATH, "//textarea[@id='currentAddress]")
    PERMANENT_ADDRESS_LOCATOR = (By.XPATH, "//textarea[@id='permanentAddress']")
    SUBMIT_BUTTON_LOCATOR = (By.ID, "button[@id='submit']")
