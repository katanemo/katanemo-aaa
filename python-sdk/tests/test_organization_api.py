# coding: utf-8

from fastapi.testclient import TestClient


from katanemo_sdk.models.bad_request_exception import BadRequestException  # noqa: F401
from katanemo_sdk.models.client_key_object import ClientKeyObject  # noqa: F401
from katanemo_sdk.models.client_key_request import ClientKeyRequest  # noqa: F401
from katanemo_sdk.models.client_key_response import ClientKeyResponse  # noqa: F401
from katanemo_sdk.models.conflict_exception import ConflictException  # noqa: F401
from katanemo_sdk.models.error import Error  # noqa: F401
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException  # noqa: F401
from katanemo_sdk.models.organization_response import OrganizationResponse  # noqa: F401
from katanemo_sdk.models.role_request import RoleRequest  # noqa: F401
from katanemo_sdk.models.role_response import RoleResponse  # noqa: F401
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException  # noqa: F401
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException  # noqa: F401
from katanemo_sdk.models.update_organization_request import UpdateOrganizationRequest  # noqa: F401
from katanemo_sdk.models.user_request import UserRequest  # noqa: F401
from katanemo_sdk.models.user_response import UserResponse  # noqa: F401


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


def test_create_user_for_account(client: TestClient):
    """Test case for create_user_for_account

    Invite User
    """
    user_request = {"account_id":"accountId","roles":["roleId1","roleId2","roleId3"],"user_id":"userId","tags":{"key":["tags","tags"]}}

    headers = {
    }
    response = client.request(
        "POST",
        "/org/{accountId}/user".format(accountId='account_id_example'),
        headers=headers,
        json=user_request,
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


def test_get_account_info(client: TestClient):
    """Test case for get_account_info

    Get Organization
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}".format(accountId='account_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_account_organization(client: TestClient):
    """Test case for get_account_organization

    List Organizations
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org",
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


def test_get_user(client: TestClient):
    """Test case for get_user

    Get User
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/user/{userId}".format(accountId='account_id_example', userId='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_users_for_account(client: TestClient):
    """Test case for get_users_for_account

    List Users
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/user".format(accountId='account_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_account_info(client: TestClient):
    """Test case for update_account_info

    Update Organization
    """
    update_organization_request = {"name":"name"}

    headers = {
    }
    response = client.request(
        "PUT",
        "/org/{accountId}".format(accountId='account_id_example'),
        headers=headers,
        json=update_organization_request,
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


def test_update_user(client: TestClient):
    """Test case for update_user

    Update user
    """
    user_request = {"account_id":"accountId","roles":["roleId1","roleId2","roleId3"],"user_id":"userId","tags":{"key":["tags","tags"]}}

    headers = {
    }
    response = client.request(
        "PUT",
        "/org/{accountId}/user/{userId}".format(userId='user_id_example', accountId='account_id_example'),
        headers=headers,
        json=user_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_verify_account_domain(client: TestClient):
    """Test case for verify_account_domain

    Verify Domain
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/org/{accountId}/verify".format(accountId='account_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

