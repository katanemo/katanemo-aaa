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
from katanemo_sdk.models.assign_role_obj import AssignRoleObj
from katanemo_sdk.models.assume_role_obj import AssumeRoleObj
from katanemo_sdk.models.bad_request_exception import BadRequestException
from katanemo_sdk.models.client_key_object import ClientKeyObject
from katanemo_sdk.models.client_key_request import ClientKeyRequest
from katanemo_sdk.models.client_key_response import ClientKeyResponse
from katanemo_sdk.models.conflict_exception import ConflictException
from katanemo_sdk.models.error import Error
from katanemo_sdk.models.get_tags_request import GetTagsRequest
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.models.o_auth_token_request import OAuthTokenRequest
from katanemo_sdk.models.o_auth_token_response import OAuthTokenResponse
from katanemo_sdk.models.role_request import RoleRequest
from katanemo_sdk.models.role_response import RoleResponse
from katanemo_sdk.models.tags import Tags
from katanemo_sdk.models.token_request import TokenRequest
from katanemo_sdk.models.token_response import TokenResponse
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException
from katanemo_sdk.models.user_response import UserResponse


router = APIRouter()


@router.post(
    "/assignrole",
    responses={
        200: {"model": UserResponse, "description": "User account"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["access-control"],
    summary="Assign role",
    response_model_by_alias=True,
)
async def assign_role_to_principal(
    assign_role_obj: AssignRoleObj = Body(None, description="Role assignment"),
) -> UserResponse:
    """Assign role to an identity principal"""
    ...


@router.post(
    "/assumeRole",
    responses={
        200: {"model": str, "description": "token"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["access-control"],
    summary="Assume role",
    response_model_by_alias=True,
)
async def assume_role(
    assume_role_obj: AssumeRoleObj = Body(None, description="Role assignment"),
) -> str:
    """Creates a token with requested roleId"""
    ...


@router.post(
    "/org/{accountId}/keys",
    responses={
        200: {"model": ClientKeyResponse, "description": "Successful org keys."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization","identity","access-control"],
    summary="Create API Key",
    response_model_by_alias=True,
)
async def create_client_key(
    accountId: str = Path(None, description=""),
    client_key_request: ClientKeyRequest = Body(None, description=""),
) -> ClientKeyResponse:
    """Creates a new client key for accessing a developers APIs"""
    ...


@router.post(
    "/org/{accountId}/role",
    responses={
        200: {"model": RoleResponse, "description": "Role"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization","access-control"],
    summary="Creates Role",
    response_model_by_alias=True,
)
async def create_role(
    accountId: str = Path(None, description=""),
    role_request: RoleRequest = Body(None, description="Role to add to the system"),
) -> RoleResponse:
    """Creates a new Role"""
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
    "/org/{accountId}/key/{keyId}",
    responses={
        200: {"model": str, "description": "Successful deletion of client key."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization","identity","access-control"],
    summary="Delete API Key",
    response_model_by_alias=True,
)
async def delete_client_key(
    accountId: str = Path(None, description=""),
    keyId: str = Path(None, description=""),
) -> str:
    """Delete a particular API Key for an organization."""
    ...


@router.get(
    "/org/{accountId}/key/{keyId}",
    responses={
        200: {"model": ClientKeyObject, "description": "Getting client key successful."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization","identity","access-control"],
    summary="Get API Key",
    response_model_by_alias=True,
)
async def get_client_key(
    accountId: str = Path(None, description=""),
    keyId: str = Path(None, description=""),
) -> ClientKeyObject:
    """Get details of a particular API key for an organization."""
    ...


@router.get(
    "/org/{accountId}/keys",
    responses={
        200: {"model": List[ClientKeyObject], "description": "List of all users successful."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization","identity","access-control"],
    summary="List API Keys",
    response_model_by_alias=True,
)
async def get_client_key_list(
    accountId: str = Path(None, description=""),
) -> List[ClientKeyObject]:
    """List all client keys for an organization accessing a developers service"""
    ...


@router.post(
    "/oauth/token",
    responses={
        200: {"model": OAuthTokenResponse, "description": "Getting token for client ID successful."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["access-control"],
    summary="OAuth Token",
    response_model_by_alias=True,
)
async def get_o_auth_token(
    o_auth_token_request: OAuthTokenRequest = Body(None, description=""),
) -> OAuthTokenResponse:
    """Get an OAuth2.0 Token for an Authorization Code"""
    ...


@router.get(
    "/org/{accountId}/role/{roleId}",
    responses={
        200: {"model": RoleResponse, "description": "role"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization","access-control"],
    summary="Get Role",
    response_model_by_alias=True,
)
async def get_role(
    accountId: str = Path(None, description=""),
    roleId: str = Path(None, description=""),
) -> RoleResponse:
    """Gets a particular role for an organization"""
    ...


@router.get(
    "/org/{accountId}/role",
    responses={
        200: {"model": List[RoleResponse], "description": "roles belonging to provided account ID"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization","access-control"],
    summary="List Roles",
    response_model_by_alias=True,
)
async def get_roles_for_account(
    accountId: str = Path(None, description=""),
) -> List[RoleResponse]:
    """Returns a list of all roles belonging to provided organization ID"""
    ...


@router.post(
    "/token",
    responses={
        200: {"model": TokenResponse, "description": "Generate Token for an authentication principal"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["access-control"],
    summary="Get Token",
    response_model_by_alias=True,
)
async def get_short_term_token(
    token_request: TokenRequest = Body(None, description=""),
) -> TokenResponse:
    """Returns a short-lived token for API key/secret pair. Tokens contain claims that identify what a principal can or cannot do."""
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


@router.put(
    "/org/{accountId}/role/{roleId}",
    responses={
        200: {"model": RoleResponse, "description": "Updated service object."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization","access-control"],
    summary="Update Role",
    response_model_by_alias=True,
)
async def update_role(
    accountId: str = Path(None, description=""),
    roleId: str = Path(None, description=""),
    role_request: RoleRequest = Body(None, description="Role object that is being updated."),
) -> RoleResponse:
    """Update role"""
    ...
