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
from katanemo_identity.models.saml_obj import SAMLObj  # noqa: E501
from katanemo_identity.rest import ApiException

class TestSAMLObj(unittest.TestCase):
    """SAMLObj unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SAMLObj
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SAMLObj`
        """
        model = katanemo_identity.models.saml_obj.SAMLObj()  # noqa: E501
        if include_optional :
            return SAMLObj(
                connection_id = '', 
                id_provider = '', 
                state = '', 
                name = '', 
                default_role_id = '', 
                login_link = '', 
                metadata_link = '', 
                acs_link = '', 
                audience_link = '', 
                attribute_role_mappings = [
                    katanemo_identity.models.attribute_role_mapping.AttributeRoleMapping(
                        attribute = '', 
                        value = '', 
                        role_id = '', )
                    ], 
                root_url = '', 
                account_id = '', 
                service_id = ''
            )
        else :
            return SAMLObj(
                id_provider = '',
                default_role_id = '',
                account_id = '',
                service_id = '',
        )
        """

    def testSAMLObj(self):
        """Test SAMLObj"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
