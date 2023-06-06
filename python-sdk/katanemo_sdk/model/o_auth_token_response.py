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


class OAuthTokenResponse(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            idToken = schemas.StrSchema
            accessToken = schemas.StrSchema
            expiresIn = schemas.IntSchema
            tokenType = schemas.StrSchema
            __annotations__ = {
                "idToken": idToken,
                "accessToken": accessToken,
                "expiresIn": expiresIn,
                "tokenType": tokenType,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idToken"]) -> MetaOapg.properties.idToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessToken"]) -> MetaOapg.properties.accessToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiresIn"]) -> MetaOapg.properties.expiresIn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokenType"]) -> MetaOapg.properties.tokenType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["idToken", "accessToken", "expiresIn", "tokenType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idToken"]) -> typing.Union[MetaOapg.properties.idToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessToken"]) -> typing.Union[MetaOapg.properties.accessToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiresIn"]) -> typing.Union[MetaOapg.properties.expiresIn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokenType"]) -> typing.Union[MetaOapg.properties.tokenType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["idToken", "accessToken", "expiresIn", "tokenType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        idToken: typing.Union[MetaOapg.properties.idToken, str, schemas.Unset] = schemas.unset,
        accessToken: typing.Union[MetaOapg.properties.accessToken, str, schemas.Unset] = schemas.unset,
        expiresIn: typing.Union[MetaOapg.properties.expiresIn, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tokenType: typing.Union[MetaOapg.properties.tokenType, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OAuthTokenResponse':
        return super().__new__(
            cls,
            *_args,
            idToken=idToken,
            accessToken=accessToken,
            expiresIn=expiresIn,
            tokenType=tokenType,
            _configuration=_configuration,
            **kwargs,
        )
