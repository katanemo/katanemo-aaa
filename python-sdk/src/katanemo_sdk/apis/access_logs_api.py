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
from katanemo_sdk.models.audit_log_entry import AuditLogEntry
from katanemo_sdk.models.bad_request_exception import BadRequestException
from katanemo_sdk.models.conflict_exception import ConflictException
from katanemo_sdk.models.error import Error
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException


router = APIRouter()


@router.get(
    "/audit-logs/service/{serviceId}/account/{accountId}",
    responses={
        200: {"model": List[AuditLogEntry], "description": "List of log entries"},
        400: {"model": BadRequestException, "description": "Bad Request Exception"},
        401: {"model": UnauthorizedException, "description": "Unauthorized Exception"},
        409: {"model": ConflictException, "description": "Conflict Exception"},
        429: {"model": TooManyRequestsException, "description": "Too Many Requests Exception"},
        500: {"model": InternalServerErrorException, "description": "Internal Server Error"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["access-logs"],
    summary="List Access logs",
    response_model_by_alias=True,
)
async def get_audit_logs(
    serviceId: str = Path(None, description=""),
    accountId: str = Path(None, description=""),
    start_time: str = Query(None, description="Start time of log entries in the format YYYY-MM-DDThh-mm-ss (e.g. 2023-01-15T15-28-58 which means 2023-01-15 15:28:58)"),
    end_time: str = Query(None, description="End time of log entries in the format YYYY-MM-DDThh-mm-ss (e.g. 2023-01-15T15-28-58 which means 2023-01-15 15:28:58)"),
) -> List[AuditLogEntry]:
    """Return a list of access logs that belong to a particular service and orgaization"""
    ...
