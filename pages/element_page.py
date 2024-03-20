import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonsLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    """Логика тестов для страницы https://demoqa.com/text-box"""

    def fill_all_fields(self):
        """Ввод данных"""
        person_info = next(generated_person())
        # Провести только одну итерацию для ввода фейковых данных. Используется функция next

        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.scroll_to_element(self.locators.SUBMIT)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        """Вытаскиваем данные для дальнейшей проверки"""

        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[
            1]  # вытаскиваем текста из DOM для дальнейшей проверки c помощью text
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[
            1]  # split разделяем текст и вытаскиваем именно первый индекс для сохранения только введенного текста для дальнейшей проверки
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators

    """Логика тестов для страницы https://demoqa.com/checkbox"""

    def open_full_list_checkbox(self):
        """Просто открытие всего списка папок для выбора с помощью чек боксов"""
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        """Логика работы для выбора случайного чек бокса"""
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21  # общее количество кликов будет = 21
        while count != 0:  # цикл для случайного клика
            item = item_list[random.randint(1, 15)]  # рандомные чекбокс от 1 до 16
            if count > 0:
                self.scroll_to_element(self.locators.ITEM_LIST)
                item.click()
                count -= 1

            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()
        # делаем замену заголовков, чтобы был корректный assert

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()  # делаем замену заголовков, чтобы был корректный assert


class RadioButtonPage(BasePage):
    locators = RadioButtonsLocators

    """Логика тестов радио кнопок"""

    def click_radio_button(self, choice):  # добавляем переменную choice для дальнейшего выбора из словаря
        choices = {  # Создаем словарь с путями для всех радио кнопок
            'yes': self.locators.YES_RADIO_BUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIO_BUTTON,
            'no': self.locators.NO_RADIO_BUTTON
        }
        self.element_is_visible(choices[choice]).click()  #

    def get_result_radio_button(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT_RADIO_BUTTON).text
