<a id="__pageTop"></a>
# katanemo_sdk.apis.tags.default_api.DefaultApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize**](#authorize) | **post** /authorize | Initiate the login flow by redirecting to login page
[**post_authorize**](#post_authorize) | **post** /arc/authorize | dummy endpoint for authorize

# **authorize**
<a id="authorize"></a>
> authorize(authorize_request)

Initiate the login flow by redirecting to login page

Determine where to take a user for login

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import default_api
from katanemo_sdk.model.authorize_request import AuthorizeRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = AuthorizeRequest(None)
    try:
        # Initiate the login flow by redirecting to login page
        api_response = api_instance.authorize(
            body=body,
        )
    except katanemo_sdk.ApiException as e:
        print("Exception when calling DefaultApi->authorize: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizeRequest**](../../models/AuthorizeRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
302 | [ApiResponseFor302](#authorize.ApiResponseFor302) | Redirect to Katanemo&#x27;s signin page

#### authorize.ApiResponseFor302
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

URL of the Katanemo signin landing page

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | URL of the Katanemo signin landing page | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_authorize**
<a id="post_authorize"></a>
> post_authorize()

dummy endpoint for authorize

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import default_api
from katanemo_sdk.model.bad_request_exception import BadRequestException
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # dummy endpoint for authorize
        api_response = api_instance.post_authorize()
    except katanemo_sdk.ApiException as e:
        print("Exception when calling DefaultApi->post_authorize: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#post_authorize.ApiResponseFor400) | Bad Request Exception

#### post_authorize.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

