<a id="__pageTop"></a>
# katanemo_sdk.apis.tags.organization_api.OrganizationApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_key**](#create_client_key) | **post** /org/{accountId}/keys | Create API Key
[**create_role**](#create_role) | **post** /org/{accountId}/role | Creates Role
[**create_user_for_account**](#create_user_for_account) | **post** /org/{accountId}/user | Invite User
[**delete_client_key**](#delete_client_key) | **delete** /org/{accountId}/key/{keyId} | Delete API Key
[**get_account_info**](#get_account_info) | **get** /org/{accountId} | Get Organization
[**get_account_organization**](#get_account_organization) | **get** /org | List Organizations
[**get_client_key**](#get_client_key) | **get** /org/{accountId}/key/{keyId} | Get API Key
[**get_client_key_list**](#get_client_key_list) | **get** /org/{accountId}/keys | List API Keys
[**get_role**](#get_role) | **get** /org/{accountId}/role/{roleId} | Get Role
[**get_roles_for_account**](#get_roles_for_account) | **get** /org/{accountId}/role | List Roles
[**get_user**](#get_user) | **get** /org/{accountId}/user/{userId} | Get User
[**get_users_for_account**](#get_users_for_account) | **get** /org/{accountId}/user | List Users
[**update_account_info**](#update_account_info) | **put** /org/{accountId} | Update Organization
[**update_role**](#update_role) | **put** /org/{accountId}/role/{roleId} | Update Role
[**update_user**](#update_user) | **put** /org/{accountId}/user/{userId} | Update user
[**verify_account_domain**](#verify_account_domain) | **get** /org/{accountId}/verify | Verify Domain

# **create_client_key**
<a id="create_client_key"></a>
> ClientKeyResponse create_client_key(account_idclient_key_request)

Create API Key

Creates a new client key for accessing a developers APIs

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.client_key_response import ClientKeyResponse
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.model.client_key_request import ClientKeyRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    body = ClientKeyRequest(None)
    try:
        # Create API Key
        api_response = api_instance.create_client_key(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->create_client_key: %s\n" % e)
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
[**ClientKeyRequest**](../../models/ClientKeyRequest.md) |  | 


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
200 | [ApiResponseFor200](#create_client_key.ApiResponseFor200) | Successful org keys.
400 | [ApiResponseFor400](#create_client_key.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#create_client_key.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#create_client_key.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#create_client_key.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#create_client_key.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#create_client_key.ApiResponseForDefault) | unexpected error

#### create_client_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClientKeyResponse**](../../models/ClientKeyResponse.md) |  | 


#### create_client_key.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### create_client_key.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### create_client_key.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### create_client_key.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### create_client_key.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### create_client_key.ApiResponseForDefault
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

# **create_role**
<a id="create_role"></a>
> RoleResponse create_role(account_idrole_request)

Creates Role

Creates a new Role

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.role_response import RoleResponse
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.role_request import RoleRequest
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    body = RoleRequest(None)
    try:
        # Creates Role
        api_response = api_instance.create_role(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->create_role: %s\n" % e)
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
[**RoleRequest**](../../models/RoleRequest.md) |  | 


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
200 | [ApiResponseFor200](#create_role.ApiResponseFor200) | Role
400 | [ApiResponseFor400](#create_role.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#create_role.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#create_role.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#create_role.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#create_role.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#create_role.ApiResponseForDefault) | unexpected error

#### create_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoleResponse**](../../models/RoleResponse.md) |  | 


#### create_role.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### create_role.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### create_role.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### create_role.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### create_role.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### create_role.ApiResponseForDefault
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

# **create_user_for_account**
<a id="create_user_for_account"></a>
> UserResponse create_user_for_account(account_iduser_request)

Invite User

Creates a new User and triggers an email verification workflow, followed by set-password

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.user_response import UserResponse
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.model.user_request import UserRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    body = UserRequest(None)
    try:
        # Invite User
        api_response = api_instance.create_user_for_account(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->create_user_for_account: %s\n" % e)
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
[**UserRequest**](../../models/UserRequest.md) |  | 


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
200 | [ApiResponseFor200](#create_user_for_account.ApiResponseFor200) | User
400 | [ApiResponseFor400](#create_user_for_account.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#create_user_for_account.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#create_user_for_account.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#create_user_for_account.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#create_user_for_account.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#create_user_for_account.ApiResponseForDefault) | unexpected error

#### create_user_for_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserResponse**](../../models/UserResponse.md) |  | 


#### create_user_for_account.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### create_user_for_account.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### create_user_for_account.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### create_user_for_account.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### create_user_for_account.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### create_user_for_account.ApiResponseForDefault
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

# **delete_client_key**
<a id="delete_client_key"></a>
> str delete_client_key(account_idkey_id)

Delete API Key

Delete a particular API Key for an organization.

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'keyId': "keyId_example",
    }
    try:
        # Delete API Key
        api_response = api_instance.delete_client_key(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->delete_client_key: %s\n" % e)
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
keyId | KeyIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# KeyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_client_key.ApiResponseFor200) | Successful deletion of client key.
400 | [ApiResponseFor400](#delete_client_key.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#delete_client_key.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#delete_client_key.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#delete_client_key.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#delete_client_key.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#delete_client_key.ApiResponseForDefault) | unexpected error

#### delete_client_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### delete_client_key.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### delete_client_key.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### delete_client_key.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### delete_client_key.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### delete_client_key.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### delete_client_key.ApiResponseForDefault
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

# **get_account_info**
<a id="get_account_info"></a>
> OrganizationResponse get_account_info(account_id)

Get Organization

Returns an object with information regarding an account

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.organization_response import OrganizationResponse
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    try:
        # Get Organization
        api_response = api_instance.get_account_info(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->get_account_info: %s\n" % e)
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
200 | [ApiResponseFor200](#get_account_info.ApiResponseFor200) | Organization
400 | [ApiResponseFor400](#get_account_info.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_account_info.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_account_info.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_account_info.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_account_info.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_account_info.ApiResponseForDefault) | unexpected error

#### get_account_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationResponse**](../../models/OrganizationResponse.md) |  | 


#### get_account_info.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_account_info.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_account_info.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_account_info.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_account_info.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_account_info.ApiResponseForDefault
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

# **get_account_organization**
<a id="get_account_organization"></a>
> OrganizationResponse get_account_organization()

List Organizations

Returns an object with information regarding an account which is present in the token

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.organization_response import OrganizationResponse
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Organizations
        api_response = api_instance.get_account_organization()
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->get_account_organization: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_account_organization.ApiResponseFor200) | Organization of the acccount.
400 | [ApiResponseFor400](#get_account_organization.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_account_organization.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_account_organization.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_account_organization.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_account_organization.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_account_organization.ApiResponseForDefault) | unexpected error

#### get_account_organization.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationResponse**](../../models/OrganizationResponse.md) |  | 


#### get_account_organization.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_account_organization.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_account_organization.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_account_organization.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_account_organization.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_account_organization.ApiResponseForDefault
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

# **get_client_key**
<a id="get_client_key"></a>
> ClientKeyObject get_client_key(account_idkey_id)

Get API Key

Get details of a particular API key for an organization.

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.client_key_object import ClientKeyObject
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'keyId': "keyId_example",
    }
    try:
        # Get API Key
        api_response = api_instance.get_client_key(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->get_client_key: %s\n" % e)
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
keyId | KeyIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# KeyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_client_key.ApiResponseFor200) | Getting client key successful.
400 | [ApiResponseFor400](#get_client_key.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_client_key.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_client_key.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_client_key.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_client_key.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_client_key.ApiResponseForDefault) | unexpected error

#### get_client_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClientKeyObject**](../../models/ClientKeyObject.md) |  | 


#### get_client_key.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_client_key.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_client_key.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_client_key.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_client_key.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_client_key.ApiResponseForDefault
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

# **get_client_key_list**
<a id="get_client_key_list"></a>
> [ClientKeyObject] get_client_key_list(account_id)

List API Keys

List all client keys for an organization accessing a developers service

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.client_key_object import ClientKeyObject
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    try:
        # List API Keys
        api_response = api_instance.get_client_key_list(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->get_client_key_list: %s\n" % e)
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
200 | [ApiResponseFor200](#get_client_key_list.ApiResponseFor200) | List of all users successful.
400 | [ApiResponseFor400](#get_client_key_list.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_client_key_list.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_client_key_list.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_client_key_list.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_client_key_list.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_client_key_list.ApiResponseForDefault) | unexpected error

#### get_client_key_list.ApiResponseFor200
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
[**ClientKeyObject**]({{complexTypePrefix}}ClientKeyObject.md) | [**ClientKeyObject**]({{complexTypePrefix}}ClientKeyObject.md) | [**ClientKeyObject**]({{complexTypePrefix}}ClientKeyObject.md) |  | 

#### get_client_key_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_client_key_list.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_client_key_list.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_client_key_list.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_client_key_list.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_client_key_list.ApiResponseForDefault
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

# **get_role**
<a id="get_role"></a>
> RoleResponse get_role(account_idrole_id)

Get Role

Gets a particular role for an organization

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.role_response import RoleResponse
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'roleId': "roleId_example",
    }
    try:
        # Get Role
        api_response = api_instance.get_role(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->get_role: %s\n" % e)
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
roleId | RoleIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RoleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_role.ApiResponseFor200) | role
400 | [ApiResponseFor400](#get_role.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_role.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_role.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_role.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_role.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_role.ApiResponseForDefault) | unexpected error

#### get_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoleResponse**](../../models/RoleResponse.md) |  | 


#### get_role.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_role.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_role.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_role.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_role.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_role.ApiResponseForDefault
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

# **get_roles_for_account**
<a id="get_roles_for_account"></a>
> [RoleResponse] get_roles_for_account(account_id)

List Roles

Returns a list of all roles belonging to provided organization ID

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.role_response import RoleResponse
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    try:
        # List Roles
        api_response = api_instance.get_roles_for_account(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->get_roles_for_account: %s\n" % e)
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
200 | [ApiResponseFor200](#get_roles_for_account.ApiResponseFor200) | roles belonging to provided account ID
400 | [ApiResponseFor400](#get_roles_for_account.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_roles_for_account.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_roles_for_account.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_roles_for_account.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_roles_for_account.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_roles_for_account.ApiResponseForDefault) | unexpected error

#### get_roles_for_account.ApiResponseFor200
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
[**RoleResponse**]({{complexTypePrefix}}RoleResponse.md) | [**RoleResponse**]({{complexTypePrefix}}RoleResponse.md) | [**RoleResponse**]({{complexTypePrefix}}RoleResponse.md) |  | 

#### get_roles_for_account.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_roles_for_account.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_roles_for_account.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_roles_for_account.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_roles_for_account.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_roles_for_account.ApiResponseForDefault
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

# **get_user**
<a id="get_user"></a>
> UserResponse get_user(account_iduser_id)

Get User

Get a specific user for a particular organization

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.user_response import UserResponse
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'userId': "userId_example",
    }
    try:
        # Get User
        api_response = api_instance.get_user(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->get_user: %s\n" % e)
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
userId | UserIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user.ApiResponseFor200) | user belonging to provided account ID
400 | [ApiResponseFor400](#get_user.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_user.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_user.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_user.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_user.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_user.ApiResponseForDefault) | unexpected error

#### get_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserResponse**](../../models/UserResponse.md) |  | 


#### get_user.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_user.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_user.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_user.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_user.ApiResponseForDefault
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

# **get_users_for_account**
<a id="get_users_for_account"></a>
> [UserResponse] get_users_for_account(account_id)

List Users

Returns a list of all users belonging to provided organization ID

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.user_response import UserResponse
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    try:
        # List Users
        api_response = api_instance.get_users_for_account(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->get_users_for_account: %s\n" % e)
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
200 | [ApiResponseFor200](#get_users_for_account.ApiResponseFor200) | users belonging to provided account ID
400 | [ApiResponseFor400](#get_users_for_account.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_users_for_account.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_users_for_account.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_users_for_account.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_users_for_account.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_users_for_account.ApiResponseForDefault) | unexpected error

#### get_users_for_account.ApiResponseFor200
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
[**UserResponse**]({{complexTypePrefix}}UserResponse.md) | [**UserResponse**]({{complexTypePrefix}}UserResponse.md) | [**UserResponse**]({{complexTypePrefix}}UserResponse.md) |  | 

#### get_users_for_account.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_users_for_account.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_users_for_account.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_users_for_account.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_users_for_account.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_users_for_account.ApiResponseForDefault
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

# **update_account_info**
<a id="update_account_info"></a>
> update_account_info(account_idupdate_organization_request)

Update Organization

Returns status code for successful or failed update.

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.update_organization_request import UpdateOrganizationRequest
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    body = UpdateOrganizationRequest(None)
    try:
        # Update Organization
        api_response = api_instance.update_account_info(
            path_params=path_params,
            body=body,
        )
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->update_account_info: %s\n" % e)
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
[**UpdateOrganizationRequest**](../../models/UpdateOrganizationRequest.md) |  | 


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
200 | [ApiResponseFor200](#update_account_info.ApiResponseFor200) | Successfully updated organization
400 | [ApiResponseFor400](#update_account_info.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#update_account_info.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#update_account_info.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#update_account_info.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#update_account_info.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#update_account_info.ApiResponseForDefault) | unexpected error

#### update_account_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_account_info.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### update_account_info.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### update_account_info.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### update_account_info.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### update_account_info.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### update_account_info.ApiResponseForDefault
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

# **update_role**
<a id="update_role"></a>
> RoleResponse update_role(account_idrole_idrole_request)

Update Role

Update role

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.role_response import RoleResponse
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.role_request import RoleRequest
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
        'roleId': "roleId_example",
    }
    body = RoleRequest(None)
    try:
        # Update Role
        api_response = api_instance.update_role(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->update_role: %s\n" % e)
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
[**RoleRequest**](../../models/RoleRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountId | AccountIdSchema | | 
roleId | RoleIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RoleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_role.ApiResponseFor200) | Updated service object.
400 | [ApiResponseFor400](#update_role.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#update_role.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#update_role.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#update_role.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#update_role.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#update_role.ApiResponseForDefault) | unexpected error

#### update_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoleResponse**](../../models/RoleResponse.md) |  | 


#### update_role.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### update_role.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### update_role.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### update_role.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### update_role.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### update_role.ApiResponseForDefault
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

# **update_user**
<a id="update_user"></a>
> UserResponse update_user(user_idaccount_iduser_request)

Update user

Updates a User account

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.user_response import UserResponse
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.model.user_request import UserRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': "userId_example",
        'accountId': "accountId_example",
    }
    body = UserRequest(None)
    try:
        # Update user
        api_response = api_instance.update_user(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->update_user: %s\n" % e)
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
[**UserRequest**](../../models/UserRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 
accountId | AccountIdSchema | | 

# UserIdSchema

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
200 | [ApiResponseFor200](#update_user.ApiResponseFor200) | User
400 | [ApiResponseFor400](#update_user.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#update_user.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#update_user.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#update_user.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#update_user.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#update_user.ApiResponseForDefault) | unexpected error

#### update_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserResponse**](../../models/UserResponse.md) |  | 


#### update_user.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### update_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### update_user.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### update_user.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### update_user.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### update_user.ApiResponseForDefault
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

# **verify_account_domain**
<a id="verify_account_domain"></a>
> verify_account_domain(account_id)

Verify Domain

Triggers the domain verification flow. If TXT record is created and has the correct verification code, the domain is verified.

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import organization_api
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'accountId': "accountId_example",
    }
    try:
        # Verify Domain
        api_response = api_instance.verify_account_domain(
            path_params=path_params,
        )
    except katanemo_sdk.ApiException as e:
        print("Exception when calling OrganizationApi->verify_account_domain: %s\n" % e)
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
200 | [ApiResponseFor200](#verify_account_domain.ApiResponseFor200) | Domain verified
400 | [ApiResponseFor400](#verify_account_domain.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#verify_account_domain.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#verify_account_domain.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#verify_account_domain.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#verify_account_domain.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#verify_account_domain.ApiResponseForDefault) | unexpected error

#### verify_account_domain.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### verify_account_domain.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### verify_account_domain.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### verify_account_domain.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### verify_account_domain.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### verify_account_domain.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### verify_account_domain.ApiResponseForDefault
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

