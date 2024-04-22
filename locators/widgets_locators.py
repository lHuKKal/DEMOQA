from selenium.webdriver.common.by import By


class AccordianLocators:
    # Sections
    FIRST_SECTION = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECOND_SECTION = (By.CSS_SELECTOR, "div[id='section2Heading']")
    THIRD_SECTION = (By.CSS_SELECTOR, "div[id='section3Heading']")

    # Sections text
    FIRST_SECTION_TEXT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECOND_SECTION_TEXT = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    THIRD_SECTION_TEXT = (By.CSS_SELECTOR, "div[id='section3Content'] p")


class AutoCompleteLocators:
    # Input
    MULTIPLE_TYPE_FIELD = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    SINGLE_TYPE_FIELD = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")

    # Result form fields
    MULTIPLE_TYPE_RESULT = (By.CSS_SELECTOR,
                            "div[class='auto-complete__value-container auto-complete__value-container--is-multi auto-complete__value-container--has-value css-1hwfws3']")
    SINGE_TYPE_RESULT = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
    MULTIPLE_TYPE_TAKE_CLEARED_VALUE = (
        By.XPATH, "//div[@class='css-xb97g8 auto-complete__multi-value__remove']/parent::div//div[1]")

    # Clear buttons
    MULTIPLE_TYPE_CLEAR_ALL_VALUE_BUTTON = (By.CSS_SELECTOR, "div[class='auto-complete__indicators css-1wy0on6']")
    MULTIPLE_TYPE_CLEAR_ONE_VALUE_BUTTON = (
        By.CSS_SELECTOR, "div[class='css-xb97g8 auto-complete__multi-value__remove']")


class DatePickerPageLocators:
    # Date select locators
    DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    # Date and Time

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, "span[class='react-datepicker__year-read-view--selected-year']")
    DATE_AND_TIME_TIME = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")
