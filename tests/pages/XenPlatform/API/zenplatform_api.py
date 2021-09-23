from core.api_util import api_utils
from core import random_data_utils
from resourses import constants


class ZenPlatformAPI:
    def __init__(self):
        self.create_account_v1_uri = "/accounts"
        self.create_account_v2_uri = "/v2/accounts"

    def create_account_v1(self, account_email=random_data_utils.get_unique_email(), type="owned",
                          business_name=random_data_utils.get_unique_business_name()):
        payload = {
            "account_email": account_email,
            "type": type,
            "business_profile": {
                "business_name": business_name
            }
        }
        return api_utils.api_request(method="POST", uri=self.create_account_v1_uri, payload=payload)

    def create_account_v2(self, account_email=random_data_utils.get_unique_email(), type="owned",
                          business_name=random_data_utils.get_unique_business_name()):
        payload = {
            "email": account_email,
            "type": type,
            "public_profile": {
                "business_name": business_name
            }
        }
        return api_utils.api_request(method="POST", uri=self.create_account_v2_uri, payload=payload)
