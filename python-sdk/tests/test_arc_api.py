# coding: utf-8

from fastapi.testclient import TestClient


from katanemo_sdk.models.bad_request_exception import BadRequestException  # noqa: F401
from katanemo_sdk.models.conflict_exception import ConflictException  # noqa: F401
from katanemo_sdk.models.error import Error  # noqa: F401
from katanemo_sdk.models.init_arc_response import InitArcResponse  # noqa: F401
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException  # noqa: F401
from katanemo_sdk.models.role_response import RoleResponse  # noqa: F401
from katanemo_sdk.models.tags import Tags  # noqa: F401
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException  # noqa: F401
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException  # noqa: F401


def test_get_roles_for_service(client: TestClient):
    """Test case for get_roles_for_service

    Get Service Roles
    """
    params = [("limit", 56)]
    headers = {
    }
    response = client.request(
        "GET",
        "/arc/{serviceId}/role".format(serviceId='service_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_tags_for_service(client: TestClient):
    """Test case for get_tags_for_service

    Get Resource Tags
    """
    params = [("limit", 56)]
    headers = {
    }
    response = client.request(
        "GET",
        "/arc/{serviceId}/tags".format(serviceId='service_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_init_arc_client(client: TestClient):
    """Test case for init_arc_client

    Initialize ARC Client
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/arc/{serviceId}/init".format(serviceId='service_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

