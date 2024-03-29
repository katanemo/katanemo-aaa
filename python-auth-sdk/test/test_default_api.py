# coding: utf-8

"""
    Katanemo Authorizer

    Katanemo authorizer service for AAA  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@katanemo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import katanemo_auth
from katanemo_auth.api.default_api import DefaultApi  # noqa: E501
from katanemo_auth.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = katanemo_auth.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_access_logs(self):
        """Test case for add_access_logs

        Add access-logs from ARC.  # noqa: E501
        """
        pass

    def test_authorize_request(self):
        """Test case for authorize_request

        Authorize a request  # noqa: E501
        """
        pass

    def test_get_healthz(self):
        """Test case for get_healthz

        Returns service health  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
