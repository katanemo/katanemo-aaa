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
from katanemo_sdk.models.authorize_request import AuthorizeRequest
from katanemo_sdk.models.bad_request_exception import BadRequestException


router = APIRouter()


@router.get(
    "/authorize",
    responses={
        302: {"description": "Redirect to Katanemo&#39;s signin page"},
    },
    tags=["default"],
    summary="Initiate the login flow by redirecting to login page",
    response_model_by_alias=True,
)
async def authorize(
    authorize_request: AuthorizeRequest = Body(None, description="parameters requiired to determine where to take the user"),
) -> None:
    """Determine where to take a user for login"""
    ...


@router.post(
    "/arc/authorize",
    responses={
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
    },
    tags=["default"],
    summary="dummy endpoint for authorize",
    response_model_by_alias=True,
)
async def post_authorize(
) -> None:
    ...
