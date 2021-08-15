from behave import given, when, then, register_type
import parse
from tests.pages.calculator_page import CalculatorPage
from core import ocr_util

CalculatorPage = CalculatorPage()


@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


register_type(NullableString=parse_nullable_string)


@given('I open Calculator Page')
def open_calculator_page_step(context):
    CalculatorPage.open_calculator_page()


@when(r'I switch to iframe=fullframe')
def switch_to_iframe_fullframe(context):
    CalculatorPage.switch_to_fullframe()


@then(r'I switch back to default iframe')
def switch_to_default_iframe(context):
    CalculatorPage.switch_to_default_frame()


@when(r'I enter value into Calculator = "{key_value:NullableString}"')
def send_keys_to_calculator_canvas(context, key_value):
    CalculatorPage.send_keys_on_canvas(key_value=key_value)


@then(r'I should be able to see "{expected_result:NullableString}"')
def take_calculator_canvas_screenshot(context, expected_result):
    screenshot_path = CalculatorPage.take_calculated_result_screenshot()
    actual_result = ocr_util.get_ocr_text(screenshot_path)
    assert actual_result == str(expected_result), "Actual Result = " + actual_result + " != " + "Expected Result = " + expected_result
