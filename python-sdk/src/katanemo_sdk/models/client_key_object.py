# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ClientKeyObject(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ClientKeyObject - a model defined in OpenAPI

        account_id: The account_id of this ClientKeyObject [Optional].
        roles: The roles of this ClientKeyObject [Optional].
        client_name: The client_name of this ClientKeyObject [Optional].
        client_key_id: The client_key_id of this ClientKeyObject [Optional].
        service_id: The service_id of this ClientKeyObject [Optional].
        is_active: The is_active of this ClientKeyObject [Optional].
    """

    account_id: Optional[str] = Field(alias="accountId", default=None)
    roles: Optional[List[str]] = Field(alias="roles", default=None)
    client_name: Optional[str] = Field(alias="clientName", default=None)
    client_key_id: Optional[str] = Field(alias="clientKeyId", default=None)
    service_id: Optional[str] = Field(alias="serviceId", default=None)
    is_active: Optional[bool] = Field(alias="isActive", default=None)

ClientKeyObject.update_forward_refs()
