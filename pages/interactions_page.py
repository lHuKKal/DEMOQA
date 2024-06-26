import random
import time

import allure

from locators.iteractions_locators import SortableLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DraggablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortableLocators

    @allure.step("Get sortable items")
    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)

        return [item.text for item in item_list]

    @allure.step("Move to random element")
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

    @allure.step("Change the list order")
    def change_list_order(self):
        self.element_is_visible(self.locators.LIST_TAB).click()

        order_before = self.get_sortable_items(self.locators.LIST_TAB_ITEMS)
        self.move_to_random_element(self.locators.LIST_TAB_ITEMS, 4)
        order_after = self.get_sortable_items(self.locators.LIST_TAB_ITEMS)

        return order_before, order_after

    @allure.step("Change the grid order")
    def change_grid_order(self):
        self.element_is_visible(self.locators.GRID_TAB).click()

        order_before = self.get_sortable_items(self.locators.GRID_TAB_ITEMS)
        self.move_to_random_element(self.locators.GRID_TAB_ITEMS, 4)
        order_after = self.get_sortable_items(self.locators.GRID_TAB_ITEMS)

        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators

    @allure.step("Select random value")
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

    @allure.step("Select value in the List tab")
    def select_values_in_the_list_tab(self):
        self.element_is_visible(self.locators.LIST_TAB).click()

        clicked_values = self.select_random_value(self.locators.LIST_TAB_ITEMS, 2)
        list_tab_result = self.check_result_list_and_grid_tabs(self.locators.LIST_TAB_SELECTED_ITEMS)

        # Необходимо тут применить sorted, т.к. значение добавляются в случайном порядке в список list_clicked_values
        # Sorted используется для выполнения корректного assert
        return sorted(clicked_values), sorted(list_tab_result)

    @allure.step("Select value in the Grid tab")
    def select_values_in_the_grid_tab(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        grid_clicked_values = self.select_random_value(self.locators.GRID_TAB_ITEMS, 5)
        grid_tab_result = self.check_result_list_and_grid_tabs(self.locators.GRID_TAB_SELECTED_ITEMS)

        # Необходимо тут применить sorted, т.к. значение добавляются в случайном порядке в список grid_clicked_values
        # Sorted используется для выполнения корректного assert
        return sorted(grid_clicked_values), sorted(grid_tab_result)

    @allure.step("Get result in the List and Grid tab")
    def check_result_list_and_grid_tabs(self, element):
        item_list = self.elements_are_visible(element)

        return [item.text for item in item_list]


class ResizablePage(BasePage):
    locators = ResizablePageLocators

    @allure.step("Get width and height of box")
    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')

        return width, height

    @allure.step("Get max and min size olf box")
    def get_max_min_size(self, element):
        size = self.element_is_visible(element)
        size_value = size.get_attribute('style')

        return size_value

    @allure.step("Change size for Resizable box")
    def change_size_resizable_box(self):
        box_element = self.element_is_visible(self.locators.FIRST_WINDOW_HANDLE)

        self.action_drag_and_drop_by_offset(box_element, 300, 200)
        resizable_box_max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.FIRST_WINDOW_BOX))

        self.action_drag_and_drop_by_offset(box_element, -500, -300)
        resizable_box_min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.FIRST_WINDOW_BOX))

        return resizable_box_max_size, resizable_box_min_size

    @allure.step("Change size of box")
    def change_size_resizable(self):
        resizable_element = self.element_is_visible(self.locators.SECOND_WINDOW_HANDLE)
        self.scroll_to_element(self.locators.SECOND_WINDOW_HANDLE)

        self.action_drag_and_drop_by_offset(resizable_element,
                                            random.randint(100, 300), random.randint(1, 300))
        resizable_max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.SECOND_WINDOW_BOX))

        self.action_drag_and_drop_by_offset(resizable_element,
                                            random.randint(-200, -1), random.randint(-200, -1))
        resizable_min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.SECOND_WINDOW_BOX))

        return resizable_max_size, resizable_min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators

    @allure.step("Drag and drop in the Simple tab")
    def drag_to_the_simple_tab(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_locator = self.element_is_visible(self.locators.DRAG_ME_ELEMENT)
        drop_element = self.element_is_visible(self.locators.DROP_SIMPLE_TAB_ELEMENT)

        self.action_drag_and_drop_to_element(drag_locator, drop_element)
        after_drop = drop_element.text

        return after_drop

    @allure.step("Drag and drop in the Accept tab")
    def drag_to_the_accept_tab(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable_element = self.element_is_visible(self.locators.ACCEPTABLE_ELEMENT)
        not_acceptable_element = self.element_is_visible(self.locators.NOT_ACCEPTABLE_ELEMENT)
        drop_element = self.element_is_visible(self.locators.DROP_ACCEPT_TAB_ELEMENT)

        self.action_drag_and_drop_to_element(not_acceptable_element, drop_element)
        after_not_acceptable_drop = drop_element.text

        self.action_drag_and_drop_to_element(acceptable_element, drop_element)
        after_acceptable_drop = drop_element.text

        return after_not_acceptable_drop, after_acceptable_drop

    @allure.step("Drag and drop in the Prevent Propagation tab")
    def drag_and_drop_in_the_prevent_propagation_tab(self):
        self.element_is_visible(self.locators.PREVENT_PROPOGATION_TAB).click()
        drag_element = self.element_is_visible(self.locators.DRAG_ME_PREVENT_TAB_ELEMENT)
        not_greedy_drop_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX)
        greedy_drop_box = self.element_is_visible(self.locators.GREEDY_DROP_BOX)

        self.action_drag_and_drop_to_element(drag_element, not_greedy_drop_box)
        after_drag_to_not_greedy_box = not_greedy_drop_box.text

        self.action_drag_and_drop_to_element(drag_element, greedy_drop_box)
        after_drag_to_greedy_box = greedy_drop_box.text
        self.action_drag_and_drop_by_offset(drag_element, 0, -98)
        after_drag_to_up_greedy_box = greedy_drop_box.text

        return (after_drag_to_not_greedy_box.splitlines(), after_drag_to_greedy_box.splitlines(),
                after_drag_to_up_greedy_box.splitlines())

    @allure.step("Drag and drop in the Revent Draggable tab")
    def drag_and_drop_in_the_revent_draggable_tab(self):
        self.element_is_visible(self.locators.REVERENT_DRAGGABLE_TAB).click()
        will_reverent = self.element_is_visible(self.locators.WILL_REVERENT)
        not_reverent = self.element_is_visible(self.locators.NOT_REVERENT)
        drop_box = self.element_is_visible(self.locators.DROP_REVERENT_BOX)

        self.action_drag_and_drop_to_element(will_reverent, drop_box)
        time.sleep(1)
        get_px_will_reverent_after_drop = self.get_px(will_reverent)
        element_is_dropped = drop_box.text

        self.action_drag_and_drop_to_element(not_reverent, drop_box)
        get_px_not_reverent = self.get_px(not_reverent)
        self.action_drag_and_drop_by_offset(not_reverent, -300, 0)
        time.sleep(1)
        get_px_not_reverent_after_drop = self.get_px(not_reverent)

        return element_is_dropped, get_px_will_reverent_after_drop, get_px_not_reverent, get_px_not_reverent_after_drop

    @allure.step("Get px of element")
    def get_px(self, element):
        locator = element
        attribute = locator.get_attribute('style')
        left = attribute.split(';')[1]
        top = attribute.split(';')[2]

        return [left, top]


class DraggablePage(BasePage):
    locators = DraggablePageLocators

    @allure.step("Get before and after changing position")
    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        before_position = self.get_px(drag_element)
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = self.get_px(drag_element)

        return before_position, after_position

    @allure.step("Get px of element")
    def get_px(self, element):
        locator = element
        attribute = locator.get_attribute('style')
        left = attribute.split(';')[1].strip()
        top = attribute.split(';')[2].strip()

        return [left, top]

    @allure.step("Drag element in the Simple tab")
    def draggable_in_the_simple_tab(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_me_element = self.element_is_visible(self.locators.DRAG_ME_ELEMENT)

        before_position, after_position = self.get_before_and_after_position(drag_me_element)

        return before_position, after_position

    @allure.step("Drag Only X element in the Axis Restricted tab")
    def dragg_only_x_in_the_axis_restricted_tab(self):
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        drag_only_x = self.element_is_visible(self.locators.ONLY_X_ELEMENT)

        before_position, after_position = self.get_before_and_after_position(drag_only_x)
        top_x_position_before = before_position[1]
        top_x_position_after = after_position[1]
        left_x_position_before = before_position[0]
        left_x_position_after = after_position[0]

        return top_x_position_before, top_x_position_after, left_x_position_before, left_x_position_after

    @allure.step("Drag Only Y element in the axis restricted tab")
    def dragg_only_y_in_the_axis_restricted_tab(self):
        drag_only_y = self.element_is_visible(self.locators.ONLY_Y_ELEMENT)

        before_position, after_position = self.get_before_and_after_position(drag_only_y)
        top_y_position_before = before_position[1]
        top_y_position_after = after_position[1]
        left_y_position_before = before_position[0]
        left_y_position_after = after_position[0]

        return top_y_position_before, top_y_position_after, left_y_position_before, left_y_position_after
