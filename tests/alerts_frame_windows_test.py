import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage


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

    class TestAlertsPage:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts' )
            alert_page.open()
            alert_text_result = alert_page.check_see_alert()
            time.sleep(5)
            assert alert_text_result == 'You clicked a button', "Error click btn to see"

        def test_see_alert_after_5sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts' )
            alert_page.open()
            alert_text_result_5sec = alert_page.check_see_alert_after_5sec()
            # time.sleep(5)
            print(alert_text_result_5sec)
            assert alert_text_result_5sec == 'This alert appeared after 5 seconds', "Error click btn to see after 5sec"

        def test_see_alert_confirm_box(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts' )
            alert_page.open()
            alert_text_confirm_box = alert_page.check_confirm_alert()
            assert alert_text_confirm_box == 'You selected Ok', "Error click btn to see confirm box"

        def test_see_alert_promt_box(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts' )
            alert_page.open()
            my_promt_text, alert_text_promt_box = alert_page.check_promt_box_alert()

            assert alert_text_promt_box == f'You entered {my_promt_text}', "Error click btn to see promt box"

    class TestFramePage:

        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_1 = frame_page.check_frame('frame1')
            print(result_1)
            result_2 = frame_page.check_frame('frame2')
            print(result_2)

            assert result_1 == ['This is a sample page', '500px', '350px']
            assert result_2 == ['This is a sample page', '100px', '100px']




            pass
