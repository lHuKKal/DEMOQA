from pages.iteractions_page import SortablePage


class TestInteractions:

    class TestSortable:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_order_before, list_order_after = sortable_page.change_list_order(4)
            grid_order_before, grid_order_after = sortable_page.change_grid_order(4)

            assert list_order_before != list_order_after, "The List tab is not sorted"
            assert grid_order_before != grid_order_after, "The Grid tab is not sorted"

    class TestSelectable:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()

