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
from katanemo_sdk.models.attribute_role_mapping import AttributeRoleMapping
from katanemo_sdk.models.bad_request_exception import BadRequestException
from katanemo_sdk.models.conflict_exception import ConflictException
from katanemo_sdk.models.error import Error
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.models.oidc_obj import OIDCObj
from katanemo_sdk.models.saml_obj import SAMLObj
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException


router = APIRouter()


@router.post(
    "/org/{accountId}/sso-connections/oidc",
    responses={
        200: {"model": OIDCObj, "description": "OIDCObj"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="Creates OIDC connection",
    response_model_by_alias=True,
)
async def create_oidcc_onnection(
    accountId: str = Path(None, description=""),
    oidc_obj: OIDCObj = Body(None, description="ODIC connection attributes"),
) -> OIDCObj:
    """Creates a new OIDC connection"""
    ...


@router.post(
    "/org/{accountId}/sso-connections/saml",
    responses={
        200: {"model": SAMLObj, "description": "SAMLObj"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="Creates SAML connection",
    response_model_by_alias=True,
)
async def create_saml_connection(
    accountId: str = Path(None, description=""),
    saml_obj: SAMLObj = Body(None, description="SAML connection attributes"),
) -> SAMLObj:
    """Creates a new SAML connection"""
    ...


@router.post(
    "/org/{accountId}/sso-connections/saml/{connectionId}/mapAttributeToRoles",
    responses={
        200: {"model": SAMLObj, "description": "SAMLObj"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="MAP SAML Attributes",
    response_model_by_alias=True,
)
async def create_saml_connection_mapping(
    accountId: str = Path(None, description=""),
    connectionId: str = Path(None, description=""),
    attribute_role_mapping: AttributeRoleMapping = Body(None, description="SAML user attributes to role mapping"),
) -> SAMLObj:
    """Creates a new attribute mapping for a SAML connection"""
    ...


@router.delete(
    "/org/{accountId}/sso-connections/oidc/{connectionId}",
    responses={
        200: {"description": "Deletion successful."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="Delete OIDC connection",
    response_model_by_alias=True,
)
async def delete_oidc_connection(
    accountId: str = Path(None, description=""),
    connectionId: str = Path(None, description=""),
) -> None:
    """Delete an OIDC connection"""
    ...


@router.get(
    "/org/{accountId}/sso-connections/oidc/{connectionId}",
    responses={
        200: {"model": OIDCObj, "description": "OIDCObj"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="Get OIDC connection",
    response_model_by_alias=True,
)
async def get_oidc_connection(
    accountId: str = Path(None, description=""),
    connectionId: str = Path(None, description=""),
) -> OIDCObj:
    """Get details of an OIDC connection"""
    ...


@router.get(
    "/org/{accountId}/sso-connections/oidc",
    responses={
        200: {"model": List[OIDCObj], "description": "OIDC connections belonging to provided account ID"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="List OIDC Connections",
    response_model_by_alias=True,
)
async def get_oidc_connections_for_account(
    accountId: str = Path(None, description=""),
) -> List[OIDCObj]:
    """Returns a list of all OIDC connections belonging to provided organization"""
    ...


@router.get(
    "/org/{accountId}/sso-connections/saml/{connectionId}",
    responses={
        200: {"model": SAMLObj, "description": "SAMLObj"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="Get connection",
    response_model_by_alias=True,
)
async def get_saml_connection(
    accountId: str = Path(None, description=""),
    connectionId: str = Path(None, description=""),
) -> SAMLObj:
    """Retreive a SAML connection"""
    ...


@router.get(
    "/org/{accountId}/sso-connections/saml",
    responses={
        200: {"model": List[SAMLObj], "description": "SAML connections belonging to provided account ID"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="List SAML Connections",
    response_model_by_alias=True,
)
async def get_saml_connections_for_account(
    accountId: str = Path(None, description=""),
) -> List[SAMLObj]:
    """Returns a list of all SAML connections belonging to provided organization"""
    ...


@router.get(
    "/org/{accountId}/sso-connections/oidc/{connectionId}/login-trigger",
    responses={
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="Trigger OIDC SSO",
    response_model_by_alias=True,
)
async def o_idc_login_trigger(
    connectionId: str = Path(None, description=""),
    accountId: str = Path(None, description=""),
) -> Error:
    """Triggers SSO for a particular OIDC connection. This would be initiated by the developer from applicatoon code"""
    ...


@router.get(
    "/org/{accountId}/sso-connections/oidc/{connectionId}/sso-callback",
    responses={
        302: {"description": "Redirect to default page for developer after succesful login."},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="OIDC Callback",
    response_model_by_alias=True,
)
async def oidc_sso_call_back(
    accountId: str = Path(None, description=""),
    connectionId: str = Path(None, description=""),
    code: str = Query(None, description="Authorization code returned by the OIDC provider"),
    state: str = Query(None, description="Authorization code returned by the OIDC provider"),
) -> Error:
    """Handles OIDC login callback"""
    ...


@router.get(
    "/org/{accountId}/sso-connections/saml/{connectionId}/login-trigger",
    responses={
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="Triggers SAML SSO",
    response_model_by_alias=True,
)
async def s_aml_login_trigger(
    connectionId: str = Path(None, description=""),
    accountId: str = Path(None, description=""),
) -> Error:
    """Triggers SAML login for a particular connection. Account can have multiple SAML connections. It redirects to the login URL corresponding to a particular connection."""
    ...


@router.post(
    "/org/{accountId}/sso-connections/saml/{connectionId}/sso-callback/saml/acs",
    responses={
        302: {"description": "Redirect to default page for developer after succesful login."},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="SAML Callback",
    response_model_by_alias=True,
)
async def saml_sso_call_back(
    accountId: str = Path(None, description=""),
    connectionId: str = Path(None, description=""),
    saml_response: str = Query(None, description="SAML response returned by the SAML IDP"),
    saml_response2: str = Form(None, description="SAML response returned by the SAML IDP"),
) -> Error:
    """Handle SAML login callback with SAML assertion. It can be passed as query parameter or payload."""
    ...


@router.put(
    "/org/{accountId}/sso-connections/oidc/{connectionId}",
    responses={
        200: {"model": OIDCObj, "description": "SAMLObj"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="Update OIDC connection",
    response_model_by_alias=True,
)
async def update_oidc_connection(
    accountId: str = Path(None, description=""),
    connectionId: str = Path(None, description=""),
    oidc_obj: OIDCObj = Body(None, description="OIDC connection attributes"),
) -> OIDCObj:
    """Updates a OIDC connection"""
    ...


@router.put(
    "/org/{accountId}/sso-connections/saml/{connectionId}",
    responses={
        200: {"model": SAMLObj, "description": "SAMLObj"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["sso"],
    summary="Update SAML connection",
    response_model_by_alias=True,
)
async def update_saml_connection(
    accountId: str = Path(None, description=""),
    connectionId: str = Path(None, description=""),
    saml_obj: SAMLObj = Body(None, description="SAML connection attributes"),
) -> SAMLObj:
    """Updates a SAML connection"""
    ...
