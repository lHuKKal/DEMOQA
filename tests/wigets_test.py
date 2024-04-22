import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgresBarPage


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

        assert several_colors == result_some_colors, "Selected colors is not matched with result"
        assert one_color == result_single_color, "Selected color is not matched with result"
        assert removed_value not in result_after_clear_for_check, f"Value '{removed_value}' is not removed from the Multi field"

        result_empty_multiple_field = auto_complete_page.check_cleared_field()
        assert result_empty_multiple_field is True, "Multiple color field is not cleared"


class TestDateTime:

    def test_date_time(self, driver):
        date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        date_picker_page.open()
        # value_date_before, value_date_after = date_picker_page.select_date()
        value_date_before, value_date_after = date_picker_page.select_date_by_text()
        date_and_time_value_before, date_and_time_value_after = date_picker_page.select_date_and_time()

        assert value_date_before != value_date_after, "Date is not changed in the 'Select Date' field"
        assert date_and_time_value_before != date_and_time_value_after, "Date is not changed in the 'Date And Time' field"


class TestSlider:

    def test_slider(self, driver):
        slider_page = SliderPage(driver, "https://demoqa.com/slider")
        slider_page.open()
        slider_value_before, slider_value_after = slider_page.random_slider_value()

        assert slider_value_before != slider_value_after, "Slider value has not been changed"

    def test_progress_bar(self, driver):
        progress_bar_page = ProgresBarPage(driver, "https://demoqa.com/progress-bar")
        progress_bar_page.open()
        value_before, value_after, value_after_reset = progress_bar_page.check_progress_bar()

        assert value_before != value_after, "Progress operation is not performed"
        assert value_after_reset == '0', "Progress bar has been not resset"
