# coding: utf-8

"""
    Katanemo - identity, and fine-grained authorization for modern { API-first } software companies.

    With Katanemo developers can add support for users, enterprise SSO, machine keys and fine-grained authorization in minutes.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@katanemo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import katanemo_sdk
from katanemo_sdk.api.health_api import HealthApi  # noqa: E501
from katanemo_sdk.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = katanemo_sdk.api.health_api.HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_healthz(self):
        """Test case for get_healthz

        Return Katanemo Health  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
