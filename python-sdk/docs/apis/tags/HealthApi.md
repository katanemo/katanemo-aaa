<a id="__pageTop"></a>
# katanemo_sdk.apis.tags.health_api.HealthApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_healthz**](#get_healthz) | **get** /healthz | Return Katanemo Health

# **get_healthz**
<a id="get_healthz"></a>
> str get_healthz()

Return Katanemo Health

This API returns the current health of the Katanemo Contorl Plane and Data Plane services.

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import health_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)

# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = health_api.HealthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return Katanemo Health
        api_response = api_instance.get_healthz()
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling HealthApi->get_healthz: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_healthz.ApiResponseFor200) | token

#### get_healthz.ApiResponseFor200
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

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

