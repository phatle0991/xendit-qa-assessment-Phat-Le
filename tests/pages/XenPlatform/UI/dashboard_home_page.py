from core.selenium_util.element_util import ElementUtil
from tests.pages.base_page import BasePage
from resourses import constants

class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        self.is_at_home_page = ElementUtil("xpath=//a[@id='lhs-settings']")
        self.lbl_welcome = ElementUtil("css=h2.font-weight-600")

    def verify_at_home_page(self):
        return self.is_at_home_page.is_displayed(constants.LONG_SLEEP)
