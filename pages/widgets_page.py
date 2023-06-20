from selenium.common import TimeoutException, ElementClickInterceptedException

from locators.widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordin_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_1,
                          'content': self.locators.TEXT_SECTION_1},
                     'second':
                         {'title': self.locators.SECTION_2,
                          'content': self.locators.TEXT_SECTION_2},
                     'third':
                         {'title': self.locators.SECTION_3,
                          'content': self.locators.TEXT_SECTION_3},
                     }
        section_title = self.element_is_visible(accordian[accordin_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordin_num]['content']).text
        except TimeoutException or ElementClickInterceptedException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordin_num]['content']).text

        # print(section_title.text, section_content)
        return [section_title.text, len(section_content)]
