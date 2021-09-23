from behave import then
from resourses import constants
from tests.pages.XenPlatform.UI.callback_api_result_page import CallbackResultPage
import json

CallbackResultPage = CallbackResultPage()


@then(r'I verify Callback Request is {is_sent_callback}')
def is_sent_callback(context, is_sent_callback):
    json_result = CallbackResultPage.get_callback_json(wait_for_callback=True)
    expected_bid = constants.TEST_RESULT["created_account_bid"]
    if is_sent_callback == "True":
        assert expected_bid in json_result
    elif is_sent_callback == "False":
        assert expected_bid not in json_result


@then("I verify Callback Response Status is {callback_status}")
def verify_callback_status(context, callback_status):
    if callback_status != "N/A":
        json_result = CallbackResultPage.get_callback_json()
        json_result = json.dumps(json_result)
        for i in json_result['data']:
            if i['business_id'] == constants.TEST_RESULT["created_account_bid"]:
                assert i['status'] == callback_status
                break
