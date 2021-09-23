from selenium.webdriver.common.keys import Keys

SEL_TIMEOUT = 30
SHORT_SLEEP = 1
MEDIUM_SLEEP = 2
LONG_SLEEP = 3
CHROME_VERSION = "92.0.4515.107"
FIREFOX_VERSION = None
TEST_RESULT = {}
HOST_PROD = "https://dashboard.xendit.co"
DASHBOARD_INTERNAL_API_HOST = "https://dashboard-gateway.xendit.co"
URL = {
    "calculator_page": "https://www.online-calculator.com/full-screen-calculator/",
    "xenplatform": {
        "login_url": HOST_PROD + "/login",
        "settings_callbacks": HOST_PROD + "/settings/developers#callbacks",
        "callback_result": DASHBOARD_INTERNAL_API_HOST + "/api/webhooks?statuses=COMPLETED+PENDING+FAILED+CALLBACK_URL_NOT_SET&environment=DEVELOPMENT"
    }
}
KEYS = {
    "KEYS.NUMPAD0": Keys.NUMPAD0,
    "KEYS.NUMPAD1": Keys.NUMPAD1,
    "KEYS.NUMPAD2": Keys.NUMPAD2,
    "KEYS.NUMPAD3": Keys.NUMPAD3,
    "KEYS.NUMPAD4": Keys.NUMPAD4,
    "KEYS.NUMPAD5": Keys.NUMPAD5,
    "KEYS.NUMPAD6": Keys.NUMPAD6,
    "KEYS.NUMPAD7": Keys.NUMPAD7,
    "KEYS.NUMPAD8": Keys.NUMPAD8,
    "KEYS.NUMPAD9": Keys.NUMPAD9,
    "KEYS.ENTER": Keys.ENTER,
    "KEYS.EQUALS": Keys.EQUALS,
    "KEYS.ADD": Keys.ADD,
    "KEYS.SUBTRACT": Keys.SUBTRACT,
    "KEYS.DIVIDE": Keys.DIVIDE,
    "KEYS.PERCENTAGE": Keys.SHIFT
}
API_HOST_PROD = "https://api.xendit.co"
AUTHORIZATION_PROD = "Basic eG5kX2RldmVsb3BtZW50X3RZcEp2d2RkVlV1N2NOT0lmcm4zSDAxc1Q4RUtCVzQwUHVrYWFDTFA3dHFCSUZCVFFPdGhBaExqamZIQlkzSE86"
DASHBOARD_EMAIL = "clone0991@gmail.com"
DASHBOARD_PASSWORD = "P@ssw0rd123"