import time

from pages.alert_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertFrameWindows:
    class TestBrowserWindows:
        """Тестирование логики открытие новых вкладок с помощью кнопок"""

        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_new_tab = browser_windows_page.new_tab_opened()
            text_new_window = browser_windows_page.new_window_opened()

            assert text_new_tab == "This is a sample page", "New tab don't opened or opened incorrectly"
            assert text_new_window == "This is a sample page", "New window don't opened or opened incorrectly"

    class TestAlerts:

        def test_alerts(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_after_click = alert_page.alert_after_click()
            alert_after_five_seconds = alert_page.alert_displayed_after_five_seconds()
            alert_after_accept = alert_page.confirm_alert()
            alert_prompt_result, text = alert_page.prompt_alert()

            assert alert_after_click == "You clicked a button", "Alert is not displayed after click"
            assert alert_after_five_seconds == "This alert appeared after 5 seconds", "Alert is not displayed after 5 sec."
            assert alert_after_accept == "You selected Ok", "Alert is not displayed after click"
            assert text in alert_prompt_result, "Entered value is not matched with result"
