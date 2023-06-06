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


router = APIRouter()


@router.get(
    "/healthz",
    responses={
        200: {"model": str, "description": "token"},
    },
    tags=["health"],
    summary="Return Katanemo Health",
    response_model_by_alias=True,
)
async def get_healthz(
) -> str:
    """This API returns the current health of the Katanemo Contorl Plane and Data Plane services."""
    ...
