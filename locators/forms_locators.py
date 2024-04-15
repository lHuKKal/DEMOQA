import random

from selenium.webdriver.common.by import By


class PracticeFormLocators:
    """Локаторы со страницы https://demoqa.com/automation-practice-form"""

    # Data Fields
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    MOBILE = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BRITH = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    STATE = (By.CSS_SELECTOR, "div[id='state']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    CITY = (By.CSS_SELECTOR, "div[id='city']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    # Upload Picture button
    UPLOAD_PICTURE = (By.CSS_SELECTOR, "input[id='uploadPicture']")

    # Subjects dynamic field
    SUBJECT = (By.CSS_SELECTOR, "input[id='subjectsInput']")

    # Radio buttons
    GENDER_MALE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_OTHER_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    RANDOM_RADIO_BUTTON = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']")

    # Hobbies check boxes
    SPORTS_CHECK_BOX = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    READING_CHECK_BOX = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    MUSIC_CHECK_BOX = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    RANDOM_CHECK_BOX = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']")

    # Result locators

    STUDENT_NAME = (By.XPATH, "//*[text()='Student Name']/following-sibling::td")
    STUDENT_EMAIL = (By.XPATH, "//*[text()='Student Email']/following-sibling::td")
    STUDENT_GENDER = (By.XPATH, "//*[text()='Gender']/following-sibling::td")
    STUDENT_MOBILE = (By.XPATH, "//*[text()='Mobile']/following-sibling::td")
    STUDENT_DATE_OF_BRITH = (By.XPATH, "//*[text()='Date of Birth']/following-sibling::td")
    STUDENT_SUBJECTS = (By.XPATH, "//*[text()='Subjects']/following-sibling::td")
    STUDENT_HOBBIES = (By.XPATH, "//*[text()='Hobbies']/following-sibling::td")
    STUDENT_PICTURE = (By.XPATH, "//*[text()='Picture']/following-sibling::td")
    STUDENT_ADDRESS = (By.XPATH, "//*[text()='Address']/following-sibling::td")
    STUDENT_STATE_AND_CITY = (By.XPATH, "//*[text()='State and City']/following-sibling::td")