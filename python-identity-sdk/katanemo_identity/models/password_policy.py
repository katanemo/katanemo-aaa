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



from pydantic import BaseModel, Field, StrictBool, StrictInt

class PasswordPolicy(BaseModel):
    """
    PasswordPolicy
    """
    minimum_legnth: StrictInt = Field(..., alias="minimumLegnth", description="The minimum length of the password in the policy that you have set. This value can't be less than 6.")
    required_numbers: StrictBool = Field(..., alias="requiredNumbers", description="In the password policy that you have set, refers to whether you have required users to use at least one number in their password.")
    require_symbols: StrictBool = Field(..., alias="requireSymbols", description="In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.")
    require_upper_case: StrictBool = Field(..., alias="requireUpperCase", description="In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.")
    require_lower_case: StrictBool = Field(..., alias="requireLowerCase", description="In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.")
    __properties = ["minimumLegnth", "requiredNumbers", "requireSymbols", "requireUpperCase", "requireLowerCase"]

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
    def from_json(cls, json_str: str) -> PasswordPolicy:
        """Create an instance of PasswordPolicy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PasswordPolicy:
        """Create an instance of PasswordPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PasswordPolicy.parse_obj(obj)

        _obj = PasswordPolicy.parse_obj({
            "minimum_legnth": obj.get("minimumLegnth"),
            "required_numbers": obj.get("requiredNumbers"),
            "require_symbols": obj.get("requireSymbols"),
            "require_upper_case": obj.get("requireUpperCase"),
            "require_lower_case": obj.get("requireLowerCase")
        })
        return _obj

