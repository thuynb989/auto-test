from loguru import logger
from behave import given, step, then
from behave.runner import Context
from hamcrest import assert_that, equal_to
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage

home_page = HomePage()
sign_in_page = SignInPage()


@step('Home Page - User click "Sign in" button')
def home_page_click_sign_in_button(context: Context) -> None:
    home_page.tap_sign_in_button()


@step('Sign In Page - User input "{email}" into email field')
def sign_in_page_input_email_field(context: Context, email: str) -> None:
    sign_in_page.input_email(email)


@step('Sign In Page - User tap "Continue" button')
def aign_in_page_tap_continue_button(context: Context) -> None:
    sign_in_page.tap_continue_button()


@then('Sign In Page - verify alert title is "{title}"')
def verify_alert_title_is(context: Context, title: str) -> None:
    assert_that(sign_in_page.get_text_of_alert_title(), equal_to(title))


@then('Sign In Page - verify alert content is "{content}"')
def verify_alert_title_is(context: Context, content: str) -> None:
    assert_that(sign_in_page.get_text_of_alert_content(), equal_to(content))


@step('Sign In Page - User input "{password}" into "Password" field')
def sign_in_page_input_password_field(context: Context, password: str) -> None:
    sign_in_page.input_password(password)


@step('Sign In Page - User click "Sign in" button')
def sign_in_page_click_sign_in_button(context: Context) -> None:
    sign_in_page.tap_sign_in_button()


@then('Home Page - verify navigate account list is displayed with text "{text}"')
def home_page_verify_navigate_account_list_is_displayed_with_text(context: Context, text) -> None:
    assert_that(home_page.get_text_of_navigate_account_list(), equal_to(text))


@step('Home Page - User sign in with valid account')
def home_page_user_sign_in_with_valid_account(context: Context) -> None:
    email, password = context.table[0].cells
    logger.info(f'email: {email}')
    home_page.tap_sign_in_button()
    sign_in_page.input_email(email)
    sign_in_page.tap_continue_button()
    sign_in_page.input_password(password)
    sign_in_page.tap_sign_in_button()


@given('Navigate to the Amazon site')
def navigate_to_amazon_site(context: Context) -> None:
    sign_in_page.navigate_to_the_site()
