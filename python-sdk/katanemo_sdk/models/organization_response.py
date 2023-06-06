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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class OrganizationResponse(BaseModel):
    """
    OrganizationResponse
    """
    account_id: StrictStr = Field(..., alias="accountId")
    name: StrictStr = Field(...)
    admin_account: StrictStr = Field(..., alias="adminAccount")
    domain_verification_code: Optional[StrictStr] = Field(None, alias="domainVerificationCode")
    domain: Optional[StrictStr] = None
    domain_verified: Optional[StrictBool] = Field(None, alias="domainVerified")
    users_count: Optional[StrictInt] = Field(None, alias="usersCount")
    roles_count: Optional[StrictInt] = Field(None, alias="rolesCount")
    oidc_connections_count: Optional[StrictInt] = Field(None, alias="oidcConnectionsCount")
    saml_connections_count: Optional[StrictInt] = Field(None, alias="samlConnectionsCount")
    default_connection: Optional[StrictStr] = Field(None, alias="defaultConnection")
    default_connection_type: Optional[StrictStr] = Field(None, alias="defaultConnectionType")
    launched_services: Optional[conlist(StrictStr)] = Field(None, alias="launchedServices")
    subscribed_services: Optional[conlist(StrictStr)] = Field(None, alias="subscribedServices")
    subscribers: Optional[conlist(StrictStr)] = None
    __properties = ["accountId", "name", "adminAccount", "domainVerificationCode", "domain", "domainVerified", "usersCount", "rolesCount", "oidcConnectionsCount", "samlConnectionsCount", "defaultConnection", "defaultConnectionType", "launchedServices", "subscribedServices", "subscribers"]

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
    def from_json(cls, json_str: str) -> OrganizationResponse:
        """Create an instance of OrganizationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationResponse:
        """Create an instance of OrganizationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrganizationResponse.parse_obj(obj)

        _obj = OrganizationResponse.parse_obj({
            "account_id": obj.get("accountId"),
            "name": obj.get("name"),
            "admin_account": obj.get("adminAccount"),
            "domain_verification_code": obj.get("domainVerificationCode"),
            "domain": obj.get("domain"),
            "domain_verified": obj.get("domainVerified"),
            "users_count": obj.get("usersCount"),
            "roles_count": obj.get("rolesCount"),
            "oidc_connections_count": obj.get("oidcConnectionsCount"),
            "saml_connections_count": obj.get("samlConnectionsCount"),
            "default_connection": obj.get("defaultConnection"),
            "default_connection_type": obj.get("defaultConnectionType"),
            "launched_services": obj.get("launchedServices"),
            "subscribed_services": obj.get("subscribedServices"),
            "subscribers": obj.get("subscribers")
        })
        return _obj
