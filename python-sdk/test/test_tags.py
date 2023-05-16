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
from katanemo_sdk.models.tags import Tags  # noqa: E501
from katanemo_sdk.rest import ApiException

class TestTags(unittest.TestCase):
    """Tags unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Tags
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Tags`
        """
        model = katanemo_sdk.models.tags.Tags()  # noqa: E501
        if include_optional :
            return Tags(
                service_id_path = '', 
                service_id = '', 
                name = '', 
                resource_id = '', 
                account_id = '', 
                token = '', 
                tags = {
                    'key' : [
                        ''
                        ]
                    }
            )
        else :
            return Tags(
                service_id = '',
                name = '',
                resource_id = '',
                token = '',
                tags = {
                    'key' : [
                        ''
                        ]
                    },
        )
        """

    def testTags(self):
        """Test Tags"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
