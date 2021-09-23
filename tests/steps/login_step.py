from behave import given
from resourses import constants
from tests.pages.XenPlatform.UI.login_page import LoginPage
from tests.pages.XenPlatform.UI.dashboard_home_page import HomePage

LoginPage = LoginPage()
HomePage = HomePage()

@given(r'I login as a XenPlatform Entity Account')
def login_as_entity_account(context):
    LoginPage.open_login_page()
    if LoginPage.verify_at_login_page():
        LoginPage.enter_email(constants.DASHBOARD_EMAIL)
        LoginPage.enter_password(constants.DASHBOARD_PASSWORD)
        LoginPage.click_login()
        assert HomePage.verify_at_home_page()