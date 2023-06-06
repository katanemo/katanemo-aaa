# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from katanemo_sdk.models.policy import Policy


class RoleRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RoleRequest - a model defined in OpenAPI

        account_id: The account_id of this RoleRequest [Optional].
        rolename: The rolename of this RoleRequest [Optional].
        description: The description of this RoleRequest [Optional].
        service_id: The service_id of this RoleRequest [Optional].
        policy: The policy of this RoleRequest [Optional].
    """

    account_id: Optional[str] = Field(alias="accountId", default=None)
    rolename: Optional[str] = Field(alias="rolename", default=None)
    description: Optional[str] = Field(alias="description", default=None)
    service_id: Optional[str] = Field(alias="serviceId", default=None)
    policy: Optional[Policy] = Field(alias="policy", default=None)

RoleRequest.update_forward_refs()
