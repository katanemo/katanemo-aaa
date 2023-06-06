# coding: utf-8

from fastapi.testclient import TestClient


from katanemo_sdk.models.assign_role_obj import AssignRoleObj  # noqa: F401
from katanemo_sdk.models.assume_role_obj import AssumeRoleObj  # noqa: F401
from katanemo_sdk.models.bad_request_exception import BadRequestException  # noqa: F401
from katanemo_sdk.models.client_key_object import ClientKeyObject  # noqa: F401
from katanemo_sdk.models.client_key_request import ClientKeyRequest  # noqa: F401
from katanemo_sdk.models.client_key_response import ClientKeyResponse  # noqa: F401
from katanemo_sdk.models.conflict_exception import ConflictException  # noqa: F401
from katanemo_sdk.models.error import Error  # noqa: F401
from katanemo_sdk.models.get_tags_request import GetTagsRequest  # noqa: F401
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException  # noqa: F401
from katanemo_sdk.models.o_auth_token_request import OAuthTokenRequest  # noqa: F401
from katanemo_sdk.models.o_auth_token_response import OAuthTokenResponse  # noqa: F401
from katanemo_sdk.models.role_request import RoleRequest  # noqa: F401
from katanemo_sdk.models.role_response import RoleResponse  # noqa: F401
from katanemo_sdk.models.tags import Tags  # noqa: F401
from katanemo_sdk.models.token_request import TokenRequest  # noqa: F401
from katanemo_sdk.models.token_response import TokenResponse  # noqa: F401
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException  # noqa: F401
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException  # noqa: F401
from katanemo_sdk.models.user_response import UserResponse  # noqa: F401


def test_assign_role_to_principal(client: TestClient):
    """Test case for assign_role_to_principal

    Assign role
    """
    assign_role_obj = {"role_id":"roleId","principal_id":"principalId"}

    headers = {
    }
    response = client.request(
        "POST",
        "/assignrole",
        headers=headers,
        json=assign_role_obj,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_assume_role(client: TestClient):
    """Test case for assume_role

    Assume role
    """
    assume_role_obj = {"role_id":"roleId","principal_id":"principalId"}

    headers = {
    }
    response = client.request(
        "POST",
        "/assumeRole",
        headers=headers,
        json=assume_role_obj,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_client_key(client: TestClient):
    """Test case for create_client_key

    Create API Key
    """
    client_key_request = {"client_name":"clientName","default_role_id":"defaultRoleId"}

    headers = {
    }
    response = client.request(
        "POST",
        "/org/{accountId}/keys".format(accountId='account_id_example'),
        headers=headers,
        json=client_key_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_role(client: TestClient):
    """Test case for create_role

    Creates Role
    """
    role_request = {"account_id":"accountId","rolename":"rolename","description":"description","service_id":"serviceId","policy":{"policy_content":"policyContent"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/org/{accountId}/role".format(accountId='account_id_example'),
        headers=headers,
        json=role_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_tags(client: TestClient):
    """Test case for create_tags

    Add tags to a resource
    """
    tags = {"account_id":"accountId","service_id_path":"serviceIdPath","resource_id":"resourceId","name":"name","service_id":"serviceId","token":"token","tags":{"key":["tags","tags"]}}

    headers = {
    }
    response = client.request(
        "POST",
        "/service/{serviceId}/tags".format(serviceId='service_id_example'),
        headers=headers,
        json=tags,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_client_key(client: TestClient):
    """Test case for delete_client_key

    Delete API Key
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/org/{accountId}/key/{keyId}".format(accountId='account_id_example', keyId='key_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_client_key(client: TestClient):
    """Test case for get_client_key

    Get API Key
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/key/{keyId}".format(accountId='account_id_example', keyId='key_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_client_key_list(client: TestClient):
    """Test case for get_client_key_list

    List API Keys
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/keys".format(accountId='account_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_o_auth_token(client: TestClient):
    """Test case for get_o_auth_token

    OAuth Token
    """
    o_auth_token_request = {"code":"code","client_id":"clientId","client_secret":"clientSecret"}

    headers = {
    }
    response = client.request(
        "POST",
        "/oauth/token",
        headers=headers,
        json=o_auth_token_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_role(client: TestClient):
    """Test case for get_role

    Get Role
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/role/{roleId}".format(accountId='account_id_example', roleId='role_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_roles_for_account(client: TestClient):
    """Test case for get_roles_for_account

    List Roles
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/role".format(accountId='account_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_short_term_token(client: TestClient):
    """Test case for get_short_term_token

    Get Token
    """
    token_request = {"client_id":"clientId","client_secret":"clientSecret"}

    headers = {
    }
    response = client.request(
        "POST",
        "/token",
        headers=headers,
        json=token_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_tags_for_resource(client: TestClient):
    """Test case for get_tags_for_resource

    Gets tags for a resource
    """
    get_tags_request = {"account_id":"accountId","resource_id":"resourceId","resource_name":"resourceName"}

    headers = {
    }
    response = client.request(
        "GET",
        "/service/{serviceId}/tags".format(serviceId='service_id_example'),
        headers=headers,
        json=get_tags_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_role(client: TestClient):
    """Test case for update_role

    Update Role
    """
    role_request = {"account_id":"accountId","rolename":"rolename","description":"description","service_id":"serviceId","policy":{"policy_content":"policyContent"}}

    headers = {
    }
    response = client.request(
        "PUT",
        "/org/{accountId}/role/{roleId}".format(accountId='account_id_example', roleId='role_id_example'),
        headers=headers,
        json=role_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

