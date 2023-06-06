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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class InitArcResponse(BaseModel):
    """
    InitArcResponse
    """
    queue_url: Optional[StrictStr] = Field(None, alias="queueUrl")
    key_id: Optional[StrictStr] = Field(None, alias="keyId")
    key_secret: Optional[StrictStr] = Field(None, alias="keySecret")
    session_token: Optional[StrictStr] = Field(None, alias="sessionToken")
    expiration: Optional[StrictInt] = None
    __properties = ["queueUrl", "keyId", "keySecret", "sessionToken", "expiration"]

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
    def from_json(cls, json_str: str) -> InitArcResponse:
        """Create an instance of InitArcResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InitArcResponse:
        """Create an instance of InitArcResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InitArcResponse.parse_obj(obj)

        _obj = InitArcResponse.parse_obj({
            "queue_url": obj.get("queueUrl"),
            "key_id": obj.get("keyId"),
            "key_secret": obj.get("keySecret"),
            "session_token": obj.get("sessionToken"),
            "expiration": obj.get("expiration")
        })
        return _obj

