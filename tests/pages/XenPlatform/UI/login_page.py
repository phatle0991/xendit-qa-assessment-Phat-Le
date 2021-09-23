from core.selenium_util.element_util import ElementUtil
from tests.pages.base_page import BasePage
from resourses import constants


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.txt_email = ElementUtil("xpath=//input[@name='email']")
        self.txt_password = ElementUtil("xpath=//input[@name='password']")
        self.btn_login = ElementUtil("css=.btn-primary")

    def open_login_page(self):
        self.open_url(constants.URL["xenplatform"]["login_url"])

    def enter_email(self, email):
        self.txt_email.send_keys(email)

    def enter_password(self, password):
        self.txt_password.send_keys(password)

    def click_login(self):
        self.btn_login.click()

    def verify_at_login_page(self):
        return self.btn_login.is_displayed(2)