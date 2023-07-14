# coding: utf-8

"""
    Katanemo - identity, and fine-grained authorization for modern { API-first } software companies.

    With Katanemo developers can add support for users, enterprise SSO, machine keys and fine-grained authorization in minutes.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@katanemo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class LoginWithPasswordRequest(BaseModel):
    """
    LoginWithPasswordRequest
    """
    email_address: StrictStr = Field(..., alias="emailAddress", description="Email address of the developer account's user")
    password: StrictStr = Field(..., description="Password of the user")
    skip_redirect: Optional[StrictBool] = Field(None, alias="skipRedirect", description="By default login will redirect to service redirect URL, if this parameter is set as true then response will be returned.")
    state: Optional[StrictStr] = Field(None, description="Optional state parameter.")
    __properties = ["emailAddress", "password", "skipRedirect", "state"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> LoginWithPasswordRequest:
        """Create an instance of LoginWithPasswordRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoginWithPasswordRequest:
        """Create an instance of LoginWithPasswordRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoginWithPasswordRequest.parse_obj(obj)

        _obj = LoginWithPasswordRequest.parse_obj({
            "email_address": obj.get("emailAddress"),
            "password": obj.get("password"),
            "skip_redirect": obj.get("skipRedirect"),
            "state": obj.get("state")
        })
        return _obj
