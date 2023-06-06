<a id="__pageTop"></a>
# katanemo_sdk.apis.tags.service_api.ServiceApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service**](#create_service) | **post** /service | Create Service
[**create_tags**](#create_tags) | **post** /service/{serviceId}/tags | Add tags to a resource
[**delete_service**](#delete_service) | **delete** /service/{serviceId} | Delete Service
[**get_default_service**](#get_default_service) | **get** /service/3xA | Get Details for Katanemo AAA
[**get_developer_public_keys**](#get_developer_public_keys) | **get** /service/{serviceId}/.well-known/jwks.json | JWKS endpoint for Service
[**get_service**](#get_service) | **get** /service/{serviceId} | Get Service
[**get_tags_for_resource**](#get_tags_for_resource) | **get** /service/{serviceId}/tags | Gets tags for a resource
[**list_services_by_developer**](#list_services_by_developer) | **get** /service | List Services
[**update_service**](#update_service) | **put** /service/{serviceId} | Update Service

# **create_service**
<a id="create_service"></a>
> ServiceResponseObj create_service()

Create Service

Create a Service in Katanemo. Once a service is created Katanemo  identity and authorization capabilities on behalf of SaaS (API) Developers

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import service_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.service_response_obj import ServiceResponseObj
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.create_service_request import CreateServiceRequest
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
    api_instance = service_api.ServiceApi(api_client)

    # example passing only optional values
    body = dict(
        name="name_example",
        description="description_example",
        redirect_url="redirect_url_example",
        api_spec_file=open('/path/to/file', 'rb'),
        auth_exclusion_paths=[
            "auth_exclusion_paths_example"
        ],
        display_name="display_name_example",
        logo_url="logo_url_example",
        details_image_url="details_image_url_example",
        terms_url="terms_url_example",
        privacy_url="privacy_url_example",
        docs_url="docs_url_example",
    )
    try:
        # Create Service
        api_response = api_instance.create_service(
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ServiceApi->create_service: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateServiceRequest**](../../models/CreateServiceRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_service.ApiResponseFor200) | Service Successfully Created.
400 | [ApiResponseFor400](#create_service.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#create_service.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#create_service.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#create_service.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#create_service.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#create_service.ApiResponseForDefault) | unexpected error

#### create_service.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceResponseObj**](../../models/ServiceResponseObj.md) |  | 


#### create_service.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### create_service.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### create_service.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### create_service.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### create_service.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### create_service.ApiResponseForDefault
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

# **create_tags**
<a id="create_tags"></a>
> Tags create_tags(service_idtags)

Add tags to a resource

Add tags (key/value pair) to a particular resource that is created for a service, for a particular organization account id.

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import service_api
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
    api_instance = service_api.ServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceId': "serviceId_example",
    }
    body = Tags(None)
    try:
        # Add tags to a resource
        api_response = api_instance.create_tags(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ServiceApi->create_tags: %s\n" % e)
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
[**Tags**](../../models/Tags.md) |  | 


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
200 | [ApiResponseFor200](#create_tags.ApiResponseFor200) | User account
400 | [ApiResponseFor400](#create_tags.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#create_tags.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#create_tags.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#create_tags.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#create_tags.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#create_tags.ApiResponseForDefault) | unexpected error

#### create_tags.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Tags**](../../models/Tags.md) |  | 


#### create_tags.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### create_tags.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### create_tags.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### create_tags.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### create_tags.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### create_tags.ApiResponseForDefault
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

# **delete_service**
<a id="delete_service"></a>
> delete_service(service_id)

Delete Service

Deletes a service. Note the delete operation is a 'soft' delete where by organizations can't access your service. Requires a bearer token to validate that the caller can delete the service.

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import service_api
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
    api_instance = service_api.ServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceId': "serviceId_example",
    }
    try:
        # Delete Service
        api_response = api_instance.delete_service(
            path_params=path_params,
        )
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ServiceApi->delete_service: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_service.ApiResponseFor200) | Deleted service.
400 | [ApiResponseFor400](#delete_service.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#delete_service.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#delete_service.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#delete_service.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#delete_service.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#delete_service.ApiResponseForDefault) | unexpected error

#### delete_service.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_service.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### delete_service.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### delete_service.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### delete_service.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### delete_service.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### delete_service.ApiResponseForDefault
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

# **get_default_service**
<a id="get_default_service"></a>
> ServiceResponseObj get_default_service()

Get Details for Katanemo AAA

Gets details about Katanemo's AAA SaaS service. Katanemo is powered by Katanemo, and our 3xA service uses the same core identity and authorization capabilities that we offer SaaS (API) developers

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import service_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.service_response_obj import ServiceResponseObj
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
    api_instance = service_api.ServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Details for Katanemo AAA
        api_response = api_instance.get_default_service()
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ServiceApi->get_default_service: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_default_service.ApiResponseFor200) | service
400 | [ApiResponseFor400](#get_default_service.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_default_service.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_default_service.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_default_service.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_default_service.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_default_service.ApiResponseForDefault) | unexpected error

#### get_default_service.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonCharsetUTF8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonCharsetUTF8
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceResponseObj**](../../models/ServiceResponseObj.md) |  | 


#### get_default_service.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_default_service.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_default_service.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_default_service.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_default_service.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_default_service.ApiResponseForDefault
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

# **get_developer_public_keys**
<a id="get_developer_public_keys"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_developer_public_keys(service_id)

JWKS endpoint for Service

Gets public key that can be used to verify jwt token issued by Katanemo. This API does not require bearer authorization

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import service_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.model.oidc_public_key import OIDCPublicKey
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_api.ServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceId': "serviceId_example",
    }
    try:
        # JWKS endpoint for Service
        api_response = api_instance.get_developer_public_keys(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ServiceApi->get_developer_public_keys: %s\n" % e)
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
200 | [ApiResponseFor200](#get_developer_public_keys.ApiResponseFor200) | List of public keys for developer
400 | [ApiResponseFor400](#get_developer_public_keys.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_developer_public_keys.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_developer_public_keys.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_developer_public_keys.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_developer_public_keys.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_developer_public_keys.ApiResponseForDefault) | unexpected error

#### get_developer_public_keys.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[keys](#keys)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# keys

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OIDCPublicKey**]({{complexTypePrefix}}OIDCPublicKey.md) | [**OIDCPublicKey**]({{complexTypePrefix}}OIDCPublicKey.md) | [**OIDCPublicKey**]({{complexTypePrefix}}OIDCPublicKey.md) |  | 

#### get_developer_public_keys.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_developer_public_keys.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_developer_public_keys.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_developer_public_keys.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_developer_public_keys.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_developer_public_keys.ApiResponseForDefault
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

# **get_service**
<a id="get_service"></a>
> ServiceResponseObj get_service(service_id)

Get Service

Gets a Katanemo Service. The principal token must be present in the bearer header to retrieve the service details, unless the service is public

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import service_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.service_response_obj import ServiceResponseObj
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
    api_instance = service_api.ServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceId': "serviceId_example",
    }
    try:
        # Get Service
        api_response = api_instance.get_service(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ServiceApi->get_service: %s\n" % e)
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
200 | [ApiResponseFor200](#get_service.ApiResponseFor200) | service
400 | [ApiResponseFor400](#get_service.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_service.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_service.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_service.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_service.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_service.ApiResponseForDefault) | unexpected error

#### get_service.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceResponseObj**](../../models/ServiceResponseObj.md) |  | 


#### get_service.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_service.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_service.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_service.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_service.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_service.ApiResponseForDefault
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

# **get_tags_for_resource**
<a id="get_tags_for_resource"></a>
> Tags get_tags_for_resource(service_idget_tags_request)

Gets tags for a resource

Gets tags associated with a resource of a service

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import service_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.get_tags_request import GetTagsRequest
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
    api_instance = service_api.ServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceId': "serviceId_example",
    }
    body = GetTagsRequest(None)
    try:
        # Gets tags for a resource
        api_response = api_instance.get_tags_for_resource(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ServiceApi->get_tags_for_resource: %s\n" % e)
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
[**GetTagsRequest**](../../models/GetTagsRequest.md) |  | 


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
200 | [ApiResponseFor200](#get_tags_for_resource.ApiResponseFor200) | tags
400 | [ApiResponseFor400](#get_tags_for_resource.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_tags_for_resource.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_tags_for_resource.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_tags_for_resource.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_tags_for_resource.ApiResponseFor500) | Internal Server Error

#### get_tags_for_resource.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Tags**](../../models/Tags.md) |  | 


#### get_tags_for_resource.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_tags_for_resource.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_tags_for_resource.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_tags_for_resource.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_tags_for_resource.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_services_by_developer**
<a id="list_services_by_developer"></a>
> [ServiceResponseObj] list_services_by_developer()

List Services

List services that belong to a particular developer. Requires bearer token authorization

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import service_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.service_response_obj import ServiceResponseObj
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
    api_instance = service_api.ServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Services
        api_response = api_instance.list_services_by_developer()
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ServiceApi->list_services_by_developer: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_services_by_developer.ApiResponseFor200) | List all services belonging to a developer
400 | [ApiResponseFor400](#list_services_by_developer.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#list_services_by_developer.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#list_services_by_developer.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#list_services_by_developer.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#list_services_by_developer.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#list_services_by_developer.ApiResponseForDefault) | unexpected error

#### list_services_by_developer.ApiResponseFor200
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
[**ServiceResponseObj**]({{complexTypePrefix}}ServiceResponseObj.md) | [**ServiceResponseObj**]({{complexTypePrefix}}ServiceResponseObj.md) | [**ServiceResponseObj**]({{complexTypePrefix}}ServiceResponseObj.md) |  | 

#### list_services_by_developer.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### list_services_by_developer.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### list_services_by_developer.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### list_services_by_developer.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### list_services_by_developer.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### list_services_by_developer.ApiResponseForDefault
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

# **update_service**
<a id="update_service"></a>
> ServiceResponseObj update_service(service_id)

Update Service

Update Service. Requires bearer token authorization for the caller updating the service

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import service_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.service_response_obj import ServiceResponseObj
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.conflict_exception import ConflictException
from katanemo_sdk.model.bad_request_exception import BadRequestException
from katanemo_sdk.model.internal_server_error_exception import InternalServerErrorException
from katanemo_sdk.model.update_service_request import UpdateServiceRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_api.ServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceId': "serviceId_example",
    }
    try:
        # Update Service
        api_response = api_instance.update_service(
            path_params=path_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ServiceApi->update_service: %s\n" % e)

    # example passing only optional values
    path_params = {
        'serviceId': "serviceId_example",
    }
    body = dict(
        name="name_example",
        description="description_example",
        redirect_url="redirect_url_example",
        api_spec_file=open('/path/to/file', 'rb'),
        auth_exclusion_paths=[
            "auth_exclusion_paths_example"
        ],
        display_name="display_name_example",
        logo_url="logo_url_example",
        details_image_url="details_image_url_example",
        terms_url="terms_url_example",
        privacy_url="privacy_url_example",
        docs_url="docs_url_example",
    )
    try:
        # Update Service
        api_response = api_instance.update_service(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling ServiceApi->update_service: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateServiceRequest**](../../models/UpdateServiceRequest.md) |  | 


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
200 | [ApiResponseFor200](#update_service.ApiResponseFor200) | Updated service object.
400 | [ApiResponseFor400](#update_service.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#update_service.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#update_service.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#update_service.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#update_service.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#update_service.ApiResponseForDefault) | unexpected error

#### update_service.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceResponseObj**](../../models/ServiceResponseObj.md) |  | 


#### update_service.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### update_service.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### update_service.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### update_service.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### update_service.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### update_service.ApiResponseForDefault
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

