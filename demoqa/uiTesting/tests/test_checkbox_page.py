from demoqa.uiTesting.pages.checkbox_page import CheckBoxPage


class TestCheckBoxPage:

    def test_expand_button(self, driver):
        checkbox_page = CheckBoxPage(driver)
        checkbox_page.open()
        checkbox_page.expand_nodes_from_list('Home', 'Desktop', 'Documents', 'Office', 'Downloads',  'WorkSpace')
        checkbox_page.check_folders('Home')
        # checkbox_page.check_folders('Home', 'Desktop', 'Documents', 'Workspace', 'React', 'Angular', 'Veu', 'Office')
        # checkbox_page.uncheck_folders('Veu')
        checkbox_text = checkbox_page.get_item_check_box_list()
        name_result = checkbox_page.get_checkbox_text_below()
        assert name_result == checkbox_text
