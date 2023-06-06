# katanemo_sdk.DefaultApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize**](DefaultApi.md#authorize) | **GET** /authorize | Initiate the login flow by redirecting to login page
[**post_authorize**](DefaultApi.md#post_authorize) | **POST** /arc/authorize | dummy endpoint for authorize


# **authorize**
> authorize(authorize_request)

Initiate the login flow by redirecting to login page

Determine where to take a user for login

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.authorize_request import AuthorizeRequest
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    authorize_request = katanemo_sdk.AuthorizeRequest() # AuthorizeRequest | parameters requiired to determine where to take the user

    try:
        # Initiate the login flow by redirecting to login page
        api_instance.authorize(authorize_request)
    except Exception as e:
        print("Exception when calling DefaultApi->authorize: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorize_request** | [**AuthorizeRequest**](AuthorizeRequest.md)| parameters requiired to determine where to take the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to Katanemo&#39;s signin page |  * Location - Redirect URL of landing page after successful login. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_authorize**
> post_authorize()

dummy endpoint for authorize

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)

    try:
        # dummy endpoint for authorize
        api_instance.post_authorize()
    except Exception as e:
        print("Exception when calling DefaultApi->post_authorize: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request Exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

