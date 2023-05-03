import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            #
            assert full_name == output_name, 'full name error'
            assert email == output_email, 'email error'
            assert current_address == output_current_address, 'current address error'
            assert permanent_address == output_permanent_address, 'permanent address error'

            # input_data = text_box_page.fill_all_fields()
            # output_data = text_box_page.check_filled_form()
            # assert input_data == output_data

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_data = check_box_page.get_checked_checkboxes()
            print('*' * 45)
            print(input_data)
            output_data = check_box_page.get_output_result()
            print('#' * 25)
            print(output_data)
            time.sleep(5)
            assert input_data == output_data, 'Error input/=output'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == "Yes", 'Error selected = Yes'
            assert output_impressive == "Impressive", 'Error selected = Impressive'
            assert output_no == "No", "!!!!Error select= NO!!!!!"

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            # input_new_person = list(web_table_page.add_new_person())
            input_new_person = web_table_page.add_new_person()
            # print(' ')
            # print(input_new_person)
            # print('***' * 25)
            output_new_person = web_table_page.check_add_new_person()
            # print(output_new_person)
            # time.sleep(5)
            # assert input_new_person == output_new_person, 'Error creating New person'
            assert input_new_person in output_new_person, 'Error into New person'

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            select_random = random.randint(0, 5)
            print(' ')
            print(select_random)
            key_person = web_table_page.add_new_person()[select_random]
            # key_person = web_table_page.add_new_person()[random.randint(0, 5)] # так не работает????
            print('== ==' * 33)
            print(key_person)
            web_table_page.search_some_person(str(key_person))
            # web_table_page.search_some_person(key_person)
            table_result = web_table_page.check_search_person()
            print('**** '*22)
            print(table_result)
            assert key_person in table_result
