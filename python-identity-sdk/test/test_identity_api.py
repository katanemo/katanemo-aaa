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

import katanemo_identity
from katanemo_identity.api.identity_api import IdentityApi  # noqa: E501
from katanemo_identity.rest import ApiException


class TestIdentityApi(unittest.TestCase):
    """IdentityApi unit test stubs"""

    def setUp(self):
        self.api = katanemo_identity.api.identity_api.IdentityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_client_key(self):
        """Test case for create_client_key

        Create API Key  # noqa: E501
        """
        pass

    def test_create_user_for_account(self):
        """Test case for create_user_for_account

        Invite User  # noqa: E501
        """
        pass

    def test_delete_client_key(self):
        """Test case for delete_client_key

        Delete API Key  # noqa: E501
        """
        pass

    def test_get_client_key(self):
        """Test case for get_client_key

        Get API Key  # noqa: E501
        """
        pass

    def test_get_client_key_list(self):
        """Test case for get_client_key_list

        List API Keys  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get User  # noqa: E501
        """
        pass

    def test_get_users_for_account(self):
        """Test case for get_users_for_account

        List Users  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
