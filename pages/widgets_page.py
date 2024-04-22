import random
import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys

from generator.generator import multiple_color, generate_date, random_year_between_five_years, \
    select_random_not_current_year_and_month, not_today_day, faker_en
from locators.widgets_locators import AccordianLocators, AutoCompleteLocators, DatePickerPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianLocators

    def accordian_page(self):
        first_section = self.element_is_visible(self.locators.FIRST_SECTION)
        second_section = self.element_is_visible(self.locators.SECOND_SECTION)
        third_section = self.element_is_visible(self.locators.THIRD_SECTION)

        second_section.click()
        second_title = second_section.text
        second_accordian_text = self.element_is_visible(self.locators.SECOND_SECTION_TEXT).text
        third_section.click()
        third_title = third_section.text
        third_accordian_text = self.element_is_visible(self.locators.THIRD_SECTION_TEXT).text
        first_section.click()
        first_title = first_section.text
        first_accordian_text = self.element_is_visible(self.locators.FIRST_SECTION).text

        return first_title, len(first_accordian_text), second_title, len(second_accordian_text), third_title, len(
            third_accordian_text)


class AutoCompletePage(BasePage):
    locators = AutoCompleteLocators

    def select_several_color_for_multi_field(self, count_colors_for_select):
        all_colors = multiple_color()
        count = count_colors_for_select
        selected_values = []

        if count > len(all_colors):
            raise ValueError("You selected counts more than available options. Should be 11 or less")

        while count != 0:
            random_color = random.choice(list(all_colors.keys()))
            self.element_is_visible(self.locators.MULTIPLE_TYPE_FIELD).send_keys(random_color)
            self.element_is_visible(self.locators.MULTIPLE_TYPE_FIELD).send_keys(Keys.ENTER)
            count -= 1
            all_colors.pop(random_color)
            selected_values.append(random_color)

        result_for_check = ', '.join(selected_values)
        return result_for_check

    def select_single_color(self):

        all_colors = multiple_color()
        random_color = random.choice(list(all_colors.keys()))

        self.element_is_visible(self.locators.SINGLE_TYPE_FIELD).click()
        self.element_is_visible(self.locators.SINGLE_TYPE_FIELD).send_keys(random_color)
        self.element_is_visible(self.locators.SINGLE_TYPE_FIELD).send_keys(Keys.ENTER)
        return random_color

    def check_selected_several_colors(self):

        multiple_colors = self.elements_are_visible(self.locators.MULTIPLE_TYPE_RESULT)
        result = []

        for text_color in multiple_colors:
            result.extend(text_color.text.splitlines())

        result_for_check = ', '.join(result)
        return result_for_check

    def check_selected_one_color(self):

        selected_single_color = self.element_is_present(self.locators.SINGE_TYPE_RESULT).text
        return selected_single_color

    def check_remove_value_from_multi_field(self, number_of_colours_to_remove):
        selected_values = self.elements_are_visible(self.locators.MULTIPLE_TYPE_RESULT)
        count = number_of_colours_to_remove
        removed_values = []

        while count != 0:
            cleared_value = self.element_is_present(self.locators.MULTIPLE_TYPE_TAKE_CLEARED_VALUE).text
            self.element_is_visible(self.locators.MULTIPLE_TYPE_CLEAR_ONE_VALUE_BUTTON).click()
            count -= 1
            removed_values.append(cleared_value)

        cleared_values_for_check = ', '.join(removed_values)

        after_clear_result = []

        for text_color in selected_values:
            after_clear_result.extend(text_color.text.splitlines())

        after_clear_result_for_check = ', '.join(after_clear_result)

        return after_clear_result_for_check, cleared_values_for_check

    def check_cleared_field(self):

        self.element_is_visible(self.locators.MULTIPLE_TYPE_CLEAR_ALL_VALUE_BUTTON).click()
        try:
            self.element_is_present(self.locators.MULTIPLE_TYPE_RESULT, 1)
        except TimeoutException:
            return True
        return False


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators

    def select_date(self):
        date = next(generate_date())

        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()

        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)

        value_date_after = input_date.get_attribute('value')

        return value_date_before, value_date_after

    def select_date_by_text(self):
        random_year, random_month, random_day = random_year_between_five_years()
        date_before = self.element_is_visible(self.locators.DATE_INPUT).text

        self.element_is_visible(self.locators.DATE_INPUT).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.DATE_INPUT).send_keys(Keys.DELETE)
        self.element_is_visible(self.locators.DATE_INPUT).send_keys(
            random_year + "/" + random_month + "/" + random_day)
        self.element_is_visible(self.locators.DATE_INPUT).send_keys(Keys.ENTER)

        date_after = self.element_is_visible(self.locators.DATE_INPUT).text

        return date_before, date_after

    def select_date_and_time(self):
        month_name, year = select_random_not_current_year_and_month()
        day = not_today_day()
        date_and_time_input = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)

        date_and_time_value_date_before = date_and_time_input.get_attribute('value')

        date_and_time_input.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, month_name)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, day)

        date_and_time_value_date_after = date_and_time_input.get_attribute('value')

        return date_and_time_value_date_before, date_and_time_value_date_after
