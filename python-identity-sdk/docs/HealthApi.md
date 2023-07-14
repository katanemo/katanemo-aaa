# katanemo_identity.HealthApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_healthz**](HealthApi.md#get_healthz) | **GET** /healthz | Return Katanemo Health


# **get_healthz**
> str get_healthz()

Return Katanemo Health

This API returns the current health of the Katanemo Contorl Plane and Data Plane services.

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_identity.Configuration(
    host = "https://api.katanemo.com"
)


# Enter a context with an instance of the API client
with katanemo_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_identity.HealthApi(api_client)

    try:
        # Return Katanemo Health
        api_response = api_instance.get_healthz()
        print("The response of HealthApi->get_healthz:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->get_healthz: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

