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
from pydantic import BaseModel, Field, StrictStr

class OIDCPublicKey(BaseModel):
    """
    OIDCPublicKey
    """
    kid: Optional[StrictStr] = Field(None, description="key id")
    alg: Optional[StrictStr] = Field(None, description="Key algorithm")
    e: Optional[StrictStr] = Field(None, description="RSA exponent")
    n: Optional[StrictStr] = Field(None, description="RSA modulus")
    use: Optional[StrictStr] = Field(None, description="key usage")
    kty: Optional[StrictStr] = Field(None, description="key type")
    __properties = ["kid", "alg", "e", "n", "use", "kty"]

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
    def from_json(cls, json_str: str) -> OIDCPublicKey:
        """Create an instance of OIDCPublicKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OIDCPublicKey:
        """Create an instance of OIDCPublicKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OIDCPublicKey.parse_obj(obj)

        _obj = OIDCPublicKey.parse_obj({
            "kid": obj.get("kid"),
            "alg": obj.get("alg"),
            "e": obj.get("e"),
            "n": obj.get("n"),
            "use": obj.get("use"),
            "kty": obj.get("kty")
        })
        return _obj

