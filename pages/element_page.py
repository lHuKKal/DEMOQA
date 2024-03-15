import time
from faker import Faker

from data.data import Person
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage

fake = Faker("ru_RU")


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        """Ввод данных"""
        person_info = next(generated_person())  # Провести только одну итерацию для ввода фейковых данных. Используется функция next

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
        """Проверка данных"""
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]  # вытаскиваем текста из DOM для дальнейшей проверки c помощью text
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]  # split разделяем текст и вытаскиваем именно первый индекс для сохранения только введенного текста для дальнейшей проверки
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
