import requests
import logging
import json
import allure
from resourses import constants


def api_request(method, uri, payload):
    global headers
    # Get request params
    method = method.upper()
    api_host = constants.API_HOST_PROD
    url = api_host + uri

    # Prepare Header
    api_headers = {}
    api_headers["Content-Type"] = "application/json"
    api_headers["Authorization"] = constants.AUTHORIZATION_PROD
    # payload = json.dumps(payload)
    # payload = json.loads(payload)
    try:
        if method == "GET":
            response = requests.request(method=method, url=url, headers=api_headers)
        elif method == "POST":
            response = response = requests.request(method=method, url=url, headers=api_headers, data=json.dumps(payload))
    except:
        msg = "Failed to send " + method + " " + url
        logging.exception(msg)

    # Get Response Json
    try:
        resp = response.json()
    # In case response is not json
    except:
        resp = response.text

    # Attach message to Body of Allure Report
    allure.attach(str(method.upper()), "Method")
    allure.attach(url, "URL")
    allure.attach(str(api_headers), "Request Headers")
    allure.attach(str(payload), "Request Payload")
    allure.attach(str(response.status_code), "HTTP Code")
    allure.attach(str(response.headers), "Response Headers")
    allure.attach(str(response.text), "Response Payload")
    return resp
