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
from katanemo_sdk.models.service_response_obj import ServiceResponseObj  # noqa: E501
from katanemo_sdk.rest import ApiException

class TestServiceResponseObj(unittest.TestCase):
    """ServiceResponseObj unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ServiceResponseObj
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceResponseObj`
        """
        model = katanemo_sdk.models.service_response_obj.ServiceResponseObj()  # noqa: E501
        if include_optional :
            return ServiceResponseObj(
                account_id = '', 
                service_id = '', 
                service_name = '', 
                description = '', 
                onboard_url = '', 
                redirect_url = '', 
                api_spec_file_contents = '', 
                apis = [
                    ''
                    ], 
                auth_exclusion_paths = [
                    ''
                    ], 
                version = 56, 
                updated_at = 56, 
                created_at = 56, 
                display_name = '', 
                logo_url = '', 
                details_image_url = '', 
                terms_url = '', 
                privacy_url = '', 
                docs_url = ''
            )
        else :
            return ServiceResponseObj(
                service_id = '',
                service_name = '',
                onboard_url = '',
                redirect_url = '',
                api_spec_file_contents = '',
                apis = [
                    ''
                    ],
        )
        """

    def testServiceResponseObj(self):
        """Test ServiceResponseObj"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
