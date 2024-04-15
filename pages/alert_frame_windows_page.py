import random
import time

from locators.alert_frame_windows_page_locators import BrowserWindowsLocators, AlertsLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsLocators

    def new_tab_opened(self):
        """Открытие новой вкладки с помощью кнопки New Tab"""

        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        # Переключить фокус драйвера на новую вкладку
        self.switch_to_tab(1)
        time.sleep(1)
        text_title = self.element_is_present(self.locators.NEW_TAB_TITLE).text
        # Закрыть текущую вкладку
        self.driver.close()
        # Переключится на основную вкладку
        self.switch_to_tab(0)

        return text_title

    def new_window_opened(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        # Переключить фокус драйвера на новую вкладку
        self.switch_to_tab(1)
        time.sleep(1)
        text_title = self.element_is_present(self.locators.NEW_TAB_TITLE).text
        self.driver.close()

        return text_title


class AlertsPage(BasePage):
    locators = AlertsLocators

    def alert_after_click(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        text = alert_window.text
        alert_window.accept()
        return text

    def alert_displayed_after_five_seconds(self):
        self.element_is_visible(self.locators.ALERT_AFTER_5_SECONDS_BUTTON).click()
        time.sleep(5.1)
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def confirm_alert(self):
        self.element_is_visible(self.locators.ALERT_CONFIRM_BUTTON).click()
        alert = self.switch_to_alert()
        alert.accept()
        text_after_click = self.element_is_present(self.locators.ALERT_CONFIRM_TEXT_AFTER_ACCEPT).text

        return text_after_click

    def prompt_alert(self):
        text = f"Autotest send keys - {random.randint(1, 100)}"

        self.element_is_visible(self.locators.ALERT_PROMPT_BUTTON).click()
        alert = self.switch_to_alert()
        alert.send_keys(text)
        alert.accept()
        result = self.element_is_present(self.locators.ALERT_PROMPT_TEXT_AFTER_ACCEPT).text

        return result, text



