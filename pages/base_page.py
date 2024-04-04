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

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)  # Извлекаем элемент из кортежа
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def action_double_click(self, locator):
        action = ActionChains(self.driver)
        action.double_click(locator).perform()

    def action_right_click(self, locator):
        action = ActionChains(self.driver)
        action.context_click(locator).perform()

    def image_get_width_and_height(self, image_locator):
        """
        Взять высоту и длину картинки. Обязательно необходимо создать
        2 переменные с width и height для использования данной функции
        """
        image = self.element_is_visible(image_locator)
        width = image.size["width"]
        height = image.size["height"]
        return width, height





