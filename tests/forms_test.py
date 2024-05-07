import time

import allure

from pages.forms_page import FillPracticeForm


@allure.suite("Testing the 'Practice Form' interface")
class TestPracticeSection:
    @allure.feature("Testing fill data forms")
    class TestPracticeForm:
        @allure.title("Testing fill data forms and check result in the 'Practice Form' interface")
        def test_practice_data_form(self, driver):
            practice_form_page = FillPracticeForm(driver, "https://demoqa.com/automation-practice-form")
            practice_form_page.open()
            first_name, last_name, email, mobile, current_address, name = practice_form_page.fill_the_data_fields_of_practice_form()
            random_gender = practice_form_page.select_radio_button_in_the_practice_form_own()
            upload_file, path = practice_form_page.upload_picture()
            hobbies_check_boxes = practice_form_page.random_solo_check_box(3)
            subjects = practice_form_page.select_subject(3)
            state_and_city = practice_form_page.select_random_state_city_and_submit_own()
            [student_name, student_email, student_gender, student_mobile, student_date_of_brith, student_subjects,
             student_hobbies, student_picture, student_address,
             student_state_and_city] = practice_form_page.check_result_data_form()

            assert name == student_name, "Name don't matched or record has been created incorrectly"
            assert email == student_email, "Email don't matched or record has been created incorrectly"
            assert str(mobile) == student_mobile, "Mobile don't matched or record has been created incorrectly"
            assert random_gender == student_gender, "Gender don't matched or record has been created incorrectly"
            assert current_address == student_address, "Current Address don't matched or record has been created incorrectly"
            assert upload_file == student_picture, "Uploaded file don't matched or record has been created incorrectly"
            assert hobbies_check_boxes == student_hobbies, "Hobbies don't matched or record has been created incorrectly"
            assert subjects == student_subjects, "Subjects don't matched or record has been created incorrectly"
            assert state_and_city == student_state_and_city, "State and City don't matched or record has been created incorrectly"
