<a id="__pageTop"></a>
# katanemo_sdk.apis.tags.arc_api.ArcApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_roles_for_service**](#get_roles_for_service) | **get** /arc/{serviceId}/role | Get Service Roles
[**get_tags_for_service**](#get_tags_for_service) | **get** /arc/{serviceId}/tags | Get Resource Tags
[**init_arc_client**](#init_arc_client) | **get** /arc/{serviceId}/init | Initialize ARC Client

# **get_roles_for_service**
<a id="get_roles_for_service"></a>
> [RoleResponse] get_roles_for_service(service_id)

Get Service Roles

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import arc_api
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
    api_instance = arc_api.ArcApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceId': "serviceId_example",
    }
    query_params = {
    }
    try:
        # Get Service Roles
        api_response = api_instance.get_roles_for_service(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ArcApi->get_roles_for_service: %s\n" % e)

    # example passing only optional values
    path_params = {
        'serviceId': "serviceId_example",
    }
    query_params = {
        'limit': 1,
    }
    try:
        # Get Service Roles
        api_response = api_instance.get_roles_for_service(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ArcApi->get_roles_for_service: %s\n" % e)
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
limit | LimitSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
serviceId | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_roles_for_service.ApiResponseFor200) | Successful retrieval of roles for service.
400 | [ApiResponseFor400](#get_roles_for_service.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_roles_for_service.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_roles_for_service.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_roles_for_service.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_roles_for_service.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_roles_for_service.ApiResponseForDefault) | unexpected error

#### get_roles_for_service.ApiResponseFor200
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

#### get_roles_for_service.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_roles_for_service.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_roles_for_service.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_roles_for_service.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_roles_for_service.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_roles_for_service.ApiResponseForDefault
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

# **get_tags_for_service**
<a id="get_tags_for_service"></a>
> [Tags] get_tags_for_service(service_id)

Get Resource Tags

Get all resource tags associated with a Katanemo Service.

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import arc_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.tags import Tags
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
    api_instance = arc_api.ArcApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceId': "serviceId_example",
    }
    query_params = {
    }
    try:
        # Get Resource Tags
        api_response = api_instance.get_tags_for_service(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ArcApi->get_tags_for_service: %s\n" % e)

    # example passing only optional values
    path_params = {
        'serviceId': "serviceId_example",
    }
    query_params = {
        'limit': 1,
    }
    try:
        # Get Resource Tags
        api_response = api_instance.get_tags_for_service(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ArcApi->get_tags_for_service: %s\n" % e)
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
limit | LimitSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
serviceId | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_tags_for_service.ApiResponseFor200) | Successful retrieval of tags for service.
400 | [ApiResponseFor400](#get_tags_for_service.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_tags_for_service.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_tags_for_service.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_tags_for_service.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_tags_for_service.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_tags_for_service.ApiResponseForDefault) | unexpected error

#### get_tags_for_service.ApiResponseFor200
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
[**Tags**]({{complexTypePrefix}}Tags.md) | [**Tags**]({{complexTypePrefix}}Tags.md) | [**Tags**]({{complexTypePrefix}}Tags.md) |  | 

#### get_tags_for_service.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_tags_for_service.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_tags_for_service.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_tags_for_service.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_tags_for_service.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_tags_for_service.ApiResponseForDefault
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

# **init_arc_client**
<a id="init_arc_client"></a>
> [InitArcResponse] init_arc_client(service_id)

Initialize ARC Client

Initiative the Authorization Runtime Client with Developer API Keys

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import arc_api
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.init_arc_response import InitArcResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arc_api.ArcApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceId': "serviceId_example",
    }
    try:
        # Initialize ARC Client
        api_response = api_instance.init_arc_client(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ArcApi->init_arc_client: %s\n" % e)
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
serviceId | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#init_arc_client.ApiResponseFor200) | Successful retrieval of init arc client.
default | [ApiResponseForDefault](#init_arc_client.ApiResponseForDefault) | unexpected error

#### init_arc_client.ApiResponseFor200
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
[**InitArcResponse**]({{complexTypePrefix}}InitArcResponse.md) | [**InitArcResponse**]({{complexTypePrefix}}InitArcResponse.md) | [**InitArcResponse**]({{complexTypePrefix}}InitArcResponse.md) |  | 

#### init_arc_client.ApiResponseForDefault
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

