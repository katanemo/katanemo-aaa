# katanemo_auth.DefaultApi

All URIs are relative to *https://auth.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_access_logs**](DefaultApi.md#add_access_logs) | **POST** /access-logs | Add access-logs from ARC.
[**authorize_request**](DefaultApi.md#authorize_request) | **POST** /arc/authorize | Authorize a request
[**get_healthz**](DefaultApi.md#get_healthz) | **GET** /healthz | Returns service health


# **add_access_logs**
> add_access_logs(audit_log_entry)

Add access-logs from ARC.

Add access-logs from ARC.

### Example

```python
import time
import os
import katanemo_auth
from katanemo_auth.models.audit_log_entry import AuditLogEntry
from katanemo_auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_auth.Configuration(
    host = "https://auth.katanemo.com"
)


# Enter a context with an instance of the API client
with katanemo_auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_auth.DefaultApi(api_client)
    audit_log_entry = [katanemo_auth.AuditLogEntry()] # List[AuditLogEntry] | List of access logs.

    try:
        # Add access-logs from ARC.
        api_instance.add_access_logs(audit_log_entry)
    except Exception as e:
        print("Exception when calling DefaultApi->add_access_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_log_entry** | [**List[AuditLogEntry]**](AuditLogEntry.md)| List of access logs. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Added logs successfully. |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_request**
> authorize_request(authorization_request)

Authorize a request

Authorize a request

### Example

```python
import time
import os
import katanemo_auth
from katanemo_auth.models.authorization_request import AuthorizationRequest
from katanemo_auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_auth.Configuration(
    host = "https://auth.katanemo.com"
)


# Enter a context with an instance of the API client
with katanemo_auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_auth.DefaultApi(api_client)
    authorization_request = katanemo_auth.AuthorizationRequest() # AuthorizationRequest | Authorization request information.

    try:
        # Authorize a request
        api_instance.authorize_request(authorization_request)
    except Exception as e:
        print("Exception when calling DefaultApi->authorize_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_request** | [**AuthorizationRequest**](AuthorizationRequest.md)| Authorization request information. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful authorization |  -  |
**401** | Invalid Token. |  -  |
**403** | Unauthorized call. |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_healthz**
> str get_healthz()

Returns service health

### Example

```python
import time
import os
import katanemo_auth
from katanemo_auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_auth.Configuration(
    host = "https://auth.katanemo.com"
)


# Enter a context with an instance of the API client
with katanemo_auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_auth.DefaultApi(api_client)

    try:
        # Returns service health
        api_response = api_instance.get_healthz()
        print("The response of DefaultApi->get_healthz:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_healthz: %s\n" % e)
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

