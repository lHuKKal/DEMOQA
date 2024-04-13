import os
import random
import time

from selenium.webdriver import Keys

from generator.generator import generate_person, generate_jpeg, generate_file, subject_keys, get_states_and_cities
from locators.forms_locators import PracticeFormLocators
from pages.base_page import BasePage


class FillPracticeForm(BasePage):
    locators = PracticeFormLocators

    def fill_the_data_fields_of_practice_form(self):
        """Заполнние обычных полей"""

        generate_data = next(generate_person())

        first_name = generate_data.first_name
        last_name = generate_data.last_name
        email = generate_data.email
        mobile = generate_data.mobile
        current_address = generate_data.current_address

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.MOBILE).send_keys(mobile)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)

        # Соединяем имя и фамилию для проверки после создания студента, т.к. в результате в поле отображается имя
        # и фамилия
        name = first_name + ' ' + last_name

        return first_name, last_name, email, mobile, current_address, name

    def select_subject(self, select_the_count_of_subjects):
        """Выбор случайного предмета с помощью ключей. Общее количество ключей 14"""

        # Общее количество объектов = 14
        subjects = subject_keys()
        count = select_the_count_of_subjects
        values = []

        # Цикл для случайного выбора предмета для теста
        while count != 0:
            random_subject = random.choice(list(subjects.keys()))
            self.element_is_visible(self.locators.SUBJECT).send_keys(random_subject)
            time.sleep(0.3)
            self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.ENTER)
            count -= 1
            # Удаляем выбранный объект из списка ключей для уникальности выбора
            subjects.pop(random_subject)
            values.append(random_subject)

        # Преобразовать список в строки для корректной проверки assert
        result_string = ', '.join(values)
        return result_string

    def select_radio_button_in_the_practice_form_own(self):
        """Выбор случайного радио кнопки с помощью словаря"""
        values_of_radio_button = {
            'Male': self.locators.GENDER_MALE_RADIO_BUTTON,
            'Female': self.locators.GENDER_FEMALE_RADIO_BUTTON,
            'Other': self.locators.GENDER_OTHER_RADIO_BUTTON
        }

        random_value = random.choice(list(values_of_radio_button.keys()))
        self.element_is_visible(values_of_radio_button[random_value]).click()

        return random_value

    def select_random_gender(self):
        """Выбор случайного пола"""

        random_radio_button = self.element_is_visible(self.locators.RANDOM_RADIO_BUTTON)
        random_radio_button.click()
        result = random_radio_button.text

        return result

    def select_date_in_practice_form(self):
        self.element_is_visible(self.locators.DATE_OF_BRITH).click()

        pass

    def upload_picture(self):
        file_name, path = generate_file()
        self.element_is_present(self.locators.UPLOAD_PICTURE).send_keys(path)
        os.remove(path)
        return file_name.split('\\')[-1], path

    def select_random_check_box(self):
        """Случайный выбор чекбокса (Не подходит для тестов)"""
        list_check_boxes = self.elements_are_visible(self.locators.RANDOM_CHECK_BOX)
        count = 3

        while count != 0:
            check_box = list_check_boxes[random.randint(0, 2)]
            check_box.click()
            count -= 1

    def random_solo_check_box(self, count_check_boxes):
        """Выбор случайного чебокса, общее количество 3"""
        check_box_values = {
            'Sports': self.locators.SPORTS_CHECK_BOX,
            'Reading': self.locators.READING_CHECK_BOX,
            'Music': self.locators.MUSIC_CHECK_BOX
        }
        # количество не должно быть больше чем общее количество ключей в словаре
        count = count_check_boxes
        # Проверка, что введенное количество меньше чем общее количество ключей
        if count_check_boxes > len(check_box_values):
            raise ValueError("You selected check box counts more than available options. Should be 3 or less")
        values = []

        while count != 0:
            # Выбираем случайный чек бокс в цикле
            random_check_box = random.choice(list(check_box_values.keys()))
            self.element_is_visible(check_box_values[random_check_box]).click()
            values.append(random_check_box)
            count -= 1
            check_box_values.pop(random_check_box)  # Удаляем выбранный ключ из словаря для уникальности выбора

        # Преобразуем результат в строку с помощью join для дальнейшего сравнения
        string_result = ', '.join(values)
        return string_result

    def select_random_state_city_and_submit_own(self):
        """Выбор случайного штата и случайного города"""

        self.scroll_to_element(self.locators.STATE)

        # Получаем список штатов и городов
        states_and_cities = get_states_and_cities()
        # Выбор случайного штата для дальнейшего ввода его в поле STATE_INPUT и для получения списка городов
        random_state = random.choice(list(states_and_cities.keys()))
        # Получение списка городов из выбранного штата
        city = states_and_cities[random_state]
        # Выбор случайного города из списка городов
        random_city = random.choice(city)

        # Ввод выбранного штата в поле "State"
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(random_state)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.ENTER)

        # Ввод выбранного города в поле "City"
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(random_city)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.ENTER)

        # Сохраняем форму данных
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

        # Соединяем штат и город для проверки после создания студента, т.к. в результате штат и город отображается
        # в одном поле
        state_and_city = random_state + ' ' + random_city

        return state_and_city

    def check_result_data_form(self):
        """Поля после создание студента для проверки"""

        student_name = self.element_is_present(self.locators.STUDENT_NAME).text
        student_email = self.element_is_present(self.locators.STUDENT_EMAIL).text
        student_gender = self.element_is_present(self.locators.STUDENT_GENDER).text
        student_mobile = self.element_is_present(self.locators.STUDENT_MOBILE).text
        student_date_of_brith = self.element_is_present(self.locators.STUDENT_DATE_OF_BRITH).text
        student_subjects = self.element_is_present(self.locators.STUDENT_SUBJECTS).text
        student_hobbies = self.element_is_present(self.locators.STUDENT_HOBBIES).text
        student_picture = self.element_is_present(self.locators.STUDENT_PICTURE).text
        student_address = self.element_is_present(self.locators.STUDENT_ADDRESS).text
        student_state_and_city = self.element_is_present(self.locators.STUDENT_STATE_AND_CITY).text

        return student_name, student_email, student_gender, student_mobile, student_date_of_brith, student_subjects, student_hobbies, student_picture, student_address, student_state_and_city
