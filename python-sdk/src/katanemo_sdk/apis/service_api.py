# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from katanemo_sdk.models.extra_models import TokenModel  # noqa: F401
from katanemo_sdk.models.bad_request_exception import BadRequestException
from katanemo_sdk.models.conflict_exception import ConflictException
from katanemo_sdk.models.error import Error
from katanemo_sdk.models.get_developer_public_keys200_response import GetDeveloperPublicKeys200Response
from katanemo_sdk.models.get_tags_request import GetTagsRequest
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.models.service_response_obj import ServiceResponseObj
from katanemo_sdk.models.tags import Tags
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException


router = APIRouter()


@router.post(
    "/service",
    responses={
        200: {"model": ServiceResponseObj, "description": "Service Successfully Created."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["service"],
    summary="Create Service",
    response_model_by_alias=True,
)
async def create_service(
    name: str = Form(None, description="Service Name"),
    redirect_url: str = Form(None, description="Redirect URL after a successful login."),
    api_spec_file: str = Form(None, description="openapi service json or yaml file"),
    description: str = Form(None, description="Service Description"),
    auth_exclusion_paths: List[str] = Form(None, description="List of paths for which we do not require authentication"),
    display_name: str = Form(None, description="Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages"),
    logo_url: str = Form(None, description="The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages"),
    details_image_url: str = Form(None, description="The URL of image showing details about the service to be displayed on the sign-up page."),
    terms_url: str = Form(None, description="The URL for the terms of the service"),
    privacy_url: str = Form(None, description="The URL for the privacy of the service"),
    docs_url: str = Form(None, description="The URL for the documentation of the service"),
) -> ServiceResponseObj:
    """Create a Service in Katanemo. Once a service is created Katanemo  identity and authorization capabilities on behalf of SaaS (API) Developers"""
    ...


@router.post(
    "/service/{serviceId}/tags",
    responses={
        200: {"model": Tags, "description": "User account"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["service","access-control"],
    summary="Add tags to a resource",
    response_model_by_alias=True,
)
async def create_tags(
    serviceId: str = Path(None, description=""),
    tags: Tags = Body(None, description="Tags and resource id"),
) -> Tags:
    """Add tags (key/value pair) to a particular resource that is created for a service, for a particular organization account id."""
    ...


@router.delete(
    "/service/{serviceId}",
    responses={
        200: {"description": "Deleted service."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["service"],
    summary="Delete Service",
    response_model_by_alias=True,
)
async def delete_service(
    serviceId: str = Path(None, description=""),
) -> None:
    """Deletes a service. Note the delete operation is a &#39;soft&#39; delete where by organizations can&#39;t access your service. Requires a bearer token to validate that the caller can delete the service."""
    ...


@router.get(
    "/service/3xA",
    responses={
        200: {"model": ServiceResponseObj, "description": "service"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["service"],
    summary="Get Details for Katanemo AAA",
    response_model_by_alias=True,
)
async def get_default_service(
) -> ServiceResponseObj:
    """Gets details about Katanemo&#39;s AAA SaaS service. Katanemo is powered by Katanemo, and our 3xA service uses the same core identity and authorization capabilities that we offer SaaS (API) developers"""
    ...


@router.get(
    "/service/{serviceId}/.well-known/jwks.json",
    responses={
        200: {"model": GetDeveloperPublicKeys200Response, "description": "List of public keys for developer"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["service"],
    summary="JWKS endpoint for Service",
    response_model_by_alias=True,
)
async def get_developer_public_keys(
    serviceId: str = Path(None, description=""),
) -> GetDeveloperPublicKeys200Response:
    """Gets public key that can be used to verify jwt token issued by Katanemo. This API does not require bearer authorization"""
    ...


@router.get(
    "/service/{serviceId}",
    responses={
        200: {"model": ServiceResponseObj, "description": "service"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["service"],
    summary="Get Service",
    response_model_by_alias=True,
)
async def get_service(
    serviceId: str = Path(None, description=""),
) -> ServiceResponseObj:
    """Gets a Katanemo Service. The principal token must be present in the bearer header to retrieve the service details, unless the service is public"""
    ...


@router.get(
    "/service/{serviceId}/tags",
    responses={
        200: {"model": Tags, "description": "tags"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
    },
    tags=["service","access-control"],
    summary="Gets tags for a resource",
    response_model_by_alias=True,
)
async def get_tags_for_resource(
    serviceId: str = Path(None, description=""),
    get_tags_request: GetTagsRequest = Body(None, description="Tags and resource id"),
) -> Tags:
    """Gets tags associated with a resource of a service"""
    ...


@router.get(
    "/service",
    responses={
        200: {"model": List[ServiceResponseObj], "description": "List all services belonging to a developer"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["service"],
    summary="List Services",
    response_model_by_alias=True,
)
async def list_services_by_developer(
) -> List[ServiceResponseObj]:
    """List services that belong to a particular developer. Requires bearer token authorization"""
    ...


@router.put(
    "/service/{serviceId}",
    responses={
        200: {"model": ServiceResponseObj, "description": "Updated service object."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["service"],
    summary="Update Service",
    response_model_by_alias=True,
)
async def update_service(
    serviceId: str = Path(None, description=""),
    name: str = Form(None, description="Service Name"),
    description: str = Form(None, description="Service Description"),
    redirect_url: str = Form(None, description="Redirect URL after a successful login."),
    api_spec_file: str = Form(None, description="openapi service json or yaml file"),
    auth_exclusion_paths: List[str] = Form(None, description="List of paths for which we do not require authentication"),
    display_name: str = Form(None, description="Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages"),
    logo_url: str = Form(None, description="The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages"),
    details_image_url: str = Form(None, description="The URL of image showing details about the service to be displayed on the sign-up page."),
    terms_url: str = Form(None, description="The URL for the terms of the service"),
    privacy_url: str = Form(None, description="The URL for the privacy of the service"),
    docs_url: str = Form(None, description="The URL for the documentatio of the service"),
) -> ServiceResponseObj:
    """Update Service. Requires bearer token authorization for the caller updating the service"""
    ...
