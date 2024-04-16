import time

from pages.alert_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


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
            """Тестирование логики алертов"""
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

    class TestFrames:

        def test_frames(self, driver):
            frames_page = FramesPage(driver, "https://demoqa.com/frames")
            frames_page.open()
            result_frame_1 = frames_page.check_frames("frame1")
            result_frame_2 = frames_page.check_frames("frame2")

            assert result_frame_1 == ['This is a sample page', '500px', '350px'], "The frame doesn't exist"
            assert result_frame_2 == ['This is a sample page', '100px', '100px'], "The frame doesn't exist"

    class TestNestedFrames:

        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frames_page.open()
            parent_tite, child_title = nested_frames_page.check_nested_frames()

            assert parent_tite == "Parent frame", "Parent frame doesn't exist"
            assert child_title == "Child Iframe" "Child frame doesn't exist"

    class TestModalDialogs:

        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            small_window_title, large_modal_title = modal_dialogs_page.check_small_and_large_modal_dialogs()

            assert small_window_title == "Small Modal", "Small modal window doesn't open"
            assert large_modal_title == "Large modal", "Small modal window doesn't open"




