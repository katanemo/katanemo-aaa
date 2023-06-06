# coding: utf-8

from fastapi.testclient import TestClient




def test_get_healthz(client: TestClient):
    """Test case for get_healthz

    Return Katanemo Health
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/healthz",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

