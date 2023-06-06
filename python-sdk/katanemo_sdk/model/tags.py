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


class Tags(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "resourceId",
            "name",
            "serviceId",
            "tags",
            "token",
        }
        
        class properties:
            serviceId = schemas.StrSchema
            name = schemas.StrSchema
            resourceId = schemas.StrSchema
            token = schemas.StrSchema
            
            
            class tags(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            serviceIdPath = schemas.StrSchema
            accountId = schemas.StrSchema
            __annotations__ = {
                "serviceId": serviceId,
                "name": name,
                "resourceId": resourceId,
                "token": token,
                "tags": tags,
                "serviceIdPath": serviceIdPath,
                "accountId": accountId,
            }

    
    resourceId: MetaOapg.properties.resourceId
    name: MetaOapg.properties.name
    serviceId: MetaOapg.properties.serviceId
    tags: MetaOapg.properties.tags
    token: MetaOapg.properties.token
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceId"]) -> MetaOapg.properties.serviceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceId"]) -> MetaOapg.properties.resourceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceIdPath"]) -> MetaOapg.properties.serviceIdPath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["serviceId", "name", "resourceId", "token", "tags", "serviceIdPath", "accountId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceId"]) -> MetaOapg.properties.serviceId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceId"]) -> MetaOapg.properties.resourceId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceIdPath"]) -> typing.Union[MetaOapg.properties.serviceIdPath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> typing.Union[MetaOapg.properties.accountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["serviceId", "name", "resourceId", "token", "tags", "serviceIdPath", "accountId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        resourceId: typing.Union[MetaOapg.properties.resourceId, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        serviceId: typing.Union[MetaOapg.properties.serviceId, str, ],
        tags: typing.Union[MetaOapg.properties.tags, dict, frozendict.frozendict, ],
        token: typing.Union[MetaOapg.properties.token, str, ],
        serviceIdPath: typing.Union[MetaOapg.properties.serviceIdPath, str, schemas.Unset] = schemas.unset,
        accountId: typing.Union[MetaOapg.properties.accountId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Tags':
        return super().__new__(
            cls,
            *_args,
            resourceId=resourceId,
            name=name,
            serviceId=serviceId,
            tags=tags,
            token=token,
            serviceIdPath=serviceIdPath,
            accountId=accountId,
            _configuration=_configuration,
            **kwargs,
        )
