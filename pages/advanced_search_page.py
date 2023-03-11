from pages.base_page import BasePage


class AdvancedSearchPage(BasePage):

    _SORT_RESULT_BY_OPTION_DROPDOWN = '//select[@name="sort"]'
    _SORT_OPTION = '//select[@name="sort"]/option[text()="{option}"]'
    _SEARCH_BTN = '//input[@name="Adv-Srch-Books-Submit"]'

    def click_search_result_by_option_dropdown(self) -> None:
        self.find_element(self._SORT_RESULT_BY_OPTION_DROPDOWN).click()

    def select_sort_by_option(self, option: str) -> None:
        self.find_element(self._SORT_OPTION, option=option).click()

    def click_search_button(self) -> None:
        self.find_element(self._SEARCH_BTN).click()
