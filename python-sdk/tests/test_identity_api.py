# coding: utf-8

from fastapi.testclient import TestClient


from katanemo_sdk.models.bad_request_exception import BadRequestException  # noqa: F401
from katanemo_sdk.models.client_key_object import ClientKeyObject  # noqa: F401
from katanemo_sdk.models.client_key_request import ClientKeyRequest  # noqa: F401
from katanemo_sdk.models.client_key_response import ClientKeyResponse  # noqa: F401
from katanemo_sdk.models.conflict_exception import ConflictException  # noqa: F401
from katanemo_sdk.models.error import Error  # noqa: F401
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException  # noqa: F401
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException  # noqa: F401
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException  # noqa: F401
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

