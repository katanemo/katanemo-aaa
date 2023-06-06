# coding: utf-8

from fastapi.testclient import TestClient


from katanemo_sdk.models.authorize_request import AuthorizeRequest  # noqa: F401
from katanemo_sdk.models.bad_request_exception import BadRequestException  # noqa: F401


def test_authorize(client: TestClient):
    """Test case for authorize

    Initiate the login flow by redirecting to login page
    """
    authorize_request = {"client_id":"clientId","state":"state"}

    headers = {
    }
    response = client.request(
        "GET",
        "/authorize",
        headers=headers,
        json=authorize_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_post_authorize(client: TestClient):
    """Test case for post_authorize

    dummy endpoint for authorize
    """

    headers = {
    }
    response = client.request(
        "POST",
        "/arc/authorize",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

