from pages.widgets_page import AccordianPage


class TestAccordian:

    def test_accordian(self, driver):
        accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
        accordian_page.open()
        first_title, first_accordian_text, second_title, second_accordian_text, third_title, third_accordian_text = accordian_page.accordian_page()
        print(first_title)
        print(second_title)
        print(third_title)
        assert first_title == "What is Lorem Ipsum?" and first_accordian_text > 0, "First section is not opened or text not exist"
        assert second_title == 'Where does it come from?' and second_accordian_text > 0, "Second section is not opened or text not exist"
        assert third_title == 'Why do we use it?' and third_accordian_text > 0, "Third section is not opened or text not exist"
