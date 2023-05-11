import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage


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

            key_person = web_table_page.add_new_person()[random.randint(0, 5)]
            print(key_person)
            web_table_page.search_some_person(str(key_person))
            table_result = web_table_page.check_search_person()
            print(table_result)
            assert key_person in table_result

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            # print(' ')
            # print(lastname)
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            time.sleep(3)
            row = web_table_page.check_search_person()
            # print(age)
            # print(row)
            assert age in row, "Error change info"

        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_delete()
            assert text == 'No rows found', "Error Delete"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            print("** **" * 33)
            print(count)
            assert count == [5, 10, 20, 25, 50, 100], "Error change count rows"

    class TestButtonPage:
        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            print(double)
            right = button_page.click_on_different_button('right')
            print(right)
            click = button_page.click_on_different_button('click')
            print(click)
            assert double == 'You have done a double click', "Error double click"
            assert right == 'You have done a right click', "Error right click"
            assert click == 'You have done a dynamic click', "Error dynamic click"

    class TestLinkPage:
        def test_check_link(self, driver):
            link_page = LinksPage(driver, 'https://demoqa.com/links')
            link_page.open()
            href_link, current_url = link_page.check_new_tab_simple_link()
            assert href_link == current_url, "Error link url incorrect"

        def test_broken_link(self, driver):
            link_page = LinksPage(driver, 'https://demoqa.com/links')
            link_page.open()
            response_code = link_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "Error code not 400"

        def test_not_found_link(self, driver):
            link_page = LinksPage(driver, 'https://demoqa.com/links')
            link_page.open()
            response_code = link_page.check_not_found_link('https://demoqa.com/invalid-url')
            assert response_code == 404, "Error url not 404"

    class TestUploadAndDownload:

        def test_upload_file(self, driver):
            upload_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            file_name, result_file = upload_page.upload_file()
            assert file_name == result_file, "Error file upload"


        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, "Error download file"
