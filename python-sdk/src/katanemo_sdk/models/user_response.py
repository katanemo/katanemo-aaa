# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class UserResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UserResponse - a model defined in OpenAPI

        account_id: The account_id of this UserResponse.
        service_id: The service_id of this UserResponse [Optional].
        user_id: The user_id of this UserResponse [Optional].
        is_admin: The is_admin of this UserResponse [Optional].
        is_active: The is_active of this UserResponse [Optional].
        token: The token of this UserResponse [Optional].
        tags: The tags of this UserResponse [Optional].
        roles: The roles of this UserResponse [Optional].
    """

    account_id: str = Field(alias="accountId")
    service_id: Optional[str] = Field(alias="serviceId", default=None)
    user_id: Optional[str] = Field(alias="userId", default=None)
    is_admin: Optional[bool] = Field(alias="isAdmin", default=None)
    is_active: Optional[bool] = Field(alias="isActive", default=None)
    token: Optional[str] = Field(alias="token", default=None)
    tags: Optional[Dict[str, List[str]]] = Field(alias="tags", default=None)
    roles: Optional[List[str]] = Field(alias="roles", default=None)

UserResponse.update_forward_refs()
