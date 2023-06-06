# katanemo_sdk.AccessControlApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_role_to_principal**](AccessControlApi.md#assign_role_to_principal) | **POST** /assignrole | Assign role
[**assume_role**](AccessControlApi.md#assume_role) | **POST** /assumeRole | Assume role
[**create_client_key**](AccessControlApi.md#create_client_key) | **POST** /org/{accountId}/keys | Create API Key
[**create_role**](AccessControlApi.md#create_role) | **POST** /org/{accountId}/role | Creates Role
[**create_tags**](AccessControlApi.md#create_tags) | **POST** /service/{serviceId}/tags | Add tags to a resource
[**delete_client_key**](AccessControlApi.md#delete_client_key) | **DELETE** /org/{accountId}/key/{keyId} | Delete API Key
[**get_client_key**](AccessControlApi.md#get_client_key) | **GET** /org/{accountId}/key/{keyId} | Get API Key
[**get_client_key_list**](AccessControlApi.md#get_client_key_list) | **GET** /org/{accountId}/keys | List API Keys
[**get_o_auth_token**](AccessControlApi.md#get_o_auth_token) | **POST** /oauth/token | OAuth Token
[**get_role**](AccessControlApi.md#get_role) | **GET** /org/{accountId}/role/{roleId} | Get Role
[**get_roles_for_account**](AccessControlApi.md#get_roles_for_account) | **GET** /org/{accountId}/role | List Roles
[**get_short_term_token**](AccessControlApi.md#get_short_term_token) | **POST** /token | Get Token
[**get_tags_for_resource**](AccessControlApi.md#get_tags_for_resource) | **GET** /service/{serviceId}/tags | Gets tags for a resource
[**update_role**](AccessControlApi.md#update_role) | **PUT** /org/{accountId}/role/{roleId} | Update Role


# **assign_role_to_principal**
> UserResponse assign_role_to_principal(assign_role_obj)

Assign role

Assign role to an identity principal

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.assign_role_obj import AssignRoleObj
from katanemo_sdk.models.user_response import UserResponse
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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    assign_role_obj = katanemo_sdk.AssignRoleObj() # AssignRoleObj | Role assignment

    try:
        # Assign role
        api_response = api_instance.assign_role_to_principal(assign_role_obj)
        print("The response of AccessControlApi->assign_role_to_principal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->assign_role_to_principal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_role_obj** | [**AssignRoleObj**](AssignRoleObj.md)| Role assignment | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **assume_role**
> str assume_role(assume_role_obj)

Assume role

Creates a token with requested roleId

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.assume_role_obj import AssumeRoleObj
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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    assume_role_obj = katanemo_sdk.AssumeRoleObj() # AssumeRoleObj | Role assignment

    try:
        # Assume role
        api_response = api_instance.assume_role(assume_role_obj)
        print("The response of AccessControlApi->assume_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->assume_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assume_role_obj** | [**AssumeRoleObj**](AssumeRoleObj.md)| Role assignment | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | token |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_key**
> ClientKeyResponse create_client_key(account_id, client_key_request)

Create API Key

Creates a new client key for accessing a developers APIs

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.client_key_request import ClientKeyRequest
from katanemo_sdk.models.client_key_response import ClientKeyResponse
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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    account_id = 'account_id_example' # str | 
    client_key_request = katanemo_sdk.ClientKeyRequest() # ClientKeyRequest | 

    try:
        # Create API Key
        api_response = api_instance.create_client_key(account_id, client_key_request)
        print("The response of AccessControlApi->create_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->create_client_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **client_key_request** | [**ClientKeyRequest**](ClientKeyRequest.md)|  | 

### Return type

[**ClientKeyResponse**](ClientKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful org keys. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> RoleResponse create_role(account_id, role_request)

Creates Role

Creates a new Role

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.role_request import RoleRequest
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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    account_id = 'account_id_example' # str | 
    role_request = katanemo_sdk.RoleRequest() # RoleRequest | Role to add to the system

    try:
        # Creates Role
        api_response = api_instance.create_role(account_id, role_request)
        print("The response of AccessControlApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->create_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **role_request** | [**RoleRequest**](RoleRequest.md)| Role to add to the system | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role |  -  |
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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    service_id = 'service_id_example' # str | 
    tags = katanemo_sdk.Tags() # Tags | Tags and resource id

    try:
        # Add tags to a resource
        api_response = api_instance.create_tags(service_id, tags)
        print("The response of AccessControlApi->create_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->create_tags: %s\n" % e)
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

# **delete_client_key**
> str delete_client_key(account_id, key_id)

Delete API Key

Delete a particular API Key for an organization.

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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    account_id = 'account_id_example' # str | 
    key_id = 'key_id_example' # str | 

    try:
        # Delete API Key
        api_response = api_instance.delete_client_key(account_id, key_id)
        print("The response of AccessControlApi->delete_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->delete_client_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **key_id** | **str**|  | 

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
**200** | Successful deletion of client key. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_key**
> ClientKeyObject get_client_key(account_id, key_id)

Get API Key

Get details of a particular API key for an organization.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.client_key_object import ClientKeyObject
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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    account_id = 'account_id_example' # str | 
    key_id = 'key_id_example' # str | 

    try:
        # Get API Key
        api_response = api_instance.get_client_key(account_id, key_id)
        print("The response of AccessControlApi->get_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_client_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

[**ClientKeyObject**](ClientKeyObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Getting client key successful. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_key_list**
> List[ClientKeyObject] get_client_key_list(account_id)

List API Keys

List all client keys for an organization accessing a developers service

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.client_key_object import ClientKeyObject
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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # List API Keys
        api_response = api_instance.get_client_key_list(account_id)
        print("The response of AccessControlApi->get_client_key_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_client_key_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**List[ClientKeyObject]**](ClientKeyObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all users successful. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_token**
> OAuthTokenResponse get_o_auth_token(o_auth_token_request)

OAuth Token

Get an OAuth2.0 Token for an Authorization Code

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.o_auth_token_request import OAuthTokenRequest
from katanemo_sdk.models.o_auth_token_response import OAuthTokenResponse
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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    o_auth_token_request = katanemo_sdk.OAuthTokenRequest() # OAuthTokenRequest | 

    try:
        # OAuth Token
        api_response = api_instance.get_o_auth_token(o_auth_token_request)
        print("The response of AccessControlApi->get_o_auth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_o_auth_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_token_request** | [**OAuthTokenRequest**](OAuthTokenRequest.md)|  | 

### Return type

[**OAuthTokenResponse**](OAuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Getting token for client ID successful. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleResponse get_role(account_id, role_id)

Get Role

Gets a particular role for an organization

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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    account_id = 'account_id_example' # str | 
    role_id = 'role_id_example' # str | 

    try:
        # Get Role
        api_response = api_instance.get_role(account_id, role_id)
        print("The response of AccessControlApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | role |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles_for_account**
> List[RoleResponse] get_roles_for_account(account_id)

List Roles

Returns a list of all roles belonging to provided organization ID

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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # List Roles
        api_response = api_instance.get_roles_for_account(account_id)
        print("The response of AccessControlApi->get_roles_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_roles_for_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

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
**200** | roles belonging to provided account ID |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_short_term_token**
> TokenResponse get_short_term_token(token_request)

Get Token

Returns a short-lived token for API key/secret pair. Tokens contain claims that identify what a principal can or cannot do.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.token_request import TokenRequest
from katanemo_sdk.models.token_response import TokenResponse
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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    token_request = katanemo_sdk.TokenRequest() # TokenRequest | 

    try:
        # Get Token
        api_response = api_instance.get_short_term_token(token_request)
        print("The response of AccessControlApi->get_short_term_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_short_term_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**TokenRequest**](TokenRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generate Token for an authentication principal |  -  |
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
import katanemo_sdk
from katanemo_sdk.models.get_tags_request import GetTagsRequest
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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    service_id = 'service_id_example' # str | 
    get_tags_request = katanemo_sdk.GetTagsRequest() # GetTagsRequest | Tags and resource id

    try:
        # Gets tags for a resource
        api_response = api_instance.get_tags_for_resource(service_id, get_tags_request)
        print("The response of AccessControlApi->get_tags_for_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_tags_for_resource: %s\n" % e)
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

# **update_role**
> RoleResponse update_role(account_id, role_id, role_request)

Update Role

Update role

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.role_request import RoleRequest
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
    api_instance = katanemo_sdk.AccessControlApi(api_client)
    account_id = 'account_id_example' # str | 
    role_id = 'role_id_example' # str | 
    role_request = katanemo_sdk.RoleRequest() # RoleRequest | Role object that is being updated.

    try:
        # Update Role
        api_response = api_instance.update_role(account_id, role_id, role_request)
        print("The response of AccessControlApi->update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->update_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **role_id** | **str**|  | 
 **role_request** | [**RoleRequest**](RoleRequest.md)| Role object that is being updated. | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

