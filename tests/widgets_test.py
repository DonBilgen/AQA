from pages.widgets_page import AccordianPage


class TestWidgets:

    class TestAccordianPage:

        def test_accordian(self, driver):
            # must ADBLOCK!!!
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            title_1, content_1 = accordian_page.check_accordian('first')

            title_2, content_2 = accordian_page.check_accordian('second')

            title_3, content_3 = accordian_page.check_accordian('third')

            assert title_1 == 'What is Lorem Ipsum?' and content_1 > 0, 'Error section 1'
            assert title_2 == 'Where does it come from?' and content_2 > 0, 'Error section 2'
            assert title_3 == 'Why do we use it?' and content_3 > 0, 'Error section 3'


