# coding: utf-8

"""
    Katanemo - identity, and fine-grained authorization for modern { API-first } software companies.

    With Katanemo developers can add support for users, enterprise SSO, machine keys and fine-grained authorization in minutes.  # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Contact: support@katanemo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import katanemo_identity
from katanemo_identity.models.internal_server_error_exception import InternalServerErrorException  # noqa: E501
from katanemo_identity.rest import ApiException

class TestInternalServerErrorException(unittest.TestCase):
    """InternalServerErrorException unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InternalServerErrorException
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalServerErrorException`
        """
        model = katanemo_identity.models.internal_server_error_exception.InternalServerErrorException()  # noqa: E501
        if include_optional :
            return InternalServerErrorException(
                message = '', 
                error_code = ''
            )
        else :
            return InternalServerErrorException(
        )
        """

    def testInternalServerErrorException(self):
        """Test InternalServerErrorException"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
