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


class CheckBoxPageLocators:
    """Локаторы со страницы https://demoqa.com/checkbox"""

    # Check box locators
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"  # Элементы для взятия заголовков чек боксов
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonsLocators:
    """Локаторы со страницы https://demoqa.com/radio-button"""

    # Radio buttons locator
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class='custom-control-label'][for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class='custom-control-label'][for='impressiveRadio']")
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class='custom-control-label disabled'][for='noRadio']")
    OUTPUT_RESULT_RADIO_BUTTON = (By.CSS_SELECTOR, "span[class='text-success']")

