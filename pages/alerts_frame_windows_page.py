import time

from faker.generator import random

from locators.alerts_frame_windows_locators import BrowserWindowsLocators, AlertsPageLocators
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






