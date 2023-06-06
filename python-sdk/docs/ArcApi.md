# katanemo_sdk.ArcApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_roles_for_service**](ArcApi.md#get_roles_for_service) | **GET** /arc/{serviceId}/role | Get Service Roles
[**get_tags_for_service**](ArcApi.md#get_tags_for_service) | **GET** /arc/{serviceId}/tags | Get Resource Tags
[**init_arc_client**](ArcApi.md#init_arc_client) | **GET** /arc/{serviceId}/init | Initialize ARC Client


# **get_roles_for_service**
> List[RoleResponse] get_roles_for_service(service_id, limit=limit)

Get Service Roles

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.role_response import RoleResponse
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
    api_instance = katanemo_sdk.ArcApi(api_client)
    service_id = 'service_id_example' # str | 
    limit = 56 # int |  (optional)

    try:
        # Get Service Roles
        api_response = api_instance.get_roles_for_service(service_id, limit=limit)
        print("The response of ArcApi->get_roles_for_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcApi->get_roles_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**List[RoleResponse]**](RoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of roles for service. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_for_service**
> List[Tags] get_tags_for_service(service_id, limit=limit)

Get Resource Tags

Get all resource tags associated with a Katanemo Service.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.tags import Tags
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
    api_instance = katanemo_sdk.ArcApi(api_client)
    service_id = 'service_id_example' # str | 
    limit = 56 # int |  (optional)

    try:
        # Get Resource Tags
        api_response = api_instance.get_tags_for_service(service_id, limit=limit)
        print("The response of ArcApi->get_tags_for_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcApi->get_tags_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**List[Tags]**](Tags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of tags for service. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_arc_client**
> List[InitArcResponse] init_arc_client(service_id)

Initialize ARC Client

Initiative the Authorization Runtime Client with Developer API Keys

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.init_arc_response import InitArcResponse
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
    api_instance = katanemo_sdk.ArcApi(api_client)
    service_id = 'service_id_example' # str | 

    try:
        # Initialize ARC Client
        api_response = api_instance.init_arc_client(service_id)
        print("The response of ArcApi->init_arc_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcApi->init_arc_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**List[InitArcResponse]**](InitArcResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of init arc client. |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

