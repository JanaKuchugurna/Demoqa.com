from datetime import time

from demoqa.uiTesting.pages.dynamic_properties_page import DynamicPropertiesPage


class TestDynamicPropertiesPage:

    def test_will_enable_5_seconds_button(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver)
        dynamic_properties_page.open()
        assert dynamic_properties_page.is_enable_button_visible(), "The 'Will enable in 5 seconds' button did not become visible within 5 seconds"

    def test_button_color_change(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver)
        dynamic_properties_page.open()
        dynamic_properties_page.click_color_button()
        assert dynamic_properties_page.is_color_danger_for_button()