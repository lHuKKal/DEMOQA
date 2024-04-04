import base64
import os
import random
import time

import requests
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

from generator.generator import generate_person, generate_file, generate_jpeg
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonsLocators, \
    WebTablesLocators, ButtonsPageLocators, LinksPageLocators, ImageLocators, UploadDownloadPageLocators
from pages.base_page import BasePage

faker_ru = Faker("ru_RU")
actions = ActionChains


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    """Логика тестов для страницы https://demoqa.com/text-box"""

    def fill_all_fields(self):
        """Ввод данных"""
        # Провести только одну итерацию для ввода фейковых данных. Используется функция next
        person_info = next(generate_person())

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
        self.element_is_visible(choices[choice]).click()

    def get_result_radio_button(self):
        return self.element_is_visible(self.locators.OUTPUT_RESULT_RADIO_BUTTON).text


class WebTablesPage(BasePage):
    """Тест CRUD интерфейса Web Tables"""
    locators = WebTablesLocators

    def create_new_record_web_table(self, count=1):
        """Создание новой записи"""

        results = []

        # цикл создания несколько записей от пестицида
        while count != 0:
            # Провести только одну итерацию для ввода фейковых данных. Используется функция next
            generation_data = next(generate_person())

            first_name = generation_data.first_name
            last_name = generation_data.last_name
            email = generation_data.email
            age = generation_data.age
            salary = generation_data.salary
            departament = generation_data.departament

            """Создание новой записи в интерфейсе Web Tables"""

            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.AGE).send_keys(age)
            self.element_is_visible(self.locators.SALARY).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTAMENT).send_keys(departament)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

            results.append([first_name, last_name, str(age), email, str(salary), departament])
            count -= 1
        return results

    def check_created_record_in_the_web_tables(self):
        """Берем ВСЕ данные из таблицы для дальнейшей проверки"""

        created_record_list = self.elements_are_present(self.locators.FULL_RECORD_LIST)

        # Берем все записи из таблицы из интерфейса Web Tables для дальнейшего сравнения с созданной записью
        # ОБЯЗАТЕЛЬНО создать такой цикл, чтобы из web element вытащить текста из списков
        data = []
        for item in created_record_list:
            data.append(item.text.splitlines())
        return data

    def search_record_in_web_table(self, key_word):
        """Поиск созданной записи с помощью поля поиска"""

        # Поиск осуществляется с помощью передачи слова в переменную key_word
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_searched_record(self):
        """Забираем данные из таблицы для дальнейшей проверке"""

        # Берем все данные родительской ветки от кнопки Delete в переменной row
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, ".//ancestor::div[contains(@class, 'rt-tr-group')]")

        return row.text.splitlines()

    def edit_created_record(self):
        """Логика редактирование записи"""

        self.element_is_present(self.locators.EDIT_BUTTON).click()
        # Пришлось очистить поле именно таким образом, иначе с помощью функции clear, поле не "очищалось"
        # И при вводе очищенное значение отображалось вновь при вводе любого значение
        self.element_is_visible(self.locators.FIRST_NAME_EDIT).send_keys(Keys.CONTROL + "a")  # Выделение всего текста
        self.element_is_visible(self.locators.FIRST_NAME_EDIT).send_keys(Keys.DELETE)  # Удаление выделенного текста
        self.element_is_visible(self.locators.LAST_NAME_EDIT).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.LAST_NAME).send_keys(Keys.DELETE)
        self.element_is_visible(self.locators.EMAIL_EDIT).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.EMAIL_EDIT).send_keys(Keys.DELETE)
        self.element_is_visible(self.locators.AGE_EDIT).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.AGE_EDIT).send_keys(Keys.DELETE)
        self.element_is_visible(self.locators.SALARY_EDIT).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.SALARY_EDIT).send_keys(Keys.DELETE)
        self.element_is_visible(self.locators.DEPARTAMENT_EDIT).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.DEPARTAMENT_EDIT).send_keys(Keys.DELETE)

        generation_data = next(generate_person())

        first_name = generation_data.first_name
        last_name = generation_data.last_name
        email = generation_data.email
        age = generation_data.age
        salary = generation_data.salary
        departament = generation_data.departament

        """Создание новой записи в интерфейсе Web Tables"""

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SALARY).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTAMENT).send_keys(departament)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(Keys.DELETE)

        return first_name, last_name, str(age), email, str(salary), departament

    def delete_record_new_table(self):
        """Клик на кнопку удалить"""

        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_delete_record(self):
        """Вытаскиваем текст "No rows found", когда запись удалена для дальнейшей проверки"""

        # Текст "No rows found" отображается когда данные не найдены, либо найденная запись была удалена
        # возвращаем данный текст в функцию для дальнейшей проверки для теста удаления
        return self.element_is_present(self.locators.NO_ROWS).text

    def clear_search_field_web_table(self):
        """Очистка поля поиска"""

        # Используется данный методы из-за того, что после функции clear и ввода любого символа, ранее введенные данные
        # вновь отображаются в поле, хотя поле до этого было очищено
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(Keys.DELETE)

    def change_count_some_rows(self):
        """Смена количество строк в таблице"""

        count_row = [5, 10, 25, 50, 100]
        data = []
        count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST_BUTTON)

        for count in count_row:
            self.scroll_to_element((By.CSS_SELECTOR, "select[aria-label='rows per page']"))
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{count}']")).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):

        list_rows = self.elements_are_present(self.locators.FULL_RECORD_LIST)
        return len(list_rows)

    def five_change_rows(self):

        self.scroll_to_element(self.locators.COUNT_ROW_LIST_BUTTON)
        self.element_is_visible(self.locators.COUNT_ROW_LIST_BUTTON).click()
        self.element_is_visible(self.locators.FIVE_COUNT_ROW).click()
        five_row = self.elements_are_present(self.locators.FULL_RECORD_LIST)
        return len(five_row)

    def own_change_count_some_rows(self):
        """Смена количество строк в таблице"""

        count_row = [5, 10, 20, 25, 50, 100]
        data = []
        count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST_BUTTON)

        for count in count_row:
            self.scroll_to_element((By.CSS_SELECTOR, "select[aria-label='rows per page']"))
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{count}']")).click()
            list_rows = self.elements_are_present(self.locators.FULL_RECORD_LIST)
            data.append(len(list_rows))
            time.sleep(0.3)
        return data


class ButtonsPage(BasePage):
    """Тестирование кликов в интерфейсе Buttons (https://demoqa.com/buttons)"""
    locators = ButtonsPageLocators

    def double_click_button(self):
        """Тест двойного клика"""

        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))

    def right_click_button(self):
        """Тест клика провой кнопки мыши"""

        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))

    def left_click_button(self):
        """Тест клика у динамической кнопки"""

        self.element_is_visible(self.locators.DYNAMIC_CLICK_BUTTON).click()

    def check_clicks_button(self):
        """Оутпуты, что кнопки были кликнуты для проверки"""

        double_click = self.element_is_present(self.locators.DOUBLE_CLICK_OUTPUT).text
        right_click = self.element_is_present(self.locators.RIGHT_CLICK_OUTPUT).text
        dynamic_click = self.element_is_present(self.locators.DYNAMIC_CLICK_OUTPUT).text

        return double_click, right_click, dynamic_click


class LinksPage(BasePage):
    locators = LinksPageLocators

    def check_new_tab_simple_link(self):

        simple_link = self.element_is_visible(self.locators.SAMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)

        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self, url):

        request = requests.get(url)

        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code


class BrokenPage(BasePage):
    """Тестирование картинок в интерфейсе Images (https://demoqa.com/broken)"""
    locators = ImageLocators

    def valid_image(self):
        """Тестирование валидной картинки"""
        width, height = self.image_get_width_and_height(self.locators.VALID_IMAGE)
        return width, height

    def broken_image(self):
        """Тестирование поломанной картинки"""
        image = self.element_is_visible(self.locators.BROKEN_IMAGE)
        width = image.size["width"]
        height = image.size["height"]

        return width, height


class UploadDownloadPage(BasePage):
    locators = UploadDownloadPageLocators

    def upload_file(self):
        file_name, path = generate_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        uploaded_file_name = self.element_is_present(self.locators.UPLOADED_FILE_NAME).text
        return file_name.split('\\')[-1], path, uploaded_file_name.split('\\')[-1]

    def download_file(self):

        link = self.element_is_visible(self.locators.DOWNLOAD_BUTTON).get_attribute('href')
        check = generate_jpeg(link)
        return check





