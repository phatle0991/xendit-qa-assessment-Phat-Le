from behave import given, when, then, register_type
import parse
from tests.pages.XenPlatform.UI.settings_page import SettingsPage

SettingsPage = SettingsPage()


@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


register_type(NullableString=parse_nullable_string)


@given('I enable XenPlatform')
def enable_xen_platform(context):
    pass


@given(r'I set Callback URL - Account created = {callback_url:NullableString}')
def set_account_created_callback_url(context, callback_url):
    SettingsPage.open_settings_callback_page()
    SettingsPage.enter_callback_url_account_created(callback_url=callback_url)
    SettingsPage.click_save_callback_account_created()


@given(r'I set Auto-retry for failed callback is {is_enable}')
def switch_to_default_iframe(context, is_enable):
    SettingsPage.open_settings_callback_page()
    if is_enable == "Enabled":
        SettingsPage.set_auto_retry(enabled=True)
    elif is_enable == "Disabled":
        SettingsPage.set_auto_retry(enabled=False)
