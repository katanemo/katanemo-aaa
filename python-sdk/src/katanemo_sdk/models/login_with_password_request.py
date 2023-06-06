# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class LoginWithPasswordRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LoginWithPasswordRequest - a model defined in OpenAPI

        email_address: The email_address of this LoginWithPasswordRequest.
        password: The password of this LoginWithPasswordRequest.
        skip_redirect: The skip_redirect of this LoginWithPasswordRequest [Optional].
        state: The state of this LoginWithPasswordRequest [Optional].
    """

    email_address: str = Field(alias="emailAddress")
    password: str = Field(alias="password")
    skip_redirect: Optional[bool] = Field(alias="skipRedirect", default=None)
    state: Optional[str] = Field(alias="state", default=None)

LoginWithPasswordRequest.update_forward_refs()
