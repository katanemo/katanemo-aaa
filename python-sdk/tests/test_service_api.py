# coding: utf-8

from fastapi.testclient import TestClient


from katanemo_sdk.models.bad_request_exception import BadRequestException  # noqa: F401
from katanemo_sdk.models.conflict_exception import ConflictException  # noqa: F401
from katanemo_sdk.models.error import Error  # noqa: F401
from katanemo_sdk.models.get_developer_public_keys200_response import GetDeveloperPublicKeys200Response  # noqa: F401
from katanemo_sdk.models.get_tags_request import GetTagsRequest  # noqa: F401
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException  # noqa: F401
from katanemo_sdk.models.service_response_obj import ServiceResponseObj  # noqa: F401
from katanemo_sdk.models.tags import Tags  # noqa: F401
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException  # noqa: F401
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException  # noqa: F401


def test_create_service(client: TestClient):
    """Test case for create_service

    Create Service
    """

    headers = {
    }
    data = {
        "name": 'name_example',
        "description": 'description_example',
        "redirect_url": 'redirect_url_example',
        "api_spec_file": '/path/to/file',
        "auth_exclusion_paths": ['auth_exclusion_paths_example'],
        "display_name": 'display_name_example',
        "logo_url": 'logo_url_example',
        "details_image_url": 'details_image_url_example',
        "terms_url": 'terms_url_example',
        "privacy_url": 'privacy_url_example',
        "docs_url": 'docs_url_example'
    }
    response = client.request(
        "POST",
        "/service",
        headers=headers,
        data=data,
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


def test_delete_service(client: TestClient):
    """Test case for delete_service

    Delete Service
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/service/{serviceId}".format(serviceId='service_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_default_service(client: TestClient):
    """Test case for get_default_service

    Get Details for Katanemo AAA
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/service/3xA",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_developer_public_keys(client: TestClient):
    """Test case for get_developer_public_keys

    JWKS endpoint for Service
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/service/{serviceId}/.well-known/jwks.json".format(serviceId='service_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_service(client: TestClient):
    """Test case for get_service

    Get Service
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/service/{serviceId}".format(serviceId='service_id_example'),
        headers=headers,
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


def test_list_services_by_developer(client: TestClient):
    """Test case for list_services_by_developer

    List Services
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/service",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_service(client: TestClient):
    """Test case for update_service

    Update Service
    """

    headers = {
    }
    data = {
        "name": 'name_example',
        "description": 'description_example',
        "redirect_url": 'redirect_url_example',
        "api_spec_file": '/path/to/file',
        "auth_exclusion_paths": ['auth_exclusion_paths_example'],
        "display_name": 'display_name_example',
        "logo_url": 'logo_url_example',
        "details_image_url": 'details_image_url_example',
        "terms_url": 'terms_url_example',
        "privacy_url": 'privacy_url_example',
        "docs_url": 'docs_url_example'
    }
    response = client.request(
        "PUT",
        "/service/{serviceId}".format(serviceId='service_id_example'),
        headers=headers,
        data=data,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

