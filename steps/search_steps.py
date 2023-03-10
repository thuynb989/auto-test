
from behave import given, step, then
from behave.runner import Context
from hamcrest import assert_that, equal_to
from pages.home_page import HomePage
from pages.search_result_page import SearchResultPage
from pages.advanced_search_page import AdvancedSearchPage

home_page = HomePage()
search_result_page = SearchResultPage()
advanced_search_page = AdvancedSearchPage()


@given('Home Page - User click "All" dropdown')
def home_page_click_all_search_dropdown(context: Context) -> None:
    home_page.click_all_search_dropdown()


@step('Home Page - User select department is "{department}"')
def home_page_click_all_search_dropdown(context: Context, department: str) -> None:
    home_page.select_value_for_all_dropdown(department)


@step('Home Page - User input value "{value}" into "Search" field')
def home_page_input_value_into_search_field(context: Context, value: str) -> None:
    home_page.input_value_into_search_field(value)


@step('Home Page - User click "Search" icon')
def home_page_click_search_icon(context: Context) -> None:
    home_page.click_search_icon()


@step('Search Result Page - Scroll to "{language}" check box')
def search_result_page_scroll_to_language_check_box(context: Context, language: str) -> None:
    search_result_page.scroll_to_language_check_box(language=language)


@step('Search Result Page - User check "{language}" check box')
def search_result_page_check_a_check_box(context: Context, language: str) -> None:
    search_result_page.check_a_language_check_box(language=language)


@then('Search Result Page - Verify search result is paginated')
def search_result_page_verify_search_result_is_paginated(context: Context) -> None:
    number_result = search_result_page.get_number_result_in_result_search_label()
    if number_result >= 16:
        assert_that(search_result_page.is_pagination_section_displayed(), equal_to(True))


@then('Search Result Page - The number of items is "{number}" in each page')
def search_result_page_verify_the_number_of_items_is_in_each_page(context: Context, number: int) -> None:
    number_page = search_result_page.get_number_of_page()
    for current_page in range(number_page-1):
        number_item = search_result_page.count_result_item_in_per_page()
        assert_that(number_item, equal_to(number))
        search_result_page.click_next_button_in_pagination_section()


@step('Advanced Search Page - User click "Search" button')
def advanced_search_page_click_search_button(context: Context) -> None:
    advanced_search_page.click_search_button()


@step('Home Page - User click "Advanced Search" tab')
def home_page_click_advanced_search_tab(context: Context) -> None:
    home_page.click_advanced_search_tab()


@step('Advanced Search Page - User click "Sort results by" dropdown')
def advanced_search_page_click_sort_result_by_dropdown(context: Context) -> None:
    advanced_search_page.click_search_result_by_option_dropdown()


@step('Advanced Search Page - User click "{option}" dropdown')
def advanced_search_page_click_sort_result_by_dropdown(context: Context, option: str) -> None:
    advanced_search_page.select_sort_by_option(option)


@then('Search Result Page - Verify the result is sorted by Publication date')
def verify_the_result_is_sorted_by_publication_date(context: Context) -> None:
    dates = []
    for element in search_result_page.get_list_publication_date_in_result_list():
        dates.append(element.text)
    sorted_dates = sorted(dates, reverse=True)
    assert_that(dates, equal_to(sorted_dates))
