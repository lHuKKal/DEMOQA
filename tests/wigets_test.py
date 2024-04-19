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
        several_colors = auto_complete_page.select_several_color_for_multi_field(11)
        one_color = auto_complete_page.select_single_color()
        result_some_colors = auto_complete_page.check_selected_several_colors()
        result_single_color = auto_complete_page.check_selected_one_color()
        result_after_clear_for_check, removed_value = auto_complete_page.check_remove_value_from_multi_field(2)
        print(removed_value)

        assert several_colors == result_some_colors, "Selected colors is not matched with result"
        assert one_color == result_single_color, "Selected color is not matched with result"
        assert removed_value not in result_after_clear_for_check, f"Value '{removed_value}' is not removed from the Multi field"

        result_empty_multiple_field = auto_complete_page.check_cleared_field()
        assert result_empty_multiple_field is True, "Multiple color field is not cleared"
