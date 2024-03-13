import time

from locators.elements_page_locators import TextBoxPageLocators as locators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    #   locators = TextBoxPageLocators()

    def fill_all_fields(self):
        BasePage.element_is_visible(self, locators.FULL_NAME).send_keys('Full Name SEL')
        BasePage.element_is_visible(self, locators.EMAIL).send_keys('Exmaple@mail.com')
        BasePage.element_is_visible(self, locators.CURRENT_ADDRESS).send_keys('Current Address SEL')
        BasePage.element_is_visible(self, locators.PERMANENT_ADDRESS).send_keys('Permanent Address SEL')
        BasePage.scroll_to_element(self, locators.SUBMIT)
        BasePage.element_is_visible(self, locators.SUBMIT).click()
        time.sleep(5)
