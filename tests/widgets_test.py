import time

import allure

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgresBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


@allure.suite("Testing the Widgets section")
class TestWidgetsSection:
    @allure.feature("Testing Accordian interface")
    class TestAccordian:
        @allure.title("Testing expand elements")
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

    @allure.feature("Testing the Auto Complete interface")
    class TestAutoComplete:
        @allure.title("Testing the select colors in the data fields")
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

    @allure.feature("Testing the Date Picker interface")
    class TestDateTime:
        @allure.title("Testing select date in the Select Date and the Date and Time fields")
        def test_date_time(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            # value_date_before, value_date_after = date_picker_page.select_date()
            value_date_before, value_date_after = date_picker_page.select_date_by_text()
            date_and_time_value_before, date_and_time_value_after = date_picker_page.select_date_and_time()

            assert value_date_before != value_date_after, "Date is not changed in the 'Select Date' field"
            assert date_and_time_value_before != date_and_time_value_after, "Date is not changed in the 'Date And Time' field"

    @allure.feature("Testing the Slider interface and Progress Bar interface")
    class TestSlider:
        @allure.title("Testing the slide function")
        def test_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            slider_value_before, slider_value_after = slider_page.random_slider_value()

            assert slider_value_before != slider_value_after, "Slider value has not been changed"

        @allure.title("Testing the progress bar function")
        def test_progress_bar(self, driver):
            progress_bar_page = ProgresBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()
            value_before, value_after, value_after_reset = progress_bar_page.check_progress_bar()

            assert value_before != value_after, "Progress operation is not performed"
            assert value_after_reset == '0', "Progress bar has been not resset"

    @allure.feature("Testing the Tabs interface")
    class TestTabs:
        @allure.title("Testing the What, Origin, Use and More tabs")
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            origin_tab, origin_tab_text = tabs_page.check_tabs('Origin')
            use_text, use_text_tab = tabs_page.check_tabs('Use')
            what_tab, what_tab_text = tabs_page.check_tabs('What')
            more_tab = tabs_page.check_tabs('More')

            assert what_tab == 'What' and what_tab_text > 0, "'What' is not opened"
            assert origin_tab == 'Origin' and origin_tab_text > 0, "'Origin' tab is not opened"
            assert use_text == 'Use' and use_text_tab > 0, "'Use' tab is not opened"
            assert more_tab is True, "'More' tab is clickable"

    @allure.feature('Testing the Tool Tips interface')
    class TestToolTips:
        @allure.title("Testing that the tool tip is displayed for elements")
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tool_tips_page.open()
            tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary_link, tool_tip_text_section_link = tool_tips_page.check_tool_tips()

            assert tool_tip_text_button == "You hovered over the Button", "Tooltip for the button is not displayed"
            assert tool_tip_text_field == "You hovered over the text field", "Tooltip for the field is not displayed"
            assert tool_tip_text_contrary_link == "You hovered over the Contrary", "Tooltip for the contrary link is not displayed"
            assert tool_tip_text_section_link == "You hovered over the 1.10.32", "Tooltip for the section link is not displayed"

    @allure.feature("Testing the Menu interface")
    class TestMenu:
        @allure.title("Testing the menu items")
        def test_menu(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu#")
            menu_page.open()
            data = menu_page.check_items()

            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3']

    @allure.feature("Testing the Select Menu interface")
    class TestSelectMenu:
        @allure.title("Fill all data fields in the Select Menu data form")
        def test_select_menu(self, driver):
            select_menu_page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
            select_menu_page.open()
            value_field = select_menu_page.select_values_field()
            one_field = select_menu_page.select_one_field()
            old_value = select_menu_page.select_random_value_for_old_field()
            standard_value = select_menu_page.select_random_value_for_standard_field()
            multiselect_field = select_menu_page.select_values_for_multiselect_field(2)
            select_value_field_result, select_one_field_result, old_style_field_result, standard_field_result = select_menu_page.check_result()
            multiselect_field_result = select_menu_page.check_result_for_multi_field()

            assert value_field == select_value_field_result, "Incorrect value is selected or not selected at all in the 'Select Value' field"
            assert one_field == select_one_field_result, "Incorrect value is selected or not selected at all in the 'Select One' field"
            assert multiselect_field == multiselect_field_result, "Incorrect value is selected or not selected at all in the 'Multiselect drop down' field"
            assert old_value in old_style_field_result, "Incorrect value is selected or not selected at all in the 'Old Style Select Menu' field"
            assert standard_value in standard_field_result, "Incorrect value is selected or not selected at all in the 'Standard multi select' field"
