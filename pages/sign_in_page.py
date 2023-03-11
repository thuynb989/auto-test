from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignInPage(BasePage):

    _EMAIL_TXT = '//input[@id="ap_email"]'
    _CONTINUE_BTN = '//input[@id="continue"]'
    _ALERT_TITLE = '//h4[@class="a-alert-heading"]'
    _ALERT_CONTENT = '//*[@id="auth-error-message-box"]//span[@class="a-list-item"]'
    _PASSWORD_TXT = '//input[@id="ap_password"]'
    _SIGN_IN_BTN = '//input[@id="signInSubmit"]'

    def input_email(self, email_value: str) -> None:
        self.find_element(self._EMAIL_TXT, 10).clear()
        self.driver.find_element(By.XPATH, self._EMAIL_TXT).send_keys(email_value)

    def tap_continue_button(self) -> None:
        self.find_element(self._CONTINUE_BTN, 10).click()

    def get_text_of_alert_title(self) -> str:
        return self.find_element(self._ALERT_TITLE).text

    def get_text_of_alert_content(self) -> str:
        return self.find_element(self._ALERT_CONTENT, 10).text

    def tap_sign_in_button(self) -> None:
        self.find_element(self._SIGN_IN_BTN).click()

    def input_password(self, password: str) -> None:
        self.find_element(self._PASSWORD_TXT).clear()
        self.find_element(self._PASSWORD_TXT).send_keys(password)

