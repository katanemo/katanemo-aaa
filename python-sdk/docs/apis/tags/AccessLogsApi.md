<a id="__pageTop"></a>
# katanemo_sdk.apis.tags.access_logs_api.AccessLogsApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_logs**](#get_audit_logs) | **get** /audit-logs/service/{serviceId}/account/{accountId} | List Access logs

# **get_audit_logs**
<a id="get_audit_logs"></a>
> [AuditLogEntry] get_audit_logs(service_idaccount_idstart_timeend_time)

List Access logs

Return a list of access logs that belong to a particular service and orgaization

### Example

```python
import katanemo_sdk
from katanemo_sdk.apis.tags import access_logs_api
from katanemo_sdk.model.too_many_requests_exception import TooManyRequestsException
from katanemo_sdk.model.error import Error
from katanemo_sdk.model.unauthorized_exception import UnauthorizedException
from katanemo_sdk.model.audit_log_entry import AuditLogEntry
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
    api_instance = access_logs_api.AccessLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceId': "serviceId_example",
        'accountId': "accountId_example",
    }
    query_params = {
        'startTime': "startTime_example",
        'endTime': "endTime_example",
    }
    try:
        # List Access logs
        api_response = api_instance.get_audit_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except katanemo_sdk.ApiException as e:
        print("Exception when calling AccessLogsApi->get_audit_logs: %s\n" % e)
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
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 


# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
serviceId | ServiceIdSchema | | 
accountId | AccountIdSchema | | 

# ServiceIdSchema

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
200 | [ApiResponseFor200](#get_audit_logs.ApiResponseFor200) | List of log entries
400 | [ApiResponseFor400](#get_audit_logs.ApiResponseFor400) | Bad Request Exception
401 | [ApiResponseFor401](#get_audit_logs.ApiResponseFor401) | Unauthorized Exception
409 | [ApiResponseFor409](#get_audit_logs.ApiResponseFor409) | Conflict Exception
429 | [ApiResponseFor429](#get_audit_logs.ApiResponseFor429) | Too Many Requests Exception
500 | [ApiResponseFor500](#get_audit_logs.ApiResponseFor500) | Internal Server Error
default | [ApiResponseForDefault](#get_audit_logs.ApiResponseForDefault) | unexpected error

#### get_audit_logs.ApiResponseFor200
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
[**AuditLogEntry**]({{complexTypePrefix}}AuditLogEntry.md) | [**AuditLogEntry**]({{complexTypePrefix}}AuditLogEntry.md) | [**AuditLogEntry**]({{complexTypePrefix}}AuditLogEntry.md) |  | 

#### get_audit_logs.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestException**](../../models/BadRequestException.md) |  | 


#### get_audit_logs.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedException**](../../models/UnauthorizedException.md) |  | 


#### get_audit_logs.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictException**](../../models/ConflictException.md) |  | 


#### get_audit_logs.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequestsException**](../../models/TooManyRequestsException.md) |  | 


#### get_audit_logs.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerErrorException**](../../models/InternalServerErrorException.md) |  | 


#### get_audit_logs.ApiResponseForDefault
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

