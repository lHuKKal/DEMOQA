from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    # Buttons
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_WINDOW_MESSAGE_BUTTON = (By.CSS_SELECTOR, "button[id='messageWindowButton']")

    # Text Locators
    NEW_TAB_TITLE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class AlertsLocators:
    # Buttons
    ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    ALERT_AFTER_5_SECONDS_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    ALERT_CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    ALERT_PROMPT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")

    # Text locators
    ALERT_PROMPT_TEXT_AFTER_ACCEPT = (By.CSS_SELECTOR, "span[id='promptResult']")
    ALERT_CONFIRM_TEXT_AFTER_ACCEPT = (By.CSS_SELECTOR, "span[id='confirmResult']")


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")

    # Title
    FRAME_TITLE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
