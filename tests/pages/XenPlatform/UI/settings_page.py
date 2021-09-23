from core.selenium_util.element_util import ElementUtil
from tests.pages.base_page import BasePage
from resourses import constants


class SettingsPage(BasePage):
    def __init__(self):
        super().__init__()
        self.txt_callback_account_created = ElementUtil(
            "xpath=//*[@id='callbacks']//tr[6]//div[@class='flex-column '][1]//input")
        self.btn_callback_account_created_save = ElementUtil(
            "xpath=//*[@id='callbacks']//tr[6]//div[@class='flex-column '][1]//button")
        self.btn_enable_auto_retry_is_on = ElementUtil("css=.switch-toggle on")
        self.btn_enable_auto_retry = ElementUtil("css=.switch-toggle-handle")

    def open_settings_callback_page(self):
        self.open_url(constants.URL["xenplatform"]["settings_callbacks"])

    def enter_callback_url_account_created(self, callback_url):
        self.txt_callback_account_created.send_keys(callback_url)
        self.txt_callback_account_created.delay(constants.LONG_SLEEP+2)

    def enabled_auto_retry_is_on(self):
        if self.btn_enable_auto_retry_is_on.is_displayed():
            return True
        return False

    def set_auto_retry(self, enabled="True"):
        if enabled == "True":
            if self.enabled_auto_retry_is_on():
                return
        else:
            if self.enabled_auto_retry_is_on() == False:
                return
        self.btn_enable_auto_retry.click()

    def click_save_callback_account_created(self):
        self.btn_callback_account_created_save.wait_for_clickable()
        self.btn_callback_account_created_save.click()
