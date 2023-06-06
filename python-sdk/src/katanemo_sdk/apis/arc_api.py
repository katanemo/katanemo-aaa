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
from katanemo_sdk.models.init_arc_response import InitArcResponse
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.models.role_response import RoleResponse
from katanemo_sdk.models.tags import Tags
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException


router = APIRouter()


@router.get(
    "/arc/{serviceId}/role",
    responses={
        200: {"model": List[RoleResponse], "description": "Successful retrieval of roles for service."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["arc"],
    summary="Get Service Roles",
    response_model_by_alias=True,
)
async def get_roles_for_service(
    serviceId: str = Path(None, description=""),
    limit: int = Query(None, description=""),
) -> List[RoleResponse]:
    ...


@router.get(
    "/arc/{serviceId}/tags",
    responses={
        200: {"model": List[Tags], "description": "Successful retrieval of tags for service."},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["arc"],
    summary="Get Resource Tags",
    response_model_by_alias=True,
)
async def get_tags_for_service(
    serviceId: str = Path(None, description=""),
    limit: int = Query(None, description=""),
) -> List[Tags]:
    """Get all resource tags associated with a Katanemo Service."""
    ...


@router.get(
    "/arc/{serviceId}/init",
    responses={
        200: {"model": List[InitArcResponse], "description": "Successful retrieval of init arc client."},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["arc"],
    summary="Initialize ARC Client",
    response_model_by_alias=True,
)
async def init_arc_client(
    serviceId: str = Path(None, description=""),
) -> List[InitArcResponse]:
    """Initiative the Authorization Runtime Client with Developer API Keys"""
    ...
