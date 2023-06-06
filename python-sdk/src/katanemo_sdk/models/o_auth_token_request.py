# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class OAuthTokenRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    OAuthTokenRequest - a model defined in OpenAPI

        code: The code of this OAuthTokenRequest [Optional].
        client_id: The client_id of this OAuthTokenRequest [Optional].
        client_secret: The client_secret of this OAuthTokenRequest [Optional].
    """

    code: Optional[str] = Field(alias="code", default=None)
    client_id: Optional[str] = Field(alias="clientId", default=None)
    client_secret: Optional[str] = Field(alias="clientSecret", default=None)

OAuthTokenRequest.update_forward_refs()
