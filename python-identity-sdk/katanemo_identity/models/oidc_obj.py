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

class OIDCObj(BaseModel):
    """
    OIDCObj
    """
    oidc_config_endpoint: StrictStr = Field(..., alias="oidcConfigEndpoint", description="OIDC configuration URL")
    redirect_url: Optional[StrictStr] = Field(None, alias="redirectURL", description="Callback URL for OIDC IdP")
    name: Optional[StrictStr] = Field(None, description="Name of the OIDC connection")
    client_id: StrictStr = Field(..., alias="clientId")
    client_secret: StrictStr = Field(..., alias="clientSecret")
    nonce: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    account_id: Optional[StrictStr] = Field(None, alias="accountId")
    service_id: Optional[StrictStr] = Field(None, alias="serviceId")
    authorization_endpoint: Optional[StrictStr] = Field(None, alias="authorizationEndpoint")
    token_endpoint: Optional[StrictStr] = Field(None, alias="tokenEndpoint")
    user_info_endpoint: Optional[StrictStr] = Field(None, alias="userInfoEndpoint")
    issuer_endpoint: Optional[StrictStr] = Field(None, alias="issuerEndpoint")
    jwks_endpoint: Optional[StrictStr] = Field(None, alias="jwksEndpoint")
    connection_id: Optional[StrictStr] = Field(None, alias="connectionId")
    __properties = ["oidcConfigEndpoint", "redirectURL", "name", "clientId", "clientSecret", "nonce", "state", "accountId", "serviceId", "authorizationEndpoint", "tokenEndpoint", "userInfoEndpoint", "issuerEndpoint", "jwksEndpoint", "connectionId"]

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
    def from_json(cls, json_str: str) -> OIDCObj:
        """Create an instance of OIDCObj from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OIDCObj:
        """Create an instance of OIDCObj from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OIDCObj.parse_obj(obj)

        _obj = OIDCObj.parse_obj({
            "oidc_config_endpoint": obj.get("oidcConfigEndpoint"),
            "redirect_url": obj.get("redirectURL"),
            "name": obj.get("name"),
            "client_id": obj.get("clientId"),
            "client_secret": obj.get("clientSecret"),
            "nonce": obj.get("nonce"),
            "state": obj.get("state"),
            "account_id": obj.get("accountId"),
            "service_id": obj.get("serviceId"),
            "authorization_endpoint": obj.get("authorizationEndpoint"),
            "token_endpoint": obj.get("tokenEndpoint"),
            "user_info_endpoint": obj.get("userInfoEndpoint"),
            "issuer_endpoint": obj.get("issuerEndpoint"),
            "jwks_endpoint": obj.get("jwksEndpoint"),
            "connection_id": obj.get("connectionId")
        })
        return _obj

