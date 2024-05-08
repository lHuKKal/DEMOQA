import random
import time

import allure
from selenium.common import TimeoutException

from locators.alert_frame_windows_page_locators import BrowserWindowsLocators, AlertsLocators, FramesPageLocators, \
    NestedFramesLocators, ModalDialogsLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsLocators

    @allure.step("Opening the new tab")
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

    @allure.step("Opened new window")
    def new_window_opened(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        # Переключить фокус драйвера на новую вкладку
        self.switch_to_tab(1)
        time.sleep(1)
        text_title = self.element_is_present(self.locators.NEW_TAB_TITLE).text
        self.driver.close()
        self.switch_to_tab(0)

        return text_title


class AlertsPage(BasePage):
    locators = AlertsLocators

    @allure.step("Alert is displayed after click")
    def alert_after_click(self):
        """Логика тестирование алерта после клика на кнопку"""
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        text = alert_window.text
        alert_window.accept()
        return text

    @allure.step("Alert is displayed after 5 sec.")
    def alert_displayed_after_five_seconds(self):
        """Алерт отображается через 5 секунд после клика на кнопку"""
        self.element_is_visible(self.locators.ALERT_AFTER_5_SECONDS_BUTTON).click()
        time.sleep(5.1)
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    @allure.step("Confirm alert")
    def confirm_alert(self):
        """Подтверждающий аллерт"""
        self.element_is_visible(self.locators.ALERT_CONFIRM_BUTTON).click()
        alert = self.switch_to_alert()
        alert.accept()
        text_after_click = self.element_is_present(self.locators.ALERT_CONFIRM_TEXT_AFTER_ACCEPT).text

        return text_after_click

    @allure.step("Enter value in the alert field window")
    def prompt_alert(self):
        """Алерт где необходимо ввести какой-нибудь текст"""

        text = f"Autotest send keys - {random.randint(1, 100)}"

        self.element_is_visible(self.locators.ALERT_PROMPT_BUTTON).click()
        alert = self.switch_to_alert()
        alert.send_keys(text)
        alert.accept()
        result = self.element_is_present(self.locators.ALERT_PROMPT_TEXT_AFTER_ACCEPT).text

        return result, text


class FramesPage(BasePage):
    locators = FramesPageLocators

    @allure.step("Get text width and height from frame")
    def get_text_width_height_from_frame(self, frame_element, element_get_title_text):
        frame = self.element_is_present(frame_element)
        width = frame.get_attribute("width")
        height = frame.get_attribute("height")
        self.switch_to_frame_by_locator(frame)
        title_text = self.element_is_present(element_get_title_text).text
        self.driver.switch_to.default_content()
        return [title_text, width, height]

    @allure.step("Check frames")
    def check_frames(self, frame_number):

        if frame_number == 'frame1':
            frame_one = self.locators.FIRST_FRAME
            frame_one_text = self.locators.FRAME_TITLE

            result_frame_one = self.get_text_width_height_from_frame(frame_one, frame_one_text)

            return result_frame_one

        if frame_number == 'frame2':
            frame_two = self.locators.SECOND_FRAME
            frame_two_text = self.locators.FRAME_TITLE

            result_frame_two = self.get_text_width_height_from_frame(frame_two, frame_two_text)

            return result_frame_two


class NestedFramesPage(BasePage):
    locators = NestedFramesLocators

    @allure.step("Check nested frames")
    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAMES)
        self.switch_to_frame_by_locator(parent_frame)
        parent_title = self.element_is_present(self.locators.PARENT_TITLE).text

        child_frame = self.element_is_present(self.locators.CHILD_IFRAME)
        self.switch_to_frame_by_locator(child_frame)
        child_title = self.element_is_present(self.locators.CHILD_TITLE).text

        return parent_title, child_title


class ModalDialogsPage(BasePage):
    locators = ModalDialogsLocators

    @allure.step("Check the small modal window is displayed")
    def check_small_modal_window_is_opened(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        small_window_title = self.element_is_present(self.locators.SMALL_MODAL_TITLE).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE).click()
        time.sleep(0.2)

        return small_window_title

    @allure.step("Check the large modal window is displayed")
    def check_large_modal_dialog_is_opened(self):
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        large_modal_title = self.element_is_present(self.locators.LARGE_MODAL_BUTTON).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE).click()
        time.sleep(0.2)

        return large_modal_title

    @allure.step("Check the small modal window is closed")
    def check_small_modal_is_closed(self):
        try:
            self.element_is_not_visible(self.locators.SMALL_MODAL_TITLE)
        except TimeoutException:
            return False
        return True

    @allure.step("Check the large modal window is closed")
    def check_large_modal_is_closed(self):
        try:
            self.element_is_not_visible(self.locators.LARGE_MODAL_TITLE)
        except TimeoutException:
            return False
        return True
