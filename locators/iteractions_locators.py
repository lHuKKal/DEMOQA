from selenium.webdriver.common.by import By


class SortableLocators:
    # Tabs
    LIST_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    GRID_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")

    # List items
    LIST_TAB_ITEMS = (
        By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']")
    GRID_TAB_ITEMS = (
        By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']")


class SelectablePageLocators:
    # Tabs
    LIST_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    GRID_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")

    # List items
    LIST_TAB_ITEMS = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item list-group-item-action']")
    GRID_TAB_ITEMS = (By.CSS_SELECTOR, "li[class='list-group-item list-group-item-action']")

    # Selected items
    LIST_TAB_SELECTED_ITEMS = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item active list-group-item-action']")
    GRID_TAB_SELECTED_ITEMS = (By.CSS_SELECTOR, "li[class='list-group-item active list-group-item-action']")


class ResizablePageLocators:
    FIRST_WINDOW_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
    FIRST_WINDOW_HANDLE = (By.CSS_SELECTOR, "div[class='constraint-area'] span[class='react-resizable-handle react-resizable-handle-se']")

    SECOND_WINDOW_BOX = (By.CSS_SELECTOR, "div[id='resizable']")
    SECOND_WINDOW_HANDLE = (By.CSS_SELECTOR, "div[class='resizable-nolimit mt-4'] span[class='react-resizable-handle react-resizable-handle-se']")
