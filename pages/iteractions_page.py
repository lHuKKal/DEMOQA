import random

from locators.iteractions_locators import SortableLocators, SelectablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortableLocators

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)

        return [item.text for item in item_list]

    def move_to_random_element(self, element, count_of_times):
        count = count_of_times
        list_elements = self.elements_are_visible(element)
        total_elements = len(list_elements)
        item_list = random.sample(self.elements_are_present(element), total_elements)
        total_index = len(item_list) - 1

        while count != 0:
            item_move_from = item_list[random.randint(0, total_index)]
            item_move_to = item_list[random.randint(0, total_index)]
            self.action_drag_and_drop_to_element(item_move_from, item_move_to)
            count -= 1

    def change_list_order(self):
        self.element_is_visible(self.locators.LIST_TAB).click()

        order_before = self.get_sortable_items(self.locators.LIST_TAB_ITEMS)
        self.move_to_random_element(self.locators.LIST_TAB_ITEMS, 4)
        order_after = self.get_sortable_items(self.locators.LIST_TAB_ITEMS)

        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.GRID_TAB).click()

        order_before = self.get_sortable_items(self.locators.GRID_TAB_ITEMS)
        self.move_to_random_element(self.locators.GRID_TAB_ITEMS, 4)
        order_after = self.get_sortable_items(self.locators.GRID_TAB_ITEMS)

        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators

    def select_random_value(self, element, select_count_values):
        list_values = (self.elements_are_visible(element))

        indexes = list(range(len(list_values)))
        clicked_values = []
        count = select_count_values

        if count > len(list_values):
            raise ValueError(f"You selected counts more than available options. Should be {len(list_values)} or less")

        while count != 0:
            random_index = random.choice(indexes)
            random_element = list_values[random_index]
            random_element.click()
            count -= 1
            text = random_element.text
            clicked_values.append(text)
            indexes.remove(random_index)

        return clicked_values

    def select_values_in_the_list_tab(self):
        self.element_is_visible(self.locators.LIST_TAB).click()

        clicked_values = self.select_random_value(self.locators.LIST_TAB_ITEMS, 2)
        list_tab_result = self.check_result_list_and_grid_tabs(self.locators.LIST_TAB_SELECTED_ITEMS)

        # Необходимо тут применить sorted, т.к. значение добавляются в случайном порядке в список list_clicked_values
        # Sorted используется для выполнения корректного assert
        return sorted(clicked_values), sorted(list_tab_result)

    def select_values_in_the_grid_tab(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        grid_clicked_values = self.select_random_value(self.locators.GRID_TAB_ITEMS, 5)
        grid_tab_result = self.check_result_list_and_grid_tabs(self.locators.GRID_TAB_SELECTED_ITEMS)

        # Необходимо тут применить sorted, т.к. значение добавляются в случайном порядке в список grid_clicked_values
        # Sorted используется для выполнения корректного assert
        return sorted(grid_clicked_values), sorted(grid_tab_result)

    def check_result_list_and_grid_tabs(self, element):
        item_list = self.elements_are_visible(element)

        return [item.text for item in item_list]
