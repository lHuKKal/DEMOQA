from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    """Локаторы со страницы https://demoqa.com/text-box"""

    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")  # input[id='userName'] поиск происходит по тегу и далее по ID
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")  # #output #name поиск идет по ID в DOM
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
