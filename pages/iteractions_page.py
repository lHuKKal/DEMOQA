import random

from locators.iteractions_locators import SortableLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortableLocators

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)

        return [item.text for item in item_list]

    def change_list_order(self, count_of_times):
        self.element_is_visible(self.locators.LIST_TAB).click()
        order_before = self.get_sortable_items(self.locators.LIST_TAB_ITEMS)

        count = count_of_times
        item_list = random.sample(self.elements_are_present(self.locators.LIST_TAB_ITEMS), 6)
        total_index = len(item_list) - 1
        while count != 0:
            item_move_from = item_list[random.randint(0, total_index)]
            item_move_to = item_list[random.randint(0, total_index)]
            self.action_drag_and_drop_to_element(item_move_from, item_move_to)
            count -= 1

        order_after = self.get_sortable_items(self.locators.LIST_TAB_ITEMS)

        return order_before, order_after

    def change_grid_order(self, count_of_times):
        self.element_is_visible(self.locators.GRID_TAB).click()
        order_before = self.get_sortable_items(self.locators.GRID_TAB_ITEMS)

        count = count_of_times
        item_list = random.sample(self.elements_are_present(self.locators.GRID_TAB_ITEMS), 9)
        total_index = len(item_list) - 1
        while count != 0:
            item_move_from = item_list[random.randint(0, total_index)]
            item_move_to = item_list[random.randint(0, total_index)]
            self.action_drag_and_drop_to_element(item_move_from, item_move_to)
            count -= 1

        order_after = self.get_sortable_items(self.locators.GRID_TAB_ITEMS)

        return order_before, order_after


