# katanemo_identity.AccessLogsApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_logs**](AccessLogsApi.md#get_audit_logs) | **GET** /audit-logs/service/{serviceId}/account/{accountId} | List Access logs


# **get_audit_logs**
> List[AuditLogEntry] get_audit_logs(service_id, account_id, start_time, end_time)

List Access logs

Return a list of access logs that belong to a particular service and orgaization

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.audit_log_entry import AuditLogEntry
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
    api_instance = katanemo_identity.AccessLogsApi(api_client)
    service_id = 'service_id_example' # str | 
    account_id = 'account_id_example' # str | 
    start_time = 'start_time_example' # str | Start time of log entries in the format YYYY-MM-DDThh-mm-ss (e.g. 2023-01-15T15-28-58 which means 2023-01-15 15:28:58)
    end_time = 'end_time_example' # str | End time of log entries in the format YYYY-MM-DDThh-mm-ss (e.g. 2023-01-15T15-28-58 which means 2023-01-15 15:28:58)

    try:
        # List Access logs
        api_response = api_instance.get_audit_logs(service_id, account_id, start_time, end_time)
        print("The response of AccessLogsApi->get_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessLogsApi->get_audit_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **account_id** | **str**|  | 
 **start_time** | **str**| Start time of log entries in the format YYYY-MM-DDThh-mm-ss (e.g. 2023-01-15T15-28-58 which means 2023-01-15 15:28:58) | 
 **end_time** | **str**| End time of log entries in the format YYYY-MM-DDThh-mm-ss (e.g. 2023-01-15T15-28-58 which means 2023-01-15 15:28:58) | 

### Return type

[**List[AuditLogEntry]**](AuditLogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of log entries |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

