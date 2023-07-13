# katanemo_identity.ServiceApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service**](ServiceApi.md#create_service) | **POST** /service | Create Service
[**create_tags**](ServiceApi.md#create_tags) | **POST** /service/{serviceId}/tags | Add tags to a resource
[**delete_service**](ServiceApi.md#delete_service) | **DELETE** /service/{serviceId} | Delete Service
[**get_default_service**](ServiceApi.md#get_default_service) | **GET** /service/3xA | Get Details for Katanemo AAA
[**get_developer_public_keys**](ServiceApi.md#get_developer_public_keys) | **GET** /service/{serviceId}/.well-known/jwks.json | JWKS endpoint for Service
[**get_service**](ServiceApi.md#get_service) | **GET** /service/{serviceId} | Get Service
[**get_tags_for_resource**](ServiceApi.md#get_tags_for_resource) | **GET** /service/{serviceId}/tags | Gets tags for a resource
[**list_services_by_developer**](ServiceApi.md#list_services_by_developer) | **GET** /service | List Services
[**update_service**](ServiceApi.md#update_service) | **PUT** /service/{serviceId} | Update Service


# **create_service**
> ServiceResponseObj create_service(name, redirect_url, api_spec_file, description=description, auth_exclusion_paths=auth_exclusion_paths, display_name=display_name, logo_url=logo_url, details_image_url=details_image_url, terms_url=terms_url, privacy_url=privacy_url, docs_url=docs_url)

Create Service

Create a Service in Katanemo. Once a service is created Katanemo  identity and authorization capabilities on behalf of SaaS (API) Developers

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.service_response_obj import ServiceResponseObj
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
    api_instance = katanemo_identity.ServiceApi(api_client)
    name = 'name_example' # str | Service Name
    redirect_url = 'redirect_url_example' # str | Redirect URL after a successful login.
    api_spec_file = None # bytearray | openapi service json or yaml file
    description = 'description_example' # str | Service Description (optional)
    auth_exclusion_paths = ['auth_exclusion_paths_example'] # List[str] | List of paths for which we do not require authentication (optional)
    display_name = 'display_name_example' # str | Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages (optional)
    logo_url = 'logo_url_example' # str | The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages (optional)
    details_image_url = 'details_image_url_example' # str | The URL of image showing details about the service to be displayed on the sign-up page. (optional)
    terms_url = 'terms_url_example' # str | The URL for the terms of the service (optional)
    privacy_url = 'privacy_url_example' # str | The URL for the privacy of the service (optional)
    docs_url = 'docs_url_example' # str | The URL for the documentation of the service (optional)

    try:
        # Create Service
        api_response = api_instance.create_service(name, redirect_url, api_spec_file, description=description, auth_exclusion_paths=auth_exclusion_paths, display_name=display_name, logo_url=logo_url, details_image_url=details_image_url, terms_url=terms_url, privacy_url=privacy_url, docs_url=docs_url)
        print("The response of ServiceApi->create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->create_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Service Name | 
 **redirect_url** | **str**| Redirect URL after a successful login. | 
 **api_spec_file** | **bytearray**| openapi service json or yaml file | 
 **description** | **str**| Service Description | [optional] 
 **auth_exclusion_paths** | [**List[str]**](str.md)| List of paths for which we do not require authentication | [optional] 
 **display_name** | **str**| Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
 **logo_url** | **str**| The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
 **details_image_url** | **str**| The URL of image showing details about the service to be displayed on the sign-up page. | [optional] 
 **terms_url** | **str**| The URL for the terms of the service | [optional] 
 **privacy_url** | **str**| The URL for the privacy of the service | [optional] 
 **docs_url** | **str**| The URL for the documentation of the service | [optional] 

### Return type

[**ServiceResponseObj**](ServiceResponseObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service Successfully Created. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tags**
> Tags create_tags(service_id, tags)

Add tags to a resource

Add tags (key/value pair) to a particular resource that is created for a service, for a particular organization account id.

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.tags import Tags
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
    api_instance = katanemo_identity.ServiceApi(api_client)
    service_id = 'service_id_example' # str | 
    tags = katanemo_identity.Tags() # Tags | Tags and resource id

    try:
        # Add tags to a resource
        api_response = api_instance.create_tags(service_id, tags)
        print("The response of ServiceApi->create_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->create_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **tags** | [**Tags**](Tags.md)| Tags and resource id | 

### Return type

[**Tags**](Tags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User account |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service**
> delete_service(service_id)

Delete Service

Deletes a service. Note the delete operation is a 'soft' delete where by organizations can't access your service. Requires a bearer token to validate that the caller can delete the service.

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
    api_instance = katanemo_identity.ServiceApi(api_client)
    service_id = 'service_id_example' # str | 

    try:
        # Delete Service
        api_instance.delete_service(service_id)
    except Exception as e:
        print("Exception when calling ServiceApi->delete_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

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
**200** | Deleted service. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_service**
> ServiceResponseObj get_default_service()

Get Details for Katanemo AAA

Gets details about Katanemo's AAA SaaS service. Katanemo is powered by Katanemo, and our 3xA service uses the same core identity and authorization capabilities that we offer SaaS (API) developers

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.service_response_obj import ServiceResponseObj
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
    api_instance = katanemo_identity.ServiceApi(api_client)

    try:
        # Get Details for Katanemo AAA
        api_response = api_instance.get_default_service()
        print("The response of ServiceApi->get_default_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->get_default_service: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceResponseObj**](ServiceResponseObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | service |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_developer_public_keys**
> GetDeveloperPublicKeys200Response get_developer_public_keys(service_id)

JWKS endpoint for Service

Gets public key that can be used to verify jwt token issued by Katanemo. This API does not require bearer authorization

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.get_developer_public_keys200_response import GetDeveloperPublicKeys200Response
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
    api_instance = katanemo_identity.ServiceApi(api_client)
    service_id = 'service_id_example' # str | 

    try:
        # JWKS endpoint for Service
        api_response = api_instance.get_developer_public_keys(service_id)
        print("The response of ServiceApi->get_developer_public_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->get_developer_public_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**GetDeveloperPublicKeys200Response**](GetDeveloperPublicKeys200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of public keys for developer |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> ServiceResponseObj get_service(service_id)

Get Service

Gets a Katanemo Service. The principal token must be present in the bearer header to retrieve the service details, unless the service is public

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.service_response_obj import ServiceResponseObj
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
    api_instance = katanemo_identity.ServiceApi(api_client)
    service_id = 'service_id_example' # str | 

    try:
        # Get Service
        api_response = api_instance.get_service(service_id)
        print("The response of ServiceApi->get_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->get_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**ServiceResponseObj**](ServiceResponseObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | service |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_for_resource**
> Tags get_tags_for_resource(service_id, get_tags_request)

Gets tags for a resource

Gets tags associated with a resource of a service

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.get_tags_request import GetTagsRequest
from katanemo_identity.models.tags import Tags
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
    api_instance = katanemo_identity.ServiceApi(api_client)
    service_id = 'service_id_example' # str | 
    get_tags_request = katanemo_identity.GetTagsRequest() # GetTagsRequest | Tags and resource id

    try:
        # Gets tags for a resource
        api_response = api_instance.get_tags_for_resource(service_id, get_tags_request)
        print("The response of ServiceApi->get_tags_for_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->get_tags_for_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **get_tags_request** | [**GetTagsRequest**](GetTagsRequest.md)| Tags and resource id | 

### Return type

[**Tags**](Tags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tags |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_services_by_developer**
> List[ServiceResponseObj] list_services_by_developer()

List Services

List services that belong to a particular developer. Requires bearer token authorization

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.service_response_obj import ServiceResponseObj
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
    api_instance = katanemo_identity.ServiceApi(api_client)

    try:
        # List Services
        api_response = api_instance.list_services_by_developer()
        print("The response of ServiceApi->list_services_by_developer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_services_by_developer: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ServiceResponseObj]**](ServiceResponseObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all services belonging to a developer |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service**
> ServiceResponseObj update_service(service_id, name=name, description=description, redirect_url=redirect_url, api_spec_file=api_spec_file, auth_exclusion_paths=auth_exclusion_paths, display_name=display_name, logo_url=logo_url, details_image_url=details_image_url, terms_url=terms_url, privacy_url=privacy_url, docs_url=docs_url)

Update Service

Update Service. Requires bearer token authorization for the caller updating the service

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.service_response_obj import ServiceResponseObj
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
    api_instance = katanemo_identity.ServiceApi(api_client)
    service_id = 'service_id_example' # str | 
    name = 'name_example' # str | Service Name (optional)
    description = 'description_example' # str | Service Description (optional)
    redirect_url = 'redirect_url_example' # str | Redirect URL after a successful login. (optional)
    api_spec_file = None # bytearray | openapi service json or yaml file (optional)
    auth_exclusion_paths = ['auth_exclusion_paths_example'] # List[str] | List of paths for which we do not require authentication (optional)
    display_name = 'display_name_example' # str | Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages (optional)
    logo_url = 'logo_url_example' # str | The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages (optional)
    details_image_url = 'details_image_url_example' # str | The URL of image showing details about the service to be displayed on the sign-up page. (optional)
    terms_url = 'terms_url_example' # str | The URL for the terms of the service (optional)
    privacy_url = 'privacy_url_example' # str | The URL for the privacy of the service (optional)
    docs_url = 'docs_url_example' # str | The URL for the documentatio of the service (optional)

    try:
        # Update Service
        api_response = api_instance.update_service(service_id, name=name, description=description, redirect_url=redirect_url, api_spec_file=api_spec_file, auth_exclusion_paths=auth_exclusion_paths, display_name=display_name, logo_url=logo_url, details_image_url=details_image_url, terms_url=terms_url, privacy_url=privacy_url, docs_url=docs_url)
        print("The response of ServiceApi->update_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->update_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **name** | **str**| Service Name | [optional] 
 **description** | **str**| Service Description | [optional] 
 **redirect_url** | **str**| Redirect URL after a successful login. | [optional] 
 **api_spec_file** | **bytearray**| openapi service json or yaml file | [optional] 
 **auth_exclusion_paths** | [**List[str]**](str.md)| List of paths for which we do not require authentication | [optional] 
 **display_name** | **str**| Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
 **logo_url** | **str**| The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
 **details_image_url** | **str**| The URL of image showing details about the service to be displayed on the sign-up page. | [optional] 
 **terms_url** | **str**| The URL for the terms of the service | [optional] 
 **privacy_url** | **str**| The URL for the privacy of the service | [optional] 
 **docs_url** | **str**| The URL for the documentatio of the service | [optional] 

### Return type

[**ServiceResponseObj**](ServiceResponseObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated service object. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

