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
import datetime

import katanemo_sdk
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException  # noqa: E501
from katanemo_sdk.rest import ApiException

class TestTooManyRequestsException(unittest.TestCase):
    """TooManyRequestsException unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TooManyRequestsException
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TooManyRequestsException`
        """
        model = katanemo_sdk.models.too_many_requests_exception.TooManyRequestsException()  # noqa: E501
        if include_optional :
            return TooManyRequestsException(
                message = '', 
                error_code = ''
            )
        else :
            return TooManyRequestsException(
        )
        """

    def testTooManyRequestsException(self):
        """Test TooManyRequestsException"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()