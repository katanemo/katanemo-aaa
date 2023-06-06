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
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException
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
