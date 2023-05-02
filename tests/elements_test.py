import time

from pages.elements_page import TextBoxPage, CheckBoxPage


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
