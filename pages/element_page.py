import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        BasePage.element_is_visible(self, TextBoxPage.locators.FULL_NAME).send_keys('Full Name SEL')
        BasePage.element_is_visible(self, TextBoxPage.locators.EMAIL).send_keys('Exmaple@mail.com')
        BasePage.element_is_visible(self, TextBoxPage.locators.CURRENT_ADDRESS).send_keys('Current Address SEL')
        BasePage.element_is_visible(self, TextBoxPage.locators.PERMANENT_ADDRESS).send_keys('Permanent Address SEL')
        BasePage.scroll_to_element(self, TextBoxPage.locators.SUBMIT)
        BasePage.element_is_visible(self, TextBoxPage.locators.SUBMIT).click()
        time.sleep(5)
