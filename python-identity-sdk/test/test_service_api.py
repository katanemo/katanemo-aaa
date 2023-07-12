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
from katanemo_identity.api.service_api import ServiceApi  # noqa: E501
from katanemo_identity.rest import ApiException


class TestServiceApi(unittest.TestCase):
    """ServiceApi unit test stubs"""

    def setUp(self):
        self.api = katanemo_identity.api.service_api.ServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_service(self):
        """Test case for create_service

        Create Service  # noqa: E501
        """
        pass

    def test_create_tags(self):
        """Test case for create_tags

        Add tags to a resource  # noqa: E501
        """
        pass

    def test_delete_service(self):
        """Test case for delete_service

        Delete Service  # noqa: E501
        """
        pass

    def test_get_default_service(self):
        """Test case for get_default_service

        Get Details for Katanemo AAA  # noqa: E501
        """
        pass

    def test_get_developer_public_keys(self):
        """Test case for get_developer_public_keys

        JWKS endpoint for Service  # noqa: E501
        """
        pass

    def test_get_service(self):
        """Test case for get_service

        Get Service  # noqa: E501
        """
        pass

    def test_get_tags_for_resource(self):
        """Test case for get_tags_for_resource

        Gets tags for a resource  # noqa: E501
        """
        pass

    def test_list_services_by_developer(self):
        """Test case for list_services_by_developer

        List Services  # noqa: E501
        """
        pass

    def test_update_service(self):
        """Test case for update_service

        Update Service  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()