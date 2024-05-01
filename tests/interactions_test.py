from pages.iteractions_page import SortablePage, SelectablePage, ResizablePage


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

