from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_1 = (By.CSS_SELECTOR,"div[id='section1Heading']")
    SECTION_2 = (By.CSS_SELECTOR,"div[id='section2Heading']")
    SECTION_3 = (By.CSS_SELECTOR,"div[id='section3Heading']")
    TEXT_SECTION_1 = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    TEXT_SECTION_2 = (By.CSS_SELECTOR, "div[id='section2Content']")
    TEXT_SECTION_3 = (By.CSS_SELECTOR, "div[id='section3Content'] p")