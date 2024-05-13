from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.add_argument("user-data-dir=C:\\profile")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs["driver"]
        attach = driver.get_screenshot_as_png()
        allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)


# Функция сортировку последовательных тестов, если будет необходимо, а лучше сделать маркировку тестов с помощью Pytest

# def pytest_collection_modify_items(config, items):
#     # Указываем список последовательных тестов
#     test_order = [
#         'elements_test',
#         'forms_test',
#         'alert_frame_windows_test',
#         'widgets_test',
#         'interactions_test'
#     ]
#
#     # Сортировка тестов в соответствии с порядком
#     items.sort(key=lambda item: test_order.index(item.module.__name__))