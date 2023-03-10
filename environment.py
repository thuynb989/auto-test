from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.base_page import BasePage


def before_all(context):
    BasePage.driver = context.driver = webdriver.Chrome(ChromeDriverManager().install())


def after_all(context):
    BasePage.driver.quit()
