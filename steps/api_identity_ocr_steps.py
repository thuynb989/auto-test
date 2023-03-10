from behave import given, step, then
from behave.runner import Context
from hamcrest import assert_that, equal_to, contains_string, is_not

from api.identity_ocr import IdentityOcr

identity_ocr = IdentityOcr()


@given('input a image with "{path}"')
def input_a_valid_image(context: Context, path: str) -> None:
    context.image_path = path


@step('calling OCR API with image')
def calling_ocr_api_with_image(context: Context) -> None:
    context.response = identity_ocr.identity_ocr(context.valid_image)


@then('verify the response status is successfully')
def verify_the_response_status_is_successfully(context: Context) -> None:
    assert_that(context.response.status_code, equal_to(200))
    assert_that(context.response.json()['status'], equal_to('success'))


@then('verify the response fields contain ID, Name, Birthday and Address')
def verify_the_response_fields_contain_correctly_fields(context: Context) -> None:
    assert_that(context.response.json(), contains_string('id'))
    assert_that(context.response.json(), contains_string('name'))
    assert_that(context.response.json(), contains_string('birthday'))
    assert_that(context.response.json(), contains_string('address'))


@then('verify the response status is failure')
def verify_the_response_status_is_failure(context: Context) -> None:
    assert_that(context.response.status_code, equal_to(200))
    assert_that(context.response.json()['status'], equal_to('failure'))


@then('verify the response status code is 400')
def verify_the_response_status_is_failure(context: Context) -> None:
    assert_that(context.response.status_code, equal_to(400))


@then('verify the response contain error field')
def verify_the_response_fields_contain_correctly_fields(context: Context) -> None:
    assert_that(context.response.json(), contains_string('error'))
