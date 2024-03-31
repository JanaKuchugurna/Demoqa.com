from selenium.webdriver.common.by import By

# EXPAND_CHECKBOX_LOCATOR = (By.XPATH, "//label[.='Home']//ancestor::span[@class='rct-text']/button")
# EXPAND_CHECKBOX_LOCATOR = "//label[.='{}']//ancestor::span[@class='rct-text']/button"
# CHECK_UNCHECK_LABEL_LOCATOR = "//label[@for='tree-node-home']"
EXPAND_COLLAPSE_BUTTON_LOCATOR = "//span[text()='{}']//ancestor::span/button/*[contains(@class, 'icon-expand')]"
CHECK_UNCHECK_LABEL_LOCATOR = "//label[@for='tree-node-{}']"
ITEM_LIST_LOCATOR = "//span[@class='rct-title']"
# CHECKED_ITEMS = "//svg[@class='rct-icon rct-icon-check']"
# TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
OUTPUT_RESULT = "//span[@class='text-success']"
