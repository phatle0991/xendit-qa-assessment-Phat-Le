from core.selenium_util.element_util import ElementUtil
from tests.pages.base_page import BasePage
from resourses import constants


class CalculatorPage(BasePage):
    def __init__(self):
        super().__init__()
        self.iframe_fullframe = ElementUtil("xpath=//iframe[@id='fullframe']")
        self.canvas_calculator = ElementUtil("xpath=//canvas[@id='canvas']")

    def open_calculator_page(self):
        self.open_url(constants.URL["calculator_page"])

    def switch_to_fullframe(self):
        self.iframe_fullframe.switch_to_iframe()

    def switch_to_default_frame(self):
        self.iframe_fullframe.switch_to_default_iframe()

    def click_on_cavas(self):
        self.canvas_calculator.click()

    def send_keys_on_canvas(self, key_value):
        self.canvas_calculator.send_keys_action(key_value=key_value)

    def take_calculated_result_screenshot(self):
        return self.canvas_calculator.take_screenshot()
