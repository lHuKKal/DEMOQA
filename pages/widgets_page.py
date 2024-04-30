import random
import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from generator.generator import multiple_color, generate_date, random_year_between_five_years, \
    select_random_not_current_year_and_month, not_today_day, \
    select_one_from_select_menu_page, select_value_from_select_menu_page, values_for_multiselect_field
from locators.widgets_locators import AccordianLocators, AutoCompleteLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators
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
            raise ValueError(f"You selected counts more than available options. Should be {len(all_colors)} or less")

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

        self.select_value_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.select_value_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)

        value_date_after = input_date.get_attribute('value')

        return value_date_before, value_date_after

    def select_date_by_text(self):
        random_year, random_month, random_day = random_year_between_five_years()
        date_before = self.element_is_visible(self.locators.DATE_INPUT).get_attribute('value')

        self.element_is_visible(self.locators.DATE_INPUT).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.DATE_INPUT).send_keys(Keys.DELETE)
        self.element_is_visible(self.locators.DATE_INPUT).send_keys(
            random_year + "/" + random_month + "/" + random_day)
        self.element_is_visible(self.locators.DATE_INPUT).send_keys(Keys.ENTER)

        date_after = self.element_is_visible(self.locators.DATE_INPUT).get_attribute('value')

        return date_before, date_after

    def select_date_and_time(self):
        month_name, year = select_random_not_current_year_and_month()
        day = not_today_day()
        date_and_time_input = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)

        date_and_time_value_before = date_and_time_input.get_attribute('value')

        date_and_time_input.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, month_name)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, day)

        date_and_time_value_after = date_and_time_input.get_attribute('value')

        return date_and_time_value_before, date_and_time_value_after


class SliderPage(BasePage):
    locators = SliderPageLocators

    def random_slider_value(self):
        slider_value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        slider_value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')

        return slider_value_before, slider_value_after


class ProgresBarPage(BasePage):
    locators = ProgressBarLocators

    def check_progress_bar(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        self.element_is_visible(self.locators.START_BUTTON).click()
        time.sleep(11)
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        self.element_is_visible(self.locators.RESET_BUTTON).click()
        time.sleep(0.1)
        value_after_reset = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')

        return value_before, value_after, value_after_reset


class TabsPage(BasePage):
    locators = TabsPageLocators

    def check_tabs(self, tab_name):
        tabs = {
            'What':
                {'title': self.locators.WHAT_TAB,
                 'text': self.locators.WHAT_TAB_TEXT},
            'Origin': {'title': self.locators.ORIGIN_TAB,
                       'text': self.locators.ORIGIN_TAB_TEXT},
            'Use': {'title': self.locators.USE_TAB,
                    'text': self.locators.USE_TAB_TEXT},
            'More': {'title': self.locators.MORE_TAB}
        }

        tab_button = self.element_is_visible(tabs[tab_name]['title'])
        # Для вкладки More, т.к. она не кликабельна и делаем Except
        try:
            tab_button.click()
        except ElementClickInterceptedException:
            return True
        tab_text = self.element_is_visible(tabs[tab_name]['text']).text

        return tab_button.text, len(tab_text)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators

    def get_text_from_tool_tips(self, hover_element, wait_element):
        element = self.element_is_present(hover_element)
        self.action_move_to_element(element)
        time.sleep(0.5)
        self.element_is_visible(wait_element)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIP_INNER)
        text = tool_tip_text.text

        return text

    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.HOVER_ME_BUTTON,
                                                            self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.HOVER_ME_INPUT, self.locators.TOOL_TIP_INPUT)
        tool_tip_text_contrary_link = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK,
                                                                   self.locators.TOOL_TIP_CONTRARY_LINK)
        tool_tip_text_section_link = self.get_text_from_tool_tips(self.locators.SECTION_LINK,
                                                                  self.locators.TOOL_TIP_SECTION_LINK)

        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary_link, tool_tip_text_section_link


