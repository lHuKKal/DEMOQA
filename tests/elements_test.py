import random
import time
import pytest
from pages.base_page import BasePage
from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage


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
        """Тестирование чек боксов в интерфейсе "Checkbox" (https://demoqa.com/checkbox)"""

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
        """Тестирование интерфейса Web Tables (https://demoqa.com/webtables) """

        def test_add_new_record_web_table(self, driver):
            """Создание новой записи в интерфейсе Web Tables"""

            web_tables = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables.open()
            new_record = web_tables.create_new_record_web_table()
            table_result = web_tables.check_created_record_in_the_web_tables()

            # Так как, в функции создание create_new_record имеется цикл создание несколько записей и созданные
            # записи добавляются в список (запись в списке - []), и в переменной table_result содержится тоже список,
            # то для корректной сверки, необходимо создать цикл for, где каждая созданная запись (new_record) будет
            # проверяться на точные совпадение значений с table_result
            for record in new_record:
                assert record in table_result, f"Созданная запись {record} не найдена в таблице"

        def test_search_created_record(self, driver):
            """Тест проверки поиска в интерфейсе Web Tables"""

            web_tables = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables.open()
            #  Берем случайное значение переменной для поиска (является второй индекс, т.к. это список списков) для key_word
            key_word = web_tables.create_new_record_web_table()[0][random.randint(0, 5)]
            web_tables.search_record_in_web_table(key_word)
            table_result = web_tables.check_searched_record()

            assert key_word in table_result, f"Created record with '{key_word}' word was not found"

        def test_edit_record(self, driver):
            """Тестирование редактирование записи"""

            web_tables = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables.open()
            # Создаем нового пользователя для теста и ищем его
            random_data_from_record = web_tables.create_new_record_web_table()[0][random.randint(0, 5)]
            web_tables.search_record_in_web_table(random_data_from_record)
            # Редактируем созданного пользователя, но берем случайную данную из созданного пользователя и
            # сохраняем его в переменную edit_data
            edit_data = web_tables.edit_created_record()[random.randint(0, 5)]
            edit_word = edit_data
            # Вновь ищем отредактированного пользователя для проверки assert
            web_tables.search_record_in_web_table(edit_word)
            table_result = web_tables.check_searched_record()

            assert edit_data in table_result, f"Edited record has been not updated with word '{edit_word}'"

            # Данный assert можно применить, если мы сравниваем одно значение со СПИСКОМ
            # В данном примере assert, в переменной edit_data хранится одно значение, а в table_result
            # хранится список. Тогда данный assert будет сравнить каждый раз edit_data, со списком table_result
            # с помощью цикла for. Если значение будет хотя бы в одном элементе, assert пройдет без ошибок
            # assert any(edit_data in item for item in table_result), f"Проверка не пройдена {edit_data} не найдено"

        def test_delete_record(self, driver):
            """Тестирование удаление созданной записи в интерфейсе Web Tables"""

            web_tables = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables.open()
            new_record = web_tables.create_new_record_web_table()[0][random.randint(0, 5)]
            web_tables.search_record_in_web_table(new_record)
            web_tables.delete_record_new_table()
            text = web_tables.check_delete_record()

            assert text == "No rows found", "Record is not deleted"

            # Данный assert можно применить, если сравнить, что после удаление созданная запись не отображается в списке
            # с помощью функции all
            # table_result = web_tables.check_created_record_in_the_web_tables()
            # assert all(new_record not in item for item in table_result), f"Record with '{new_record}' value is still present"

        def test_web_table_change_count_rows(self, driver):
            """Тестирование смену строк в интерфейсе Web Tables"""

            web_tables = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables.open()
            count = web_tables.own_change_count_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], "The number of rows has not been changed or changed incorrectly"

    class TestButtonInterface:

        def test_double_click(self, driver):
            button_interface = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_interface.open()
            button_interface.double_click_button()
            button_interface.right_click_button()
            button_interface.left_click_button()
            double_click, right_click, dynamic_click = button_interface.check_clicks_button()
            assert "You have done a double click" == double_click, "Double click is not performed"
            assert "You have done a right click" == right_click, "Right click is not performed"
            assert "You have done a dynamic click" == dynamic_click, "Dynamic click is not performed"

            time.sleep(2)


