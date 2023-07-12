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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from katanemo_identity.models.attribute_role_mapping import AttributeRoleMapping

class SAMLObj(BaseModel):
    """
    SAMLObj
    """
    connection_id: Optional[StrictStr] = Field(None, alias="connectionId")
    id_provider: StrictStr = Field(..., alias="idProvider")
    state: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    default_role_id: StrictStr = Field(..., alias="defaultRoleId")
    login_link: Optional[StrictStr] = Field(None, alias="loginLink")
    metadata_link: Optional[StrictStr] = Field(None, alias="metadataLink")
    acs_link: Optional[StrictStr] = Field(None, alias="acsLink")
    audience_link: Optional[StrictStr] = Field(None, alias="audienceLink")
    attribute_role_mappings: Optional[conlist(AttributeRoleMapping)] = Field(None, alias="attributeRoleMappings")
    root_url: Optional[StrictStr] = Field(None, alias="rootURL")
    account_id: StrictStr = Field(..., alias="accountId")
    service_id: StrictStr = Field(..., alias="serviceId")
    __properties = ["connectionId", "idProvider", "state", "name", "defaultRoleId", "loginLink", "metadataLink", "acsLink", "audienceLink", "attributeRoleMappings", "rootURL", "accountId", "serviceId"]

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
    def from_json(cls, json_str: str) -> SAMLObj:
        """Create an instance of SAMLObj from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in attribute_role_mappings (list)
        _items = []
        if self.attribute_role_mappings:
            for _item in self.attribute_role_mappings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributeRoleMappings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SAMLObj:
        """Create an instance of SAMLObj from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SAMLObj.parse_obj(obj)

        _obj = SAMLObj.parse_obj({
            "connection_id": obj.get("connectionId"),
            "id_provider": obj.get("idProvider"),
            "state": obj.get("state"),
            "name": obj.get("name"),
            "default_role_id": obj.get("defaultRoleId"),
            "login_link": obj.get("loginLink"),
            "metadata_link": obj.get("metadataLink"),
            "acs_link": obj.get("acsLink"),
            "audience_link": obj.get("audienceLink"),
            "attribute_role_mappings": [AttributeRoleMapping.from_dict(_item) for _item in obj.get("attributeRoleMappings")] if obj.get("attributeRoleMappings") is not None else None,
            "root_url": obj.get("rootURL"),
            "account_id": obj.get("accountId"),
            "service_id": obj.get("serviceId")
        })
        return _obj

