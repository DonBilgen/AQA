import os
import random
import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        # self.remove_footer()

        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        file_name, path = generated_file()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person_info.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person_info.lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(person_info.email)
        self.element_is_visible(self.locators.GENDER).click()

        self.element_is_visible(self.locators.MOBILE).send_keys(person_info.mobile)
        Uu = {1: "Hindi", 2: "English", 3: "Maths", 4: "Physics", 5: "Chemistry", 6: "Biology", 7: "Computer Science",
              8: "Commerce", 9: "Accounting", 10: "Economics", 11: "Arts", 12: "Social Studies", 13: "History",
              14: "Civics"}
        for x in range(random.randint(1, 5)):
            subject_list = Uu[random.randint(1, 14)]
            self.element_is_visible(self.locators.SUBJECT).send_keys(subject_list)
            # print(subject_list)
            x += 1
            # self.element_is_visible(self.locators.SUBJECT).send_keys('Maths')
            self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        time.sleep(2)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person_info.current_address)

        state_list = {1: "NCR", 2: "Uttar Pradesh", 3: "Haryana", 4: "Rajasthan"}
        selected_state = state_list[random.randint(1, 4)]
        print("=**********=")
        print(selected_state)

        self.go_to_element(self.element_is_visible(self.locators.SELECT_STATE))
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(selected_state)
        # time.sleep(3)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)

        self.element_is_visible(self.locators.SELECT_CITY).click()
        for i in range(random.randint(1, 4)):
            time.sleep(2)
            self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.DOWN)
            print('i= '+str(i))
            i += 1
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        city_select = self.element_is_present(self.locators.SELECT_CITY).text
        print("VVVVVV"*10)
        print(city_select)
        print("++++"*40)

        self.driver.execute_script("document.body.style.zoom = '0.85'")
        self.go_to_element(self.element_is_visible(self.locators.SUBMIT))
        self.element_is_visible(self.locators.SUBMIT).send_keys(Keys.RETURN)
        return person_info

    def form_result(self):
        result_list = self.element_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data
