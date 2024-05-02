from pages.iteractions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


class TestInteractions:
    class TestSortable:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_order_before, list_order_after = sortable_page.change_list_order()
            grid_order_before, grid_order_after = sortable_page.change_grid_order()

            assert list_order_before != list_order_after, "The List tab is not sorted"
            assert grid_order_before != grid_order_after, "The Grid tab is not sorted"

    class TestSelectable:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            list_selected_values, list_tab_result = selectable_page.select_values_in_the_list_tab()
            grid_selected_values, grid_tab_result = selectable_page.select_values_in_the_grid_tab()

            assert list_selected_values == list_tab_result, "Selected values in the 'List' tab don't match or selected incorrectly"
            assert grid_selected_values == grid_tab_result, "" "Selected values in the 'Grid' tab don't match or selected incorrectly"

    class TestResizable:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            resizable_box_max_size, resizable_box_min_size = resizable_page.change_size_resizable_box()
            resizable_max_size, resizable_min_size = resizable_page.change_size_resizable()

            assert resizable_box_max_size == ('500px', '300px'), "Max resizable not equal '500px', '300px'"
            assert resizable_box_min_size == ('150px', '150px'), "Min resizable not equal '500px', '300px'"
            assert resizable_max_size != resizable_min_size, "Size is not changed for Resizable object"

    class TestDroppable:

        def test_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            after_drop = droppable_page.drag_to_the_simple_tab()
            after_not_acceptable_drop, after_acceptable_drop = droppable_page.drag_to_the_accept_tab()
            (after_drag_to_not_greedy_box, after_drag_to_greedy_box,
             after_drag_to_up_greedy_box) = droppable_page.drag_and_drop_in_the_prevent_propagation_tab()
            (element_is_dropped, get_px_will_reverent_after_drop, get_px_not_reverent,
             get_px_not_reverent_after_drop) = droppable_page.drag_and_drop_in_the_revent_draggable_tab()

            # Accept tab
            assert after_drop == 'Dropped!', "Element is not dragged in the Simple tab"
            # Simple tab
            assert after_not_acceptable_drop == 'Drop here', "Not accepted element is accepted in the Accept tab"
            assert after_acceptable_drop == 'Dropped!', "Accepted element is not accepted in the Accept tab"
            # Prevent Propagation tab
            assert after_drag_to_not_greedy_box == ['Dropped!', 'Dropped!'], "Element is not dragged in the 'not greedy inner box' of Prevent Propagation tab"
            assert after_drag_to_greedy_box == ['Outer droppable', 'Dropped!'], "Element is not dragged in the 'greedy inner box' of Prevent Propagation tab"
            assert after_drag_to_up_greedy_box == ['Dropped!', 'Dropped!'], "Element is not dragged up in the 'greedy box' of Prevent Propagation tab"
            # Revert Draggable tab
            assert element_is_dropped == 'Dropped!', "Element is not dragged in the 'Revent Draggable' tab tab"
            assert get_px_will_reverent_after_drop == [' left: 0px', ' top: 0px'], "The 'Will Reverent' element is not back to position"
            assert get_px_not_reverent == get_px_not_reverent_after_drop, "The 'Not Reverent' element is not back to position"

    class TestDraggable:

        def test_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before_position, after_position = draggable_page.draggable_in_the_simple_tab()
            (top_x_position_before, top_x_position_after, left_x_position_before,
             left_x_position_after) = draggable_page.dragg_only_x_in_the_axis_restricted_tab()
            (top_y_position_before, top_y_position_after, left_y_position_before,
             left_y_position_after) = draggable_page.dragg_only_y_in_the_axis_restricted_tab()

            # Simple tab
            assert before_position != after_position, "Element is not dragged"
            # Axis Restricted tab - Only X element
            assert top_x_position_before and top_x_position_after == "top: 0px", "The 'Only X' element is moved to the top, but should not be moved"
            assert left_x_position_before != left_x_position_after, "The 'Only X' element is not moved to the left"
            # Axis Restricted tab - Only X element
            assert top_y_position_before != top_y_position_after
            assert left_y_position_before and left_y_position_after == "left: 0px"
