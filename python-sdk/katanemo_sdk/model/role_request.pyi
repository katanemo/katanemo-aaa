# coding: utf-8

"""
    Katanemo - identity, and fine-grained authorization for modern { API-first } software companies.

    With Katanemo developers can add support for users, enterprise SSO, machine keys and fine-grained authorization in minutes.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@katanemo.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from katanemo_sdk import schemas  # noqa: F401


class RoleRequest(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            accountId = schemas.StrSchema
            rolename = schemas.StrSchema
            description = schemas.StrSchema
            serviceId = schemas.StrSchema
        
            @staticmethod
            def policy() -> typing.Type['Policy']:
                return Policy
            __annotations__ = {
                "accountId": accountId,
                "rolename": rolename,
                "description": description,
                "serviceId": serviceId,
                "policy": policy,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rolename"]) -> MetaOapg.properties.rolename: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceId"]) -> MetaOapg.properties.serviceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policy"]) -> 'Policy': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountId", "rolename", "description", "serviceId", "policy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> typing.Union[MetaOapg.properties.accountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rolename"]) -> typing.Union[MetaOapg.properties.rolename, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceId"]) -> typing.Union[MetaOapg.properties.serviceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policy"]) -> typing.Union['Policy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountId", "rolename", "description", "serviceId", "policy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        accountId: typing.Union[MetaOapg.properties.accountId, str, schemas.Unset] = schemas.unset,
        rolename: typing.Union[MetaOapg.properties.rolename, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        serviceId: typing.Union[MetaOapg.properties.serviceId, str, schemas.Unset] = schemas.unset,
        policy: typing.Union['Policy', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RoleRequest':
        return super().__new__(
            cls,
            *_args,
            accountId=accountId,
            rolename=rolename,
            description=description,
            serviceId=serviceId,
            policy=policy,
            _configuration=_configuration,
            **kwargs,
        )

from katanemo_sdk.model.policy import Policy
