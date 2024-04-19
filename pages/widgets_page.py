import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import multiple_color
from locators.widgets_locators import AccordianLocators, AutoCompleteLocators
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

    def select_some_multiple_color(self, count_of_colors):
        all_colors = multiple_color()
        count = count_of_colors
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

    def select_color(self):

        all_colors = multiple_color()
        random_color = random.choice(list(all_colors.keys()))

        self.element_is_visible(self.locators.SINGLE_TYPE_FIELD).click()
        self.element_is_visible(self.locators.SINGLE_TYPE_FIELD).send_keys(random_color)
        self.element_is_visible(self.locators.SINGLE_TYPE_FIELD).send_keys(Keys.ENTER)
        return random_color

    def check_selected_colors(self):

        multiple_colors = self.elements_are_visible(self.locators.MULTIPLE_TYPE_RESULT)
        result = []

        for text_color in multiple_colors:
            result.extend(text_color.text.splitlines())

        result_for_check = ', '.join(result)
        return result_for_check

    def check_selected_one_color(self):

        selected_single_color = self.element_is_present(self.locators.SINGE_TYPE_RESULT).text
        return selected_single_color

    def check_clear_field(self):

        self.element_is_visible(self.locators.MULTIPLE_TYPE_CLEAR_BUTTON).click()
        try:
            self.element_is_present(self.locators.MULTIPLE_TYPE_RESULT, 1)
        except TimeoutException:
            return True
        return False
