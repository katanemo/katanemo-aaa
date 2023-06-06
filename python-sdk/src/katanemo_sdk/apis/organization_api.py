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
from katanemo_sdk.models.client_key_object import ClientKeyObject
from katanemo_sdk.models.client_key_request import ClientKeyRequest
from katanemo_sdk.models.client_key_response import ClientKeyResponse
from katanemo_sdk.models.conflict_exception import ConflictException
from katanemo_sdk.models.error import Error
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.models.organization_response import OrganizationResponse
from katanemo_sdk.models.role_request import RoleRequest
from katanemo_sdk.models.role_response import RoleResponse
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException
from katanemo_sdk.models.update_organization_request import UpdateOrganizationRequest
from katanemo_sdk.models.user_request import UserRequest
from katanemo_sdk.models.user_response import UserResponse


router = APIRouter()


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
    "/org/{accountId}/user",
    responses={
        200: {"model": UserResponse, "description": "User"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization","identity"],
    summary="Invite User",
    response_model_by_alias=True,
)
async def create_user_for_account(
    accountId: str = Path(None, description=""),
    user_request: UserRequest = Body(None, description="User information"),
) -> UserResponse:
    """Creates a new User and triggers an email verification workflow, followed by set-password"""
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
    "/org/{accountId}",
    responses={
        200: {"model": OrganizationResponse, "description": "Organization"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization"],
    summary="Get Organization",
    response_model_by_alias=True,
)
async def get_account_info(
    accountId: str = Path(None, description=""),
) -> OrganizationResponse:
    """Returns an object with information regarding an account"""
    ...


@router.get(
    "/org",
    responses={
        200: {"model": OrganizationResponse, "description": "Organization of the acccount."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization"],
    summary="List Organizations",
    response_model_by_alias=True,
)
async def get_account_organization(
) -> OrganizationResponse:
    """Returns an object with information regarding an account which is present in the token"""
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


@router.get(
    "/org/{accountId}/user/{userId}",
    responses={
        200: {"model": UserResponse, "description": "user belonging to provided account ID"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization","identity"],
    summary="Get User",
    response_model_by_alias=True,
)
async def get_user(
    accountId: str = Path(None, description=""),
    userId: str = Path(None, description=""),
) -> UserResponse:
    """Get a specific user for a particular organization"""
    ...


@router.get(
    "/org/{accountId}/user",
    responses={
        200: {"model": List[UserResponse], "description": "users belonging to provided account ID"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization","identity"],
    summary="List Users",
    response_model_by_alias=True,
)
async def get_users_for_account(
    accountId: str = Path(None, description=""),
) -> List[UserResponse]:
    """Returns a list of all users belonging to provided organization ID"""
    ...


@router.put(
    "/org/{accountId}",
    responses={
        200: {"description": "Successfully updated organization"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization"],
    summary="Update Organization",
    response_model_by_alias=True,
)
async def update_account_info(
    accountId: str = Path(None, description=""),
    update_organization_request: UpdateOrganizationRequest = Body(None, description="Update account object"),
) -> None:
    """Returns status code for successful or failed update."""
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


@router.put(
    "/org/{accountId}/user/{userId}",
    responses={
        200: {"model": UserResponse, "description": "User"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization","identity"],
    summary="Update user",
    response_model_by_alias=True,
)
async def update_user(
    userId: str = Path(None, description=""),
    accountId: str = Path(None, description=""),
    user_request: UserRequest = Body(None, description="User information"),
) -> UserResponse:
    """Updates a User account"""
    ...


@router.get(
    "/org/{accountId}/verify",
    responses={
        200: {"description": "Domain verified"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["organization"],
    summary="Verify Domain",
    response_model_by_alias=True,
)
async def verify_account_domain(
    accountId: str = Path(None, description=""),
) -> None:
    """Triggers the domain verification flow. If TXT record is created and has the correct verification code, the domain is verified."""
    ...
