from pages.base_page import BasePage


class HomePage(BasePage):

    _SIGN_IN_BTN = '//*[@id="nav-link-accountList"]'
    _NAVIGATE_ACCOUNT_LIST = '//span[@id="nav-link-accountList-nav-line-1"]'
    _ALL_DROPDOWN = 'searchDropdownBox'
    _DEPARTMENT_VALUE = '//*[@id="searchDropdownBox"]/option[contains(@value, "books")]'
    _SEARCH_TXT = 'twotabsearchtextbox'
    _SEARCH_ICON = 'nav-search-submit-button'
    _ADVANCED_SEARCH_TAB = '//span[normalize-space()="Advanced Search"]'

    def tap_sign_in_button(self) -> None:
        self.find_element(self._SIGN_IN_BTN).click()

    def get_text_of_navigate_account_list(self) -> str:
        return self.find_element(self._NAVIGATE_ACCOUNT_LIST, 10).text

    def click_all_search_dropdown(self) -> None:
        self.find_element(self._ALL_DROPDOWN).click()

    def select_value_for_all_dropdown(self, department_value: str):
        self.find_element(self._DEPARTMENT_VALUE, department_value=department_value).click()

    def input_value_into_search_field(self, value: str) -> None:
        self.find_element(self._SEARCH_TXT).clear()
        self.find_element(self._SEARCH_TXT).send_keys(value)

    def click_search_icon(self) -> None:
        self.find_element(self._SEARCH_ICON).click()

    def click_advanced_search_tab(self) -> None:
        self.find_element(self._ADVANCED_SEARCH_TAB).click()
