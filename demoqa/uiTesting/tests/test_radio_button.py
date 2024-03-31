from demoqa.uiTesting.pages.radio_button_page import RadioButtonPage


class TestRadioButtonPage:

    def test_radio_button_page(self, driver):
        radio_button_page = RadioButtonPage(driver)
        radio_button_page.open()
        radio_button_page.select_button_by_name("Impressive")
        radio_button_page.is_radio_button_selected("Impressive")
        target_radio_button_text = radio_button_page.target_radio_button_text("Impressive")
        radio_button_name = radio_button_page.get_selected_radio_button_name("Impressive")
        assert radio_button_name == target_radio_button_text
