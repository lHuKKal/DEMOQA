from locators.widgets_locators import AccordianLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianLocators

    def accordian_page(self):

        first_section = self.element_is_visible(self.locators.FIRST_SECTION)
        second_section = self.element_is_visible(self.locators.SECOND_SECTION)
        third_section = self.element_is_visible(self.locators.THIRD_SECTION)

        second_section.click()
        second_title = second_section.text
        second_accordian_text = self.element_is_visible(self.locators.SECOND_SECTION_TEXT).text
        third_section.click()
        third_title = third_section.text
        third_accordian_text = self.element_is_visible(self.locators.THIRD_SECTION_TEXT).text
        first_section.click()
        first_title = first_section.text
        first_accordian_text = self.element_is_visible(self.locators.FIRST_SECTION).text

        return first_title, len(first_accordian_text), second_title, len(second_accordian_text), third_title, len(third_accordian_text)
