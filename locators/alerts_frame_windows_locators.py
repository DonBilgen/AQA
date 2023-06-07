from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")

    TITLE_NEW = (By.CSS_SELECTOR, "h1[id='sampleHeading']")

class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    SEE_ALERT_AFTER_5SEC_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    SEE_ALERT_CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    SEE_ALERT_PROMT_BOX_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    RESULT_PROMT_BOX = (By.CSS_SELECTOR, "span[id='promptResult']")

