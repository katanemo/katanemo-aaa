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
from katanemo_sdk.models.initial_login_request import InitialLoginRequest
from katanemo_sdk.models.initial_login_response import InitialLoginResponse
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.models.login_token import LoginToken
from katanemo_sdk.models.login_with_password_request import LoginWithPasswordRequest
from katanemo_sdk.models.password_policy import PasswordPolicy
from katanemo_sdk.models.set_password_request import SetPasswordRequest
from katanemo_sdk.models.signup_request import SignupRequest
from katanemo_sdk.models.signup_response import SignupResponse
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException
from katanemo_sdk.models.user_confirmation_response import UserConfirmationResponse


router = APIRouter()


@router.get(
    "/confirmUser/{confirmationCode}",
    responses={
        200: {"model": UserConfirmationResponse, "description": "The first user (email) has been subscribed to a particular service and an organization id has been created"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sign-up/login"],
    summary="Confirm User",
    response_model_by_alias=True,
)
async def confirm_user(
    confirmationCode: str = Path(None, description=""),
) -> UserConfirmationResponse:
    """Confirm that the user belongs to the organization (email) they signed-up with. Used by Katanemo to verify developers signing-up for its 3xA service and for service developers on-boarding their customers (subscribers)"""
    ...


@router.get(
    "/set-password/{serviceId}",
    responses={
        200: {"model": PasswordPolicy, "description": "returns the password stregnth needed to successful set password"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
    },
    tags=["sign-up/login"],
    summary="Get password policy",
    response_model_by_alias=True,
)
async def get_password_policy(
    serviceId: str = Path(None, description=""),
) -> PasswordPolicy:
    """Gets the password policy (length, characters, etc), to help the user set the correct password"""
    ...


@router.post(
    "/login/{serviceId}",
    responses={
        302: {"description": "Redirect to default page for developer after succesful login."},
        200: {"model": LoginToken, "description": "Returns login token in a response object if skipRedirect is set to true."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sign-up/login"],
    summary="Login (Password)",
    response_model_by_alias=True,
)
async def login(
    serviceId: str = Path(None, description=""),
    login_with_password_request: LoginWithPasswordRequest = Body(None, description="Login info of a user"),
) -> LoginToken:
    """Login to any katanemo service. serviceId indicates service user is logging in to."""
    ...


@router.post(
    "/login-init/{serviceId}",
    responses={
        200: {"model": InitialLoginResponse, "description": "This API is used to determine if the user should login via an email/password combination or if the UI should redirect the user to the Idp for SSO"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sign-up/login"],
    summary="Login-init (SSO vs. Password)",
    response_model_by_alias=True,
)
async def login_init(
    serviceId: str = Path(None, description=""),
    initial_login_request: InitialLoginRequest = Body(None, description="Login info (email) of the user"),
) -> InitialLoginResponse:
    """Login-init helps developers determine if the user should be presented a SAML/SSO workflow or a user/password sign-in experience."""
    ...


@router.post(
    "/sign-up/{serviceId}",
    responses={
        200: {"model": SignupResponse, "description": "Signup is successful."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sign-up/login"],
    summary="Sign-up for Service",
    response_model_by_alias=True,
)
async def service_signup(
    serviceId: str = Path(None, description=""),
    signup_request: SignupRequest = Body(None, description="Signup Info of the service developer or a service subscriber"),
) -> SignupResponse:
    """Onborad customers to a particular SaaS service managed by Katanemo. Generates email verification workflows and creates an organization for the customer subscribing to this particular service"""
    ...


@router.post(
    "/set-password/{serviceId}",
    responses={
        200: {"description": "Settting pasword for user is successful."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sign-up/login"],
    summary="Set Password",
    response_model_by_alias=True,
)
async def set_password(
    serviceId: str = Path(None, description=""),
    set_password_request: SetPasswordRequest = Body(None, description="Set password info"),
) -> None:
    """Allows the user to set password after verficiation via a session token."""
    ...
