import time

from pages.widgets_page import AccordianPage, AutoCompletePage


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


class TestAutoComplete:

    def test_auto_complete_page(self, driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        selected_colors = auto_complete_page.select_some_multiple_color(11)
        one_color = auto_complete_page.select_color()
        result_some_colors = auto_complete_page.check_selected_colors()
        result_single_color = auto_complete_page.check_selected_one_color()

        assert selected_colors == result_some_colors, "Selected colors is not matched with result"
        assert one_color == result_single_color, "Selected color is not matched with result"

