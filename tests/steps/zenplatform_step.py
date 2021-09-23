from behave import given, when, then, register_type
import parse
from resourses import constants
from tests.pages.XenPlatform.API.zenplatform_api import ZenPlatformAPI

ZenPlatformAPI = ZenPlatformAPI()


@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


register_type(NullableString=parse_nullable_string)


@when(r'I create {account_type} Account by API {create_account_version}')
def create_account_versions(context, account_type, create_account_version):
    if create_account_version == "v1":
        json_result = ZenPlatformAPI.create_account_v1(type=account_type)
        constants.TEST_RESULT["created_account_bid"] = json_result["user_id"]
    elif create_account_version == "v2":
        json_result = ZenPlatformAPI.create_account_v2(type=account_type)
        constants.TEST_RESULT["created_account_bid"] = json_result["id"]


@when(r'Callback response time is {response_time}')
def create_account_versions(context, response_time):
    pass


@then(r'I verify automatic retry is {is_retry}')
def is_retry(context, is_retry):
    pass
