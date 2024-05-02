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
    FIRST_WINDOW_HANDLE = (
        By.CSS_SELECTOR, "div[class='constraint-area'] span[class='react-resizable-handle react-resizable-handle-se']")

    SECOND_WINDOW_BOX = (By.CSS_SELECTOR, "div[id='resizable']")
    SECOND_WINDOW_HANDLE = (By.CSS_SELECTOR,
                            "div[class='resizable-nolimit mt-4'] span[class='react-resizable-handle react-resizable-handle-se']")


class DroppablePageLocators:
    # Simple tab
    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-simple']")
    DRAG_ME_ELEMENT = (By.CSS_SELECTOR, "div[id='draggable']")
    DROP_SIMPLE_TAB_ELEMENT = (By.CSS_SELECTOR, "div[id='simpleDropContainer'] div[id='droppable']")

    # Accept tab
    ACCEPT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']")
    ACCEPTABLE_ELEMENT = (By.CSS_SELECTOR, "div[id='acceptable']")
    NOT_ACCEPTABLE_ELEMENT = (By.CSS_SELECTOR, "div[id='notAcceptable']")
    DROP_ACCEPT_TAB_ELEMENT = (By.CSS_SELECTOR, "div[id='droppableExample-tabpane-accept'] div[id='droppable']")

    # Prevent Propagation tab
    PREVENT_PROPOGATION_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']")
    DRAG_ME_PREVENT_TAB_ELEMENT = (By.CSS_SELECTOR, "div[id='dragBox']")
    NOT_GREEDY_DROP_BOX = (By.CSS_SELECTOR, "div[id='notGreedyDropBox']")
    NOT_GREEDY_INNER_DROP_BOX = (By.CSS_SELECTOR, "div[id='notGreedyInnerDropBox']")
    GREEDY_DROP_BOX = (By.CSS_SELECTOR, "div[id='greedyDropBox']")
    GREEDY_INNER_DROP_BOX = (By.CSS_SELECTOR, "div[id='greedyDropBoxInner']")

    # Revert Draggable tab
    REVERENT_DRAGGABLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-revertable']")
    WILL_REVERENT = (By.CSS_SELECTOR, "div[id='revertable']")
    NOT_REVERENT = (By.CSS_SELECTOR, "div[id='notRevertable']")
    DROP_REVERENT_BOX = (By.CSS_SELECTOR, "div[id='droppableExample-tabpane-revertable'] div[id='droppable']")
