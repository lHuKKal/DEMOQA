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
