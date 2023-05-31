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

import katanemo_sdk
from katanemo_sdk.api.default_api import DefaultApi  # noqa: E501
from katanemo_sdk.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = katanemo_sdk.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_assign_role_to_principal(self):
        """Test case for assign_role_to_principal

        Assign role to an identity principal  # noqa: E501
        """
        pass

    def test_assume_role(self):
        """Test case for assume_role

        Creates a token with requested roleId  # noqa: E501
        """
        pass

    def test_confirm_user(self):
        """Test case for confirm_user

        Confirm that the user belongs to the organization (email) they signed-up with. Used by Katanemo to verify developers signing-up for its 3xA service and for service developers on-boarding their customers (subscribers)  # noqa: E501
        """
        pass

    def test_create_client_key(self):
        """Test case for create_client_key

        Creates a new client key  # noqa: E501
        """
        pass

    def test_create_oidcc_onnection(self):
        """Test case for create_oidcc_onnection

        Creates a new OIDC connection  # noqa: E501
        """
        pass

    def test_create_role(self):
        """Test case for create_role

        Creates a new Role  # noqa: E501
        """
        pass

    def test_create_saml_connection(self):
        """Test case for create_saml_connection

        Creates a new SAML connection  # noqa: E501
        """
        pass

    def test_create_saml_connection_mapping(self):
        """Test case for create_saml_connection_mapping

        Creates a new attribute mapping for a SAML connection  # noqa: E501
        """
        pass

    def test_create_service(self):
        """Test case for create_service

        Create a Service object.  # noqa: E501
        """
        pass

    def test_create_tags(self):
        """Test case for create_tags

        creates a resource with provided tags  # noqa: E501
        """
        pass

    def test_create_user_for_account(self):
        """Test case for create_user_for_account

        Creates a new User account tied to the specified organization  # noqa: E501
        """
        pass

    def test_delete_client_key(self):
        """Test case for delete_client_key

        delete a client key  # noqa: E501
        """
        pass

    def test_delete_oidc_connection(self):
        """Test case for delete_oidc_connection

        Deletes an OIDC connection  # noqa: E501
        """
        pass

    def test_delete_service(self):
        """Test case for delete_service

        Deletes a service with service ID. Note the delete operation is a \"soft\" delete where by organizations can't access your service. Requires bearer token authorization.  # noqa: E501
        """
        pass

    def test_get_account_info(self):
        """Test case for get_account_info

        Returns an object with information regarding an account  # noqa: E501
        """
        pass

    def test_get_account_organization(self):
        """Test case for get_account_organization

        Returns an object with information regarding an account which is present in the token  # noqa: E501
        """
        pass

    def test_get_audit_logs(self):
        """Test case for get_audit_logs

        Returns list of log entries for a service and account  # noqa: E501
        """
        pass

    def test_get_client_key(self):
        """Test case for get_client_key

        Get details of client key  # noqa: E501
        """
        pass

    def test_get_client_key_list(self):
        """Test case for get_client_key_list

        Get list of all client keys  # noqa: E501
        """
        pass

    def test_get_default_service(self):
        """Test case for get_default_service

        Get details about Katanemo's AAA SaaS service. Katanemo is powered by Katanemo, and our 3xA service uses the same core identity and authorization capabilities that we offer SaaS (API) developers  # noqa: E501
        """
        pass

    def test_get_developer_public_keys(self):
        """Test case for get_developer_public_keys

        Gets public key that can be used to verify jwt token issued by Katanemo. This API does not require bearer authorizationn if service is public  # noqa: E501
        """
        pass

    def test_get_healthz(self):
        """Test case for get_healthz

        Returns service health  # noqa: E501
        """
        pass

    def test_get_o_auth_token(self):
        """Test case for get_o_auth_token

        get token for client id / secret  # noqa: E501
        """
        pass

    def test_get_oidc_connection(self):
        """Test case for get_oidc_connection

        Retrieves an OIDC connection  # noqa: E501
        """
        pass

    def test_get_oidc_connections_for_account(self):
        """Test case for get_oidc_connections_for_account

        Returns a list of all OIDC connections belonging to provided account ID  # noqa: E501
        """
        pass

    def test_get_password_policy(self):
        """Test case for get_password_policy

        Gets the password policy (length, characters, etc), to help the user set the correct password  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        Gets a role  # noqa: E501
        """
        pass

    def test_get_roles_for_account(self):
        """Test case for get_roles_for_account

        Returns a list of all roles belonging to provided account ID  # noqa: E501
        """
        pass

    def test_get_roles_for_service(self):
        """Test case for get_roles_for_service

        """
        pass

    def test_get_saml_connection(self):
        """Test case for get_saml_connection

        Retreive a SAML connection  # noqa: E501
        """
        pass

    def test_get_saml_connections_for_account(self):
        """Test case for get_saml_connections_for_account

        Returns a list of all SAML connections belonging to provided account ID  # noqa: E501
        """
        pass

    def test_get_service(self):
        """Test case for get_service

        Gets a service with service ID  # noqa: E501
        """
        pass

    def test_get_tags_for_resource(self):
        """Test case for get_tags_for_resource

        Gets tags for resource  # noqa: E501
        """
        pass

    def test_get_tags_for_service(self):
        """Test case for get_tags_for_service

        """
        pass

    def test_get_user(self):
        """Test case for get_user

        """
        pass

    def test_get_users_for_account(self):
        """Test case for get_users_for_account

        Returns a list of all users belonging to provided account ID  # noqa: E501
        """
        pass

    def test_init_arc_client(self):
        """Test case for init_arc_client

        """
        pass

    def test_list_services_by_developer(self):
        """Test case for list_services_by_developer

        List services that belong to a particular developer. Requires bearer token authorization  # noqa: E501
        """
        pass

    def test_login(self):
        """Test case for login

        Login to any katanemo service with email and password  # noqa: E501
        """
        pass

    def test_login_init(self):
        """Test case for login_init

        Login-init helps developers determine if the user should be presented a SAML/SSO workflow or a user/password sign-in experience.  # noqa: E501
        """
        pass

    def test_o_idc_login_trigger(self):
        """Test case for o_idc_login_trigger

        Triggers okta signin flow  # noqa: E501
        """
        pass

    def test_oidc_sso_call_back(self):
        """Test case for oidc_sso_call_back

        Handle OIDC SSO login callback  # noqa: E501
        """
        pass

    def test_s_aml_login_trigger(self):
        """Test case for s_aml_login_trigger

        Triggers SAML SSO signin flow  # noqa: E501
        """
        pass

    def test_saml_sso_call_back(self):
        """Test case for saml_sso_call_back

        Handle SAML login callback with SAML assertion. It can be passed as query parameter or payload.  # noqa: E501
        """
        pass

    def test_service_signup(self):
        """Test case for service_signup

        Onborad customers to a particular SaaS service managed by Katanemo  # noqa: E501
        """
        pass

    def test_set_password(self):
        """Test case for set_password

        Set password after user verification.  # noqa: E501
        """
        pass

    def test_update_oidc_connection(self):
        """Test case for update_oidc_connection

        Updates a OIDC connection  # noqa: E501
        """
        pass

    def test_update_role(self):
        """Test case for update_role

        Updates role  # noqa: E501
        """
        pass

    def test_update_saml_connection(self):
        """Test case for update_saml_connection

        Updates a SAML connection  # noqa: E501
        """
        pass

    def test_update_service(self):
        """Test case for update_service

        Update a Service. Requires bearer token authorization  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Updates a user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()