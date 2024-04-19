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
    MULTIPLE_TYPE_RESULT = (By.CSS_SELECTOR, "div[class='auto-complete__value-container auto-complete__value-container--is-multi auto-complete__value-container--has-value css-1hwfws3']")
    SINGE_TYPE_RESULT = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")

    # Clear button
    MULTIPLE_TYPE_CLEAR_BUTTON = (By.CSS_SELECTOR, "div[class='auto-complete__indicators css-1wy0on6']")

