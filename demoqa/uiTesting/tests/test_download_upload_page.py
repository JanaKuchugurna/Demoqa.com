from demoqa.uiTesting.pages.download_upload_page import DownloadUploadPage


class TestUploadDownloadPage:

    def test_upload_file(self, driver):
        upload_download_page = DownloadUploadPage(driver)
        upload_download_page.open()
        file_name, result_text = upload_download_page.upload_file()
        assert file_name == result_text

    def test_download_button(self, driver):
        upload_download_page = DownloadUploadPage(driver)
        upload_download_page.open()
        check = upload_download_page.download_button()
        assert check is True

