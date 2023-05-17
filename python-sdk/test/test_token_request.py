# coding: utf-8

"""
    Katanemo - identity, and fine-grained authorization for modern [API-first] software companies.

    Public APIs of Katanemo. With Katanemo developers can add support for users, enterprise SSO, machine keys and fine-grained authorization in minutes.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@katanemo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import katanemo_sdk
from katanemo_sdk.models.token_request import TokenRequest  # noqa: E501
from katanemo_sdk.rest import ApiException

class TestTokenRequest(unittest.TestCase):
    """TokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TokenRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenRequest`
        """
        model = katanemo_sdk.models.token_request.TokenRequest()  # noqa: E501
        if include_optional :
            return TokenRequest(
                client_id = '', 
                client_secret = ''
            )
        else :
            return TokenRequest(
        )
        """

    def testTokenRequest(self):
        """Test TokenRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
