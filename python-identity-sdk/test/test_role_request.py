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
from katanemo_identity.models.role_request import RoleRequest  # noqa: E501
from katanemo_identity.rest import ApiException

class TestRoleRequest(unittest.TestCase):
    """RoleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RoleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleRequest`
        """
        model = katanemo_identity.models.role_request.RoleRequest()  # noqa: E501
        if include_optional :
            return RoleRequest(
                account_id = '', 
                rolename = '', 
                description = '', 
                service_id = '', 
                policy = katanemo_identity.models.policy.Policy(
                    policy_content = '', )
            )
        else :
            return RoleRequest(
        )
        """

    def testRoleRequest(self):
        """Test RoleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
