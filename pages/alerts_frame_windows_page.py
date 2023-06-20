import time

from faker.generator import random

from locators.alerts_frame_windows_locators import BrowserWindowsLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_windows = self.driver.switch_to.alert
        return  alert_windows.text

    def check_see_alert_after_5sec(self):
        self.element_is_visible(self.locators.SEE_ALERT_AFTER_5SEC_BUTTON).click()
        time.sleep(5)
        alert_windows = self.driver.switch_to.alert
        return alert_windows.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_CONFIRM_BUTTON).click()
        alert_windows = self.driver.switch_to.alert
        alert_windows.accept()   # click OK
        # alert_windows.dismiss()  # click Cancel

        text_result = self.element_is_visible(self.locators.CONFIRM_RESULT).text
        print(text_result)
        return text_result

    def check_promt_box_alert(self):
        text = f"autotest{random.randint(0,999)}"
        print(text)
        self.element_is_visible(self.locators.SEE_ALERT_PROMT_BOX_BUTTON).click()
        alert_windows = self.driver.switch_to.alert
        alert_windows.send_keys(text)
        alert_windows.accept()
        text_result = self.element_is_present(self.locators.RESULT_PROMT_BOX).text

        print(text_result)
        return text, text_result

class FramesPage(BasePage):

    locators = FramesPageLocators()

    def check_frame(self,frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FRAME_1)
            width = frame.get_attribute('width')
            height =frame.get_attribute('height')
            print(width)
            print(height)
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]

        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.FRAME_2)
            width = frame.get_attribute('width')
            height =frame.get_attribute('height')
            print(width)
            print(height)
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()

            return [text, width, height]

class NestedFramesPage(BasePage):

        locators = NestedFramesPageLocators()

        def check_nested_frame(self):
            parent_frame = self.element_is_present(self.locators.FRAME_PARENT)
            self.driver.switch_to.frame(parent_frame)
            parent_text = self.element_is_present(self.locators.PARENT_TEXT).text

            child_frame = self.element_is_present(self.locators.FRAME_CHILD)
            self.driver.switch_to.frame(child_frame)
            child_text = self.element_is_present(self.locators.CHILD_TEXT).text

            return parent_text, child_text

class ModalDialogsPage(BasePage):

    locators = ModalDialogsPageLocators()

    def check_Modal_Dialogs_Page(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        text_small = self.element_is_visible(self.locators.SMALL_MODAL_BUTTON_TEXT).text
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON_CLOSE).click()

        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        text_large = self.element_is_visible(self.locators.LARGE_MODAL_BUTTON_TEXT).text
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON_CLOSE).click()

        return [title_small, len(text_small)], [title_large, len(text_large)]















