import random
import time
import pytest
from pages.base_page import BasePage
from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_per_adr = text_box_page.check_filled_form()

            assert full_name == output_name, "the full name don't match"
            assert email == output_email, "the email don't match"
            assert current_address == output_current_address, "the current address don't match"
            assert permanent_address == output_per_adr, "the permanent address don't match"

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list_checkbox()
            check_box_page.click_random_checkbox()
            input_check_box = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print("Selected check boxes " + str(input_check_box))
            print("Output " + str(output_result))
            assert input_check_box == output_result, "checkboxes has not been selected"

    class TestRadioButtons:

        def test_radio_button_click(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()

            radio_button_page.click_radio_button("yes")
            output_radio_button_yes = radio_button_page.get_result_radio_button()
            print(output_radio_button_yes)
            assert 'Yes' == output_radio_button_yes, "YES radio button is not selected"

            radio_button_page.click_radio_button("impressive")
            output_radio_button_impressive = radio_button_page.get_result_radio_button()
            assert 'Impressive' == output_radio_button_impressive, "IMPRESSIVE radio button is not selected"

            input_radio_button_no = radio_button_page.click_radio_button("no")
            output_radio_button_no = radio_button_page.get_result_radio_button()
            assert "No" != output_radio_button_no, "There is bug"

    class TestWebTable:

        def test_add_new_record_web_table(self, driver):
            """Создание новой записи в интерфейсе Web Tables"""

            web_tables = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables.open()
            new_record = web_tables.create_new_record_web_table()
            table_result = web_tables.check_created_record_in_the_web_tables()

            # Для корректной проверки необходимо создать цикл (ТОЛЬКО для списков).
            # В данном примере new_record имеет список и будет проверяться список
            for record in new_record:
                assert record in table_result, f"Созданная запись {record} не найдена в таблице"

        def test_search_created_record(self, driver):
            """Тест проверки поиска в интерфейсе Web Tables"""

            web_tables = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables.open()
            #  Берем случайное значение переменной для поиска (является второй индекс) для key_word
            key_word = web_tables.create_new_record_web_table()[0][random.randint(0, 5)]
            web_tables.search_record_in_web_table(key_word)
            table_result = web_tables.check_searched_record()

            assert key_word in table_result, f"Created record with '{key_word}' word was not found"

        def test_edit_record(self, driver):
            """Тестирование редактирование записи"""
            web_tables = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables.open()
            key_word = web_tables.create_new_record_web_table()[0][random.randint(0, 5)]
            web_tables.search_record_in_web_table(key_word)
            web_tables.edit_created_record()
            table_result = web_tables.check_searched_record()

            assert key_word in table_result, f"Edited record with '{key_word}' word was not found"

