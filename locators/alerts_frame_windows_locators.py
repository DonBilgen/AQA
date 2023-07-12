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

class FramesPageLocators:
    FRAME_1 = (By.CSS_SELECTOR, "iframe[id='frame1']")
    FRAME_2 = (By.CSS_SELECTOR, "iframe[id='frame2']")
    TITLE_FRAME = (By.CSS_SELECTOR, "h1[id='sampleHeading']")

class NestedFramesPageLocators:
    FRAME_PARENT = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_TEXT = (By.CSS_SELECTOR, "body")
    FRAME_CHILD = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_TEXT = (By.CSS_SELECTOR, "p")

class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR,"button[id='showSmallModal']")
    SMALL_MODAL_BUTTON_CLOSE = (By.CSS_SELECTOR,"button[id='closeSmallModal']")
    SMALL_MODAL_BUTTON_TEXT = (By.CSS_SELECTOR,"div[class='modal-body']")
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR,"div[id='example-modal-sizes-title-sm']")

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR,"button[id='showLargeModal']")
    LARGE_MODAL_BUTTON_CLOSE = (By.CSS_SELECTOR,"button[id='closeLargeModal']")
    LARGE_MODAL_BUTTON_TEXT = (By.CSS_SELECTOR,"div[class='modal-body'] p")
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR,"div[id='example-modal-sizes-title-lg']")


