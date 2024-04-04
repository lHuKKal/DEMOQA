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

    # Radio buttons locators
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class='custom-control-label'][for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class='custom-control-label'][for='impressiveRadio']")
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class='custom-control-label disabled'][for='noRadio']")
    OUTPUT_RESULT_RADIO_BUTTON = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablesLocators:
    """Локаторы со страницы https://demoqa.com/webtables"""

    # "Add" button for opens data form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")

    # "Registration Form" data form
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE = (By.CSS_SELECTOR, "input[id='age']")
    SALARY = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTAMENT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    # "Edit Form" data form locators
    FIRST_NAME_EDIT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_EDIT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_EDIT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_EDIT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_EDIT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTAMENT_EDIT = (By.CSS_SELECTOR, "input[id='department']")

    # table list
    FULL_RECORD_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    NO_ROWS = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST_BUTTON = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
    FIVE_COUNT_ROW = (By.CSS_SELECTOR, f"option[value='5']")
    TEN_COUNT_ROW = (By.CSS_SELECTOR, f"option[value='10']")
    TWENTY_COUNT_ROW = (By.CSS_SELECTOR, f"option[value='20']")
    TWENTY_FIVE_COUNT_ROW = (By.CSS_SELECTOR, f"option[value='25']")
    FIFTY_COUNT_ROW = (By.CSS_SELECTOR, f"option[value='50']")
    ONE_HUNDRED_COUNT_ROW = (By.CSS_SELECTOR, f"option[value='100']")

    # Search field
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    # ROW_PARENT = ".//ancestor::div[contains(@class, 'rt-tr-group')]"


class ButtonsPageLocators:
    """Локаторы со страницы https://demoqa.com/buttons"""

    # Buttons
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    DYNAMIC_CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")

    # Outputs
    DOUBLE_CLICK_OUTPUT = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_OUTPUT = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    DYNAMIC_CLICK_OUTPUT = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")


class LinksPageLocators:
    """Локаторы со страницы https://demoqa.com/links"""

    # Link buttons
    SAMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")


class ImageLocators:
    """Локаторы со страницы https://demoqa.com/broken"""

    # Images
    VALID_IMAGE = (By.XPATH, "//*[text()='Valid image']/following-sibling::img[1]")
    BROKEN_IMAGE = (By.XPATH, "//*[text()='Broken image']/following-sibling::img[1]")


class UploadDownloadPageLocators:
    # Buttons for file
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "a[id='downloadButton']")

    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOADED_FILE_NAME = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")
