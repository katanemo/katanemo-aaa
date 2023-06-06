# coding: utf-8

from fastapi.testclient import TestClient


from katanemo_sdk.models.attribute_role_mapping import AttributeRoleMapping  # noqa: F401
from katanemo_sdk.models.bad_request_exception import BadRequestException  # noqa: F401
from katanemo_sdk.models.conflict_exception import ConflictException  # noqa: F401
from katanemo_sdk.models.error import Error  # noqa: F401
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException  # noqa: F401
from katanemo_sdk.models.oidc_obj import OIDCObj  # noqa: F401
from katanemo_sdk.models.saml_obj import SAMLObj  # noqa: F401
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException  # noqa: F401
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException  # noqa: F401


def test_create_oidcc_onnection(client: TestClient):
    """Test case for create_oidcc_onnection

    Creates OIDC connection
    """
    oidc_obj = {"redirect_url":"redirectURL","client_id":"clientId","jwks_endpoint":"jwksEndpoint","oidc_config_endpoint":"oidcConfigEndpoint","nonce":"nonce","authorization_endpoint":"authorizationEndpoint","account_id":"accountId","token_endpoint":"tokenEndpoint","issuer_endpoint":"issuerEndpoint","name":"name","connection_id":"connectionId","client_secret":"clientSecret","state":"state","service_id":"serviceId","user_info_endpoint":"userInfoEndpoint"}

    headers = {
    }
    response = client.request(
        "POST",
        "/org/{accountId}/sso-connections/oidc".format(accountId='account_id_example'),
        headers=headers,
        json=oidc_obj,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_saml_connection(client: TestClient):
    """Test case for create_saml_connection

    Creates SAML connection
    """
    saml_obj = {"audience_link":"audienceLink","login_link":"loginLink","acs_link":"acsLink","root_url":"rootURL","account_id":"accountId","id_provider":"idProvider","name":"name","connection_id":"connectionId","attribute_role_mappings":[{"role_id":"roleId","attribute":"attribute","value":"value"},{"role_id":"roleId","attribute":"attribute","value":"value"}],"state":"state","metadata_link":"metadataLink","service_id":"serviceId","default_role_id":"defaultRoleId"}

    headers = {
    }
    response = client.request(
        "POST",
        "/org/{accountId}/sso-connections/saml".format(accountId='account_id_example'),
        headers=headers,
        json=saml_obj,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_saml_connection_mapping(client: TestClient):
    """Test case for create_saml_connection_mapping

    MAP SAML Attributes
    """
    attribute_role_mapping = {"role_id":"roleId","attribute":"attribute","value":"value"}

    headers = {
    }
    response = client.request(
        "POST",
        "/org/{accountId}/sso-connections/saml/{connectionId}/mapAttributeToRoles".format(accountId='account_id_example', connectionId='connection_id_example'),
        headers=headers,
        json=attribute_role_mapping,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_oidc_connection(client: TestClient):
    """Test case for delete_oidc_connection

    Delete OIDC connection
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/org/{accountId}/sso-connections/oidc/{connectionId}".format(accountId='account_id_example', connectionId='connection_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_oidc_connection(client: TestClient):
    """Test case for get_oidc_connection

    Get OIDC connection
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/sso-connections/oidc/{connectionId}".format(accountId='account_id_example', connectionId='connection_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_oidc_connections_for_account(client: TestClient):
    """Test case for get_oidc_connections_for_account

    List OIDC Connections
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/sso-connections/oidc".format(accountId='account_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_saml_connection(client: TestClient):
    """Test case for get_saml_connection

    Get connection
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/sso-connections/saml/{connectionId}".format(accountId='account_id_example', connectionId='connection_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_saml_connections_for_account(client: TestClient):
    """Test case for get_saml_connections_for_account

    List SAML Connections
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/sso-connections/saml".format(accountId='account_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_o_idc_login_trigger(client: TestClient):
    """Test case for o_idc_login_trigger

    Trigger OIDC SSO
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/sso-connections/oidc/{connectionId}/login-trigger".format(connectionId='connection_id_example', accountId='account_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_oidc_sso_call_back(client: TestClient):
    """Test case for oidc_sso_call_back

    OIDC Callback
    """
    params = [("code", 'code_example'),     ("state", 'state_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/sso-connections/oidc/{connectionId}/sso-callback".format(accountId='account_id_example', connectionId='connection_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_s_aml_login_trigger(client: TestClient):
    """Test case for s_aml_login_trigger

    Triggers SAML SSO
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/sso-connections/saml/{connectionId}/login-trigger".format(connectionId='connection_id_example', accountId='account_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_saml_sso_call_back(client: TestClient):
    """Test case for saml_sso_call_back

    SAML Callback
    """
    params = [("saml_response", 'saml_response_example')]
    headers = {
    }
    data = {
        "saml_response2": 'saml_response_example'
    }
    response = client.request(
        "POST",
        "/org/{accountId}/sso-connections/saml/{connectionId}/sso-callback/saml/acs".format(accountId='account_id_example', connectionId='connection_id_example'),
        headers=headers,
        data=data,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_oidc_connection(client: TestClient):
    """Test case for update_oidc_connection

    Update OIDC connection
    """
    oidc_obj = {"redirect_url":"redirectURL","client_id":"clientId","jwks_endpoint":"jwksEndpoint","oidc_config_endpoint":"oidcConfigEndpoint","nonce":"nonce","authorization_endpoint":"authorizationEndpoint","account_id":"accountId","token_endpoint":"tokenEndpoint","issuer_endpoint":"issuerEndpoint","name":"name","connection_id":"connectionId","client_secret":"clientSecret","state":"state","service_id":"serviceId","user_info_endpoint":"userInfoEndpoint"}

    headers = {
    }
    response = client.request(
        "PUT",
        "/org/{accountId}/sso-connections/oidc/{connectionId}".format(accountId='account_id_example', connectionId='connection_id_example'),
        headers=headers,
        json=oidc_obj,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_saml_connection(client: TestClient):
    """Test case for update_saml_connection

    Update SAML connection
    """
    saml_obj = {"audience_link":"audienceLink","login_link":"loginLink","acs_link":"acsLink","root_url":"rootURL","account_id":"accountId","id_provider":"idProvider","name":"name","connection_id":"connectionId","attribute_role_mappings":[{"role_id":"roleId","attribute":"attribute","value":"value"},{"role_id":"roleId","attribute":"attribute","value":"value"}],"state":"state","metadata_link":"metadataLink","service_id":"serviceId","default_role_id":"defaultRoleId"}

    headers = {
    }
    response = client.request(
        "PUT",
        "/org/{accountId}/sso-connections/saml/{connectionId}".format(accountId='account_id_example', connectionId='connection_id_example'),
        headers=headers,
        json=saml_obj,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

