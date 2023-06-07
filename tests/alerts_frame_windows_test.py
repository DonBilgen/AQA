import time

from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindows:

    class TestBrowserWindows:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            test_result = new_tab_page.check_opened_new_tab()
            # time.sleep(5)
            assert test_result == 'This is a sample page', "Error new tab"


        def test_new_window(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            test_result = new_tab_page.check_opened_new_window()
            assert test_result == 'This is a sample page', "Error new window"

