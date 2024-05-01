from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_not_clickable(self, locator, timeout=5):
        """
        True - element is not clickable,
        False - element is clickable
        """
        try:
            wait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()
            return False
        except ElementClickInterceptedException:
            return True

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)  # Извлекаем элемент из кортежа
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_child_element(self, locator):
        element = self.driver.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def select_value_by_text(self, locator, value):
        select = Select(self.element_is_present(locator))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, locators, value):
        item_list = self.elements_are_present(locators)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def action_double_click(self, locator):
        action = ActionChains(self.driver)
        action.double_click(locator).perform()

    def action_right_click(self, locator):
        action = ActionChains(self.driver)
        action.context_click(locator).perform()

    def action_move_to_element(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator)
        action.perform()

    def image_get_width_and_height(self, image_locator):
        image = self.element_is_visible(image_locator)
        width = image.size["width"]
        height = image.size["height"]
        return width, height

    def switch_to_tab(self, index_of_tab):
        self.driver.switch_to.window(self.driver.window_handles[index_of_tab])

    def switch_to_alert(self):
        alert = self.driver.switch_to.alert
        return alert

    def switch_to_frame_by_locator(self, locator):
        self.driver.switch_to.frame(locator)

    def action_drag_and_drop_by_offset(self, locator, x_cords, y_cords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(locator, x_cords, y_cords)
        action.perform()

    def action_drag_and_drop_to_element(self, element_move_from, element_move_to):
        action = ActionChains(self.driver)
        action.drag_and_drop(element_move_from, element_move_to)
        action.perform()