class MenuPage(BasePage):
    locators = MenuPageLocators

    def check_items(self):
        item_list = self.elements_are_present(self.locators.ITEM_LIST)
        data = []

        for item in item_list:
            self.action_move_to_element(item)
            text = item.text
            data.append(text)
        return data


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators

    def select_values_field(self):
        values = select_value_from_select_menu_page()

        select_value_for_select_value_field = random.choice(list(values.keys()))
        self.element_is_visible(self.locators.SELECT_VALUE_FIELD).send_keys(select_value_for_select_value_field)
        self.element_is_visible(self.locators.SELECT_VALUE_FIELD).send_keys(Keys.ENTER)

        return select_value_for_select_value_field

    def select_one_field(self):
        values = select_one_from_select_menu_page()

        select_value_for_select_one_field = random.choice(list(values.keys()))
        self.element_is_visible(self.locators.SELECT_ONE_FIELD).send_keys(select_value_for_select_one_field)
        self.element_is_visible(self.locators.SELECT_ONE_FIELD).send_keys(Keys.ENTER)

        return select_value_for_select_one_field

    def select_random_value_for_old_field(self):
        field_locator = self.locators.OLD_STYLE_SELECT_MENU_LIST
        values = self.elements_are_present(self.locators.OLD_STYLE_SELECT_MENU_LIST)
        values_list = []

        for item in values:
            text = item.text
            values_list.extend(text.splitlines())

        random_value = values_list[random.randint(0, 10)]
        self.element_is_visible(field_locator).click()
        self.select_value_by_text(field_locator, random_value)

        return random_value

    def select_random_value_for_standard_field(self):
        field_locator = self.locators.STANDARD_MULTI_SECTION_LIST
        values = self.elements_are_present(self.locators.STANDARD_MULTI_SECTION_LIST)
        values_list = []

        for item in values:
            text = item.text
            values_list.extend(text.splitlines())

        total_index = len(values_list) - 1

        random_value = values_list[random.randint(0, total_index)]
        self.select_value_by_text(field_locator, random_value)

        return random_value

    def select_values_for_multiselect_field(self, count_values_for_select):
        colors = values_for_multiselect_field()
        count = count_values_for_select
        selected_values = []

        if count > len(colors):
            # Максимум 4
            raise ValueError(f"You selected counts more than available options. Should be {len(colors)} or less")

        while count != 0:
            random_color = random.choice(list(colors.keys()))
            self.element_is_visible(self.locators.MULTI_SELECT_FIELD).send_keys(random_color)
            self.element_is_visible(self.locators.MULTI_SELECT_FIELD).send_keys(Keys.ENTER)
            count -= 1
            colors.pop(random_color)
            selected_values.append(random_color)
            self.element_is_visible(self.locators.MULTI_SELECT_FIELD).send_keys(Keys.ESCAPE)

        return selected_values

    def check_result(self):
        select_value_field_result = self.element_is_visible(self.locators.SELECT_VALUE_FIELD_RESULT).text
        select_one_field_result = self.element_is_visible(self.locators.SELECT_ONE_FIELD_RESULT).text
        old_style_field_result = self.element_is_visible(self.locators.OLD_STYLE_SELECT_MENU_LIST_RESULT).text
        standard_field_result = self.element_is_visible(self.locators.STANDARD_MULTI_SECTION_LIST_RESULT).text

        return select_value_field_result, select_one_field_result, old_style_field_result, standard_field_result

    # Так как на сайте, кривой локатор для поля "Multiselect drop down"
    # Приходится использовать данный костыль, для взятия данных для корректной проверки
    def check_result_for_multi_field(self):
        multi_select = self.elements_are_visible(self.locators.MULTI_SELECT_FIELD_RESULT)
        multi_select_result_result = []

        for item in multi_select:
            text = item.text
            multi_select_result_result.extend(text.splitlines())

        text = [item.replace(' option', '').replace('selected.', '').replace('Nos', '') for item in multi_select_result_result]

        # Удаляем первый индекс для корректного сравнения (почему-то берет не введенное значение из поля)
        text.pop(0)

        # Удаляем пустые строки и пробелы в начале и конце строк
        text = [item.strip() for item in text if item.strip()]

        return text


