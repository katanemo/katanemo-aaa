<a id="__pageTop"></a>
# katanemo_sdk.apis.tags.sso_api.SsoApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_oidcc_onnection**](#create_oidcc_onnection) | **post** /org/{accountId}/sso-connections/oidc | Creates OIDC connection
[**create_saml_connection**](#create_saml_connection) | **post** /org/{accountId}/sso-connections/saml | Creates SAML connection
[**create_saml_connection_mapping**](#create_saml_connection_mapping) | **post** /org/{accountId}/sso-connections/saml/{connectionId}/mapAttributeToRoles | MAP SAML Attributes
[**delete_oidc_connection**](#delete_oidc_connection) | **delete** /org/{accountId}/sso-connections/oidc/{connectionId} | Delete OIDC connection
[**get_oidc_connection**](#get_oidc_connection) | **get** /org/{accountId}/sso-connections/oidc/{connectionId} | Get OIDC connection
[**get_oidc_connections_for_account**](#get_oidc_connections_for_account) | **get** /org/{accountId}/sso-connections/oidc | List OIDC Connections
[**get_saml_connection**](#get_saml_connection) | **get** /org/{accountId}/sso-connections/saml/{connectionId} | Get connection
[**get_saml_connections_for_account**](#get_saml_connections_for_account) | **get** /org/{accountId}/sso-connections/saml | List SAML Connections
[**o_idc_login_trigger**](#o_idc_login_trigger) | **get** /org/{accountId}/sso-connections/oidc/{connectionId}/login-trigger | Trigger OIDC SSO
[**oidc_sso_call_back**](#oidc_sso_call_back) | **get** /org/{accountId}/sso-connections/oidc/{connectionId}/sso-callback | OIDC Callback
[**s_aml_login_trigger**](#s_aml_login_trigger) | **get** /org/{accountId}/sso-connections/saml/{connectionId}/login-trigger | Triggers SAML SSO
[**saml_sso_call_back**](#saml_sso_call_back) | **post** /org/{accountId}/sso-connections/saml/{connectionId}/sso-callback/saml/acs | SAML Callback
[**update_oidc_connection**](#update_oidc_connection) | **put** /org/{accountId}/sso-connections/oidc/{connectionId} | Update OIDC connection
[**update_saml_connection**](#update_saml_connection) | **put** /org/{accountId}/sso-connections/saml/{connectionId} | Update SAML connection

# **create_oidcc_onnection**
<a id="create_oidcc_onnection"></a>
> OIDCObj create_oidcc_onnection(account_idoidc_obj)

Creates OIDC connection

Creates a new OIDC connection

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.model.oidc_obj import OIDCObj
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    body = OIDCObj(None)
    try:
        # Creates OIDC connection
        api_response = api_instance.create_oidcc_onnection(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->create_oidcc_onnection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OIDCObj**](../../models/OIDCObj.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_oidcc_onnection.ApiResponseFor200) | OIDCObj
400 | [ApiResponseFor400](#create_oidcc_onnection.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#create_oidcc_onnection.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#create_oidcc_onnection.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#create_oidcc_onnection.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#create_oidcc_onnection.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#create_oidcc_onnection.ApiResponseForDefault) | unexpected error

#### create_oidcc_onnection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OIDCObj**](../../models/OIDCObj.md) |  | 


#### create_oidcc_onnection.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### create_oidcc_onnection.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### create_oidcc_onnection.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### create_oidcc_onnection.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### create_oidcc_onnection.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### create_oidcc_onnection.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_saml_connection**
<a id="create_saml_connection"></a>
> SAMLObj create_saml_connection(account_idsaml_obj)

Creates SAML connection

Creates a new SAML connection

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.saml_obj import SAMLObj
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    body = SAMLObj(None)
    try:
        # Creates SAML connection
        api_response = api_instance.create_saml_connection(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->create_saml_connection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SAMLObj**](../../models/SAMLObj.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_saml_connection.ApiResponseFor200) | SAMLObj
400 | [ApiResponseFor400](#create_saml_connection.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#create_saml_connection.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#create_saml_connection.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#create_saml_connection.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#create_saml_connection.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#create_saml_connection.ApiResponseForDefault) | unexpected error

#### create_saml_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SAMLObj**](../../models/SAMLObj.md) |  | 


#### create_saml_connection.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### create_saml_connection.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### create_saml_connection.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### create_saml_connection.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### create_saml_connection.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### create_saml_connection.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_saml_connection_mapping**
<a id="create_saml_connection_mapping"></a>
> SAMLObj create_saml_connection_mapping(account_idconnection_idattribute_role_mapping)

MAP SAML Attributes

Creates a new attribute mapping for a SAML connection

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.saml_obj import SAMLObj
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.attribute_role_mapping import AttributeRoleMapping
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'connectionId': "connectionId_example",
    }
    body = AttributeRoleMapping(None)
    try:
        # MAP SAML Attributes
        api_response = api_instance.create_saml_connection_mapping(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->create_saml_connection_mapping: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AttributeRoleMapping**](../../models/AttributeRoleMapping.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 
connectionId | ConnectionIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_saml_connection_mapping.ApiResponseFor200) | SAMLObj
400 | [ApiResponseFor400](#create_saml_connection_mapping.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#create_saml_connection_mapping.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#create_saml_connection_mapping.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#create_saml_connection_mapping.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#create_saml_connection_mapping.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#create_saml_connection_mapping.ApiResponseForDefault) | unexpected error

#### create_saml_connection_mapping.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SAMLObj**](../../models/SAMLObj.md) |  | 


#### create_saml_connection_mapping.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### create_saml_connection_mapping.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### create_saml_connection_mapping.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### create_saml_connection_mapping.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### create_saml_connection_mapping.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### create_saml_connection_mapping.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_oidc_connection**
<a id="delete_oidc_connection"></a>
> delete_oidc_connection(account_idconnection_id)

Delete OIDC connection

Delete an OIDC connection

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'connectionId': "connectionId_example",
    }
    try:
        # Delete OIDC connection
        api_response = api_instance.delete_oidc_connection(
            path_params=path_params,
        )
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->delete_oidc_connection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 
connectionId | ConnectionIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_oidc_connection.ApiResponseFor200) | Deletion successful.
400 | [ApiResponseFor400](#delete_oidc_connection.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#delete_oidc_connection.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#delete_oidc_connection.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#delete_oidc_connection.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#delete_oidc_connection.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#delete_oidc_connection.ApiResponseForDefault) | unexpected error

#### delete_oidc_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_oidc_connection.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### delete_oidc_connection.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### delete_oidc_connection.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### delete_oidc_connection.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### delete_oidc_connection.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### delete_oidc_connection.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_oidc_connection**
<a id="get_oidc_connection"></a>
> OIDCObj get_oidc_connection(account_idconnection_id)

Get OIDC connection

Get details of an OIDC connection

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.model.oidc_obj import OIDCObj
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'connectionId': "connectionId_example",
    }
    try:
        # Get OIDC connection
        api_response = api_instance.get_oidc_connection(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->get_oidc_connection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 
connectionId | ConnectionIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_oidc_connection.ApiResponseFor200) | OIDCObj
400 | [ApiResponseFor400](#get_oidc_connection.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_oidc_connection.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_oidc_connection.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_oidc_connection.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_oidc_connection.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_oidc_connection.ApiResponseForDefault) | unexpected error

#### get_oidc_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OIDCObj**](../../models/OIDCObj.md) |  | 


#### get_oidc_connection.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_oidc_connection.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_oidc_connection.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_oidc_connection.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_oidc_connection.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_oidc_connection.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_oidc_connections_for_account**
<a id="get_oidc_connections_for_account"></a>
> [OIDCObj] get_oidc_connections_for_account(account_id)

List OIDC Connections

Returns a list of all OIDC connections belonging to provided organization

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.model.oidc_obj import OIDCObj
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    try:
        # List OIDC Connections
        api_response = api_instance.get_oidc_connections_for_account(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->get_oidc_connections_for_account: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_oidc_connections_for_account.ApiResponseFor200) | OIDC connections belonging to provided account ID
400 | [ApiResponseFor400](#get_oidc_connections_for_account.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_oidc_connections_for_account.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_oidc_connections_for_account.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_oidc_connections_for_account.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_oidc_connections_for_account.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_oidc_connections_for_account.ApiResponseForDefault) | unexpected error

#### get_oidc_connections_for_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OIDCObj**]({{complexTypePrefix}}OIDCObj.md) | [**OIDCObj**]({{complexTypePrefix}}OIDCObj.md) | [**OIDCObj**]({{complexTypePrefix}}OIDCObj.md) |  | 

#### get_oidc_connections_for_account.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_oidc_connections_for_account.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_oidc_connections_for_account.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_oidc_connections_for_account.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_oidc_connections_for_account.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_oidc_connections_for_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_saml_connection**
<a id="get_saml_connection"></a>
> SAMLObj get_saml_connection(account_idconnection_id)

Get connection

Retreive a SAML connection

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.saml_obj import SAMLObj
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'connectionId': "connectionId_example",
    }
    try:
        # Get connection
        api_response = api_instance.get_saml_connection(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->get_saml_connection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 
connectionId | ConnectionIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_saml_connection.ApiResponseFor200) | SAMLObj
400 | [ApiResponseFor400](#get_saml_connection.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_saml_connection.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_saml_connection.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_saml_connection.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_saml_connection.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_saml_connection.ApiResponseForDefault) | unexpected error

#### get_saml_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SAMLObj**](../../models/SAMLObj.md) |  | 


#### get_saml_connection.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_saml_connection.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_saml_connection.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_saml_connection.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_saml_connection.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_saml_connection.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_saml_connections_for_account**
<a id="get_saml_connections_for_account"></a>
> [SAMLObj] get_saml_connections_for_account(account_id)

List SAML Connections

Returns a list of all SAML connections belonging to provided organization

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.saml_obj import SAMLObj
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    try:
        # List SAML Connections
        api_response = api_instance.get_saml_connections_for_account(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->get_saml_connections_for_account: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_saml_connections_for_account.ApiResponseFor200) | SAML connections belonging to provided account ID
400 | [ApiResponseFor400](#get_saml_connections_for_account.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_saml_connections_for_account.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_saml_connections_for_account.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_saml_connections_for_account.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_saml_connections_for_account.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_saml_connections_for_account.ApiResponseForDefault) | unexpected error

#### get_saml_connections_for_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SAMLObj**]({{complexTypePrefix}}SAMLObj.md) | [**SAMLObj**]({{complexTypePrefix}}SAMLObj.md) | [**SAMLObj**]({{complexTypePrefix}}SAMLObj.md) |  | 

#### get_saml_connections_for_account.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_saml_connections_for_account.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_saml_connections_for_account.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_saml_connections_for_account.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_saml_connections_for_account.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_saml_connections_for_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **o_idc_login_trigger**
<a id="o_idc_login_trigger"></a>
> Error o_idc_login_trigger(connection_idaccount_id)

Trigger OIDC SSO

Triggers SSO for a particular OIDC connection. This would be initiated by the developer from applicatoon code

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connectionId': "connectionId_example",
        'accountId': "accountId_example",
    }
    try:
        # Trigger OIDC SSO
        api_response = api_instance.o_idc_login_trigger(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->o_idc_login_trigger: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
connectionId | ConnectionIdSchema | | 
accountId | AccountIdSchema | | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#o_idc_login_trigger.ApiResponseForDefault) | unexpected error

#### o_idc_login_trigger.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **oidc_sso_call_back**
<a id="oidc_sso_call_back"></a>
> Error oidc_sso_call_back(account_idconnection_idcodestate)

OIDC Callback

Handles OIDC login callback

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'connectionId': "connectionId_example",
    }
    query_params = {
        'code': "code_example",
        'state': "state_example",
    }
    try:
        # OIDC Callback
        api_response = api_instance.oidc_sso_call_back(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->oidc_sso_call_back: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
code | CodeSchema | | 
state | StateSchema | | 


# CodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 
connectionId | ConnectionIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
302 | [ApiResponseFor302](#oidc_sso_call_back.ApiResponseFor302) | Redirect to default page for developer after succesful login.
default | [ApiResponseForDefault](#oidc_sso_call_back.ApiResponseForDefault) | unexpected error

#### oidc_sso_call_back.ApiResponseFor302
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor302 |  |
#### ResponseHeadersFor302

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Location | LocationSchema | | optional

# LocationSchema

Redirect URL of landing page after successful login.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Redirect URL of landing page after successful login. | 


#### oidc_sso_call_back.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **s_aml_login_trigger**
<a id="s_aml_login_trigger"></a>
> Error s_aml_login_trigger(connection_idaccount_id)

Triggers SAML SSO

Triggers SAML login for a particular connection. Account can have multiple SAML connections. It redirects to the login URL corresponding to a particular connection.

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connectionId': "connectionId_example",
        'accountId': "accountId_example",
    }
    try:
        # Triggers SAML SSO
        api_response = api_instance.s_aml_login_trigger(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->s_aml_login_trigger: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
connectionId | ConnectionIdSchema | | 
accountId | AccountIdSchema | | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#s_aml_login_trigger.ApiResponseForDefault) | unexpected error

#### s_aml_login_trigger.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **saml_sso_call_back**
<a id="saml_sso_call_back"></a>
> Error saml_sso_call_back(account_idconnection_id)

SAML Callback

Handle SAML login callback with SAML assertion. It can be passed as query parameter or payload.

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'connectionId': "connectionId_example",
    }
    query_params = {
    }
    try:
        # SAML Callback
        api_response = api_instance.saml_sso_call_back(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->saml_sso_call_back: %s\n" % e)

    # example passing only optional values
    path_params = {
        'accountId': "accountId_example",
        'connectionId': "connectionId_example",
    }
    query_params = {
        'SAMLResponse': "SAMLResponse_example",
    }
    body = dict(
        saml_response="saml_response_example",
    )
    try:
        # SAML Callback
        api_response = api_instance.saml_sso_call_back(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->saml_sso_call_back: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**SAMLResponse** | str,  | str,  | SAML response returned by the SAML IDP | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
SAMLResponse | SAMLResponseSchema | | optional


# SAMLResponseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 
connectionId | ConnectionIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
302 | [ApiResponseFor302](#saml_sso_call_back.ApiResponseFor302) | Redirect to default page for developer after succesful login.
default | [ApiResponseForDefault](#saml_sso_call_back.ApiResponseForDefault) | unexpected error

#### saml_sso_call_back.ApiResponseFor302
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor302 |  |
#### ResponseHeadersFor302

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Location | LocationSchema | | optional

# LocationSchema

Redirect URL of landing page after successful login.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Redirect URL of landing page after successful login. | 


#### saml_sso_call_back.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_oidc_connection**
<a id="update_oidc_connection"></a>
> OIDCObj update_oidc_connection(account_idconnection_idoidc_obj)

Update OIDC connection

Updates a OIDC connection

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.model.oidc_obj import OIDCObj
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'connectionId': "connectionId_example",
    }
    body = OIDCObj(None)
    try:
        # Update OIDC connection
        api_response = api_instance.update_oidc_connection(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->update_oidc_connection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OIDCObj**](../../models/OIDCObj.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 
connectionId | ConnectionIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_oidc_connection.ApiResponseFor200) | SAMLObj
400 | [ApiResponseFor400](#update_oidc_connection.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#update_oidc_connection.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#update_oidc_connection.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#update_oidc_connection.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#update_oidc_connection.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#update_oidc_connection.ApiResponseForDefault) | unexpected error

#### update_oidc_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OIDCObj**](../../models/OIDCObj.md) |  | 


#### update_oidc_connection.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### update_oidc_connection.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### update_oidc_connection.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### update_oidc_connection.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### update_oidc_connection.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### update_oidc_connection.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_saml_connection**
<a id="update_saml_connection"></a>
> SAMLObj update_saml_connection(account_idconnection_idsaml_obj)

Update SAML connection

Updates a SAML connection

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import sso_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.saml_obj import SAMLObj
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sso_api.SsoApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'connectionId': "connectionId_example",
    }
    body = SAMLObj(None)
    try:
        # Update SAML connection
        api_response = api_instance.update_saml_connection(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling SsoApi->update_saml_connection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SAMLObj**](../../models/SAMLObj.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 
connectionId | ConnectionIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_saml_connection.ApiResponseFor200) | SAMLObj
400 | [ApiResponseFor400](#update_saml_connection.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#update_saml_connection.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#update_saml_connection.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#update_saml_connection.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#update_saml_connection.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#update_saml_connection.ApiResponseForDefault) | unexpected error

#### update_saml_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SAMLObj**](../../models/SAMLObj.md) |  | 


#### update_saml_connection.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### update_saml_connection.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### update_saml_connection.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### update_saml_connection.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### update_saml_connection.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### update_saml_connection.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

