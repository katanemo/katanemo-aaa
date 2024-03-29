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



from pydantic import BaseModel, Field, StrictStr

class UserConfirmationResponse(BaseModel):
    """
    UserConfirmationResponse
    """
    session: StrictStr = Field(..., description="Session info in response to confirm user. This session can be used to set password.")
    account_id: StrictStr = Field(..., alias="accountId", description="returns the account id for the organization that subscribed to the service.")
    email_address: StrictStr = Field(..., alias="emailAddress", description="returns the email address of the user signing up.")
    service_id: StrictStr = Field(..., alias="serviceId", description="returns the service id for which user subscribed to.")
    __properties = ["session", "accountId", "emailAddress", "serviceId"]

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
    def from_json(cls, json_str: str) -> UserConfirmationResponse:
        """Create an instance of UserConfirmationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserConfirmationResponse:
        """Create an instance of UserConfirmationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserConfirmationResponse.parse_obj(obj)

        _obj = UserConfirmationResponse.parse_obj({
            "session": obj.get("session"),
            "account_id": obj.get("accountId"),
            "email_address": obj.get("emailAddress"),
            "service_id": obj.get("serviceId")
        })
        return _obj

