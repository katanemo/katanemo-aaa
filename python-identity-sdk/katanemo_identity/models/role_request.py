# coding: utf-8

"""
    Katanemo - identity, and fine-grained authorization for modern { API-first } software companies.

    With Katanemo developers can add support for users, enterprise SSO, machine keys and fine-grained authorization in minutes.  # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Contact: support@katanemo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from katanemo_identity.models.policy import Policy

class RoleRequest(BaseModel):
    """
    RoleRequest
    """
    account_id: Optional[StrictStr] = Field(None, alias="accountId", description="AccountId")
    rolename: Optional[StrictStr] = Field(None, description="Role name")
    description: Optional[StrictStr] = Field(None, description="Role description")
    service_id: Optional[StrictStr] = Field(None, alias="serviceId", description="ID of the service")
    policy: Optional[Policy] = None
    __properties = ["accountId", "rolename", "description", "serviceId", "policy"]

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
    def from_json(cls, json_str: str) -> RoleRequest:
        """Create an instance of RoleRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of policy
        if self.policy:
            _dict['policy'] = self.policy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoleRequest:
        """Create an instance of RoleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoleRequest.parse_obj(obj)

        _obj = RoleRequest.parse_obj({
            "account_id": obj.get("accountId"),
            "rolename": obj.get("rolename"),
            "description": obj.get("description"),
            "service_id": obj.get("serviceId"),
            "policy": Policy.from_dict(obj.get("policy")) if obj.get("policy") is not None else None
        })
        return _obj

