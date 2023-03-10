from typing import Optional, Any, Tuple, List
from loguru import logger
from selenium.common import TimeoutException

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver: WebDriver

    def __init__(self, driver: WebDriver = None) -> None:
        if driver:
            self.driver = driver

    def get_locator(self, locators: str) -> Tuple[str, str]:
        return self.auto_parse_locator(locators)

    def navigate_to_the_site(self) -> None:
        self.driver.get("https://www.amazon.com/ref=nav_logo")
        self.driver.maximize_window()

    @staticmethod
    def auto_parse_locator(value: str) -> Tuple[str, str]:
        if value.startswith('./') or value.startswith('/') or value.startswith('('):
            return 'xpath', value
        return 'id', value

    def find_element(self, locators: str, time_out: int = 10, **kwargs: Optional[Any]) -> WebElement:
        locators = locators.format(**kwargs)
        by, value = self.get_locator(locators)
        return WebDriverWait(self.driver, time_out).until(ec.presence_of_element_located((by, value)))

    def find_elements(self, locators: str, time_out: int = 10, **kwargs: Optional[Any]) -> List[WebElement]:
        locators = locators.format(**kwargs)
        by, value = self.get_locator(locators)
        return WebDriverWait(self.driver, time_out).until(ec.presence_of_element_located((by, value)))

    def scroll_to_element(self, locators: str, time_out: int = 10, **kwargs: Optional[Any]):
        locators = locators.format(**kwargs)
        by, value = self.get_locator(locators)
        element = WebDriverWait(self, time_out).until(ec.visibility_of_element_located((by, value)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def is_element_displayed(self, locators: str, time_out: int = 10, **kwargs: Optional[Any]) -> bool:
        locators = locators.format(**kwargs)
        by, value = self.get_locator(locators)
        logger.info(f'Check if element with locator {by}:{value} is displayed')
        try:
            element = self.find_element(locators, time_out=time_out, **kwargs)
            logger.info(f'The element is{"" if element.is_displayed() else " not"} displayed')
            return element.is_displayed()
        except TimeoutException:
            logger.warning(f'The element is not displayed within {time_out} seconds')
            return False

    def is_element_enabled(self, locators: str, time_out: int = 10, **kwargs: Optional[Any]) -> bool:
        locators = locators.format(**kwargs)
        by, value = self.get_locator(locators)
        logger.info(f'Check if element with locator {by}:{value} is enabled')
        try:
            element = self.find_element(locators, time_out=time_out, **kwargs)
            logger.info(f'The element is {"enabled" if element.is_enabled() else "disabled"}')
            return element.is_enabled()
        except TimeoutException:
            logger.warning(f'Cant find the element within {time_out} seconds')
            return False





