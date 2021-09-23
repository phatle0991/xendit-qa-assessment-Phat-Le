from core.selenium_util.element_util import ElementUtil
from tests.pages.base_page import BasePage
from resourses import constants
import json


class CallbackResultPage(BasePage):
    def __init__(self):
        super().__init__()
        self.json_response = ElementUtil("xpath=//pre")

    def get_callback_json(self, wait_for_callback=False):
        #delay waiting for callback response
        if wait_for_callback:
            self.json_response.delay(30)
        self.open_url(constants.URL["xenplatform"]["callback_result"])
        json_str =  self.json_response.text
        return json_str
