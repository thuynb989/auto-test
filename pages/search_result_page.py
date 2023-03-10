from typing import List

from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class SearchResultPage(BasePage):

    _LANGUAGE_CHECKBOX = '//span[text()="{language}"]/preceding-sibling::div//input'
    _ITEMS_PER_PAGE = '//img[@class="s-image"]'
    _RESULT_SEARCH_LABEL = '//span[contains(text(),"of over")]'
    _PAGINATION_SECTION = '//*[@id="search"]//span[@class="s-pagination-strip"]'
    _NEXT_BTN = '//a[text()="Next"]'
    _NUMBER_OF_PAGE = '//a[text()="Next"]/preceding-sibling::span[1]'
    _PUBLICATION_DATE_LIST = '//span[@class="a-size-base a-color-secondary a-text-normal"]'

    def check_a_language_check_box(self, language: str) -> None:
        self.find_element(self._LANGUAGE_CHECKBOX, language=language).click()

    def scroll_to_language_check_box(self, language: str) -> None:
        self.scroll_to_element(self._LANGUAGE_CHECKBOX, language=language)

    def count_result_item_in_per_page(self) -> int:
        return len(self.find_elements(self._ITEMS_PER_PAGE))

    def get_number_result_in_result_search_label(self) -> int:
        result_search_label = self.find_element(self._RESULT_SEARCH_LABEL).text
        number_result = result_search_label.split(" ")[-2].replace(",", "")
        return int(number_result)

    def is_pagination_section_displayed(self) -> bool:
        return self.is_element_displayed(self._PAGINATION_SECTION)

    def is_next_button_enabled(self) -> bool:
        return self.is_element_enabled(self._NEXT_BTN)

    def click_next_button_in_pagination_section(self) -> None:
        self.find_element(self._NEXT_BTN).click()

    def get_number_of_page(self) -> int:
        return int(self.find_element(self._NUMBER_OF_PAGE).text)

    def get_list_publication_date_in_result_list(self) -> List[WebElement]:
        return self.find_elements(self._PUBLICATION_DATE_LIST)
