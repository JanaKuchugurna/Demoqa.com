# RADIO_BUTTON_LOCATOR = "//label[text()="Yes"]//ancestor::div[contains(@class, "radio")]"
# RESULT_NAME_LOCATOR = "//span[@class='text-success' and text()='Yes']"
LOCATOR = "//label[text()='{}']//ancestor::div[contains(@class, 'radio')]"
INPUT = f'{LOCATOR}/input'
LABEL = f'{LOCATOR}/label'
RESULT_NAME_LOCATOR = "//span[@class='text-success' and text()='{}']"
