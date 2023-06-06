# katanemo_sdk.OrganizationApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_key**](OrganizationApi.md#create_client_key) | **POST** /org/{accountId}/keys | Create API Key
[**create_role**](OrganizationApi.md#create_role) | **POST** /org/{accountId}/role | Creates Role
[**create_user_for_account**](OrganizationApi.md#create_user_for_account) | **POST** /org/{accountId}/user | Invite User
[**delete_client_key**](OrganizationApi.md#delete_client_key) | **DELETE** /org/{accountId}/key/{keyId} | Delete API Key
[**get_account_info**](OrganizationApi.md#get_account_info) | **GET** /org/{accountId} | Get Organization
[**get_account_organization**](OrganizationApi.md#get_account_organization) | **GET** /org | List Organizations
[**get_client_key**](OrganizationApi.md#get_client_key) | **GET** /org/{accountId}/key/{keyId} | Get API Key
[**get_client_key_list**](OrganizationApi.md#get_client_key_list) | **GET** /org/{accountId}/keys | List API Keys
[**get_role**](OrganizationApi.md#get_role) | **GET** /org/{accountId}/role/{roleId} | Get Role
[**get_roles_for_account**](OrganizationApi.md#get_roles_for_account) | **GET** /org/{accountId}/role | List Roles
[**get_user**](OrganizationApi.md#get_user) | **GET** /org/{accountId}/user/{userId} | Get User
[**get_users_for_account**](OrganizationApi.md#get_users_for_account) | **GET** /org/{accountId}/user | List Users
[**update_account_info**](OrganizationApi.md#update_account_info) | **PUT** /org/{accountId} | Update Organization
[**update_role**](OrganizationApi.md#update_role) | **PUT** /org/{accountId}/role/{roleId} | Update Role
[**update_user**](OrganizationApi.md#update_user) | **PUT** /org/{accountId}/user/{userId} | Update user
[**verify_account_domain**](OrganizationApi.md#verify_account_domain) | **GET** /org/{accountId}/verify | Verify Domain


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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 
    client_key_request = katanemo_sdk.ClientKeyRequest() # ClientKeyRequest | 

    try:
        # Create API Key
        api_response = api_instance.create_client_key(account_id, client_key_request)
        print("The response of OrganizationApi->create_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->create_client_key: %s\n" % e)
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 
    role_request = katanemo_sdk.RoleRequest() # RoleRequest | Role to add to the system

    try:
        # Creates Role
        api_response = api_instance.create_role(account_id, role_request)
        print("The response of OrganizationApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->create_role: %s\n" % e)
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

# **create_user_for_account**
> UserResponse create_user_for_account(account_id, user_request)

Invite User

Creates a new User and triggers an email verification workflow, followed by set-password

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.user_request import UserRequest
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 
    user_request = katanemo_sdk.UserRequest() # UserRequest | User information

    try:
        # Invite User
        api_response = api_instance.create_user_for_account(account_id, user_request)
        print("The response of OrganizationApi->create_user_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->create_user_for_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **user_request** | [**UserRequest**](UserRequest.md)| User information | 

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
**200** | User |  -  |
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 
    key_id = 'key_id_example' # str | 

    try:
        # Delete API Key
        api_response = api_instance.delete_client_key(account_id, key_id)
        print("The response of OrganizationApi->delete_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->delete_client_key: %s\n" % e)
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

# **get_account_info**
> OrganizationResponse get_account_info(account_id)

Get Organization

Returns an object with information regarding an account

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.organization_response import OrganizationResponse
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Get Organization
        api_response = api_instance.get_account_info(account_id)
        print("The response of OrganizationApi->get_account_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_account_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_organization**
> OrganizationResponse get_account_organization()

List Organizations

Returns an object with information regarding an account which is present in the token

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.organization_response import OrganizationResponse
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)

    try:
        # List Organizations
        api_response = api_instance.get_account_organization()
        print("The response of OrganizationApi->get_account_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_account_organization: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization of the acccount. |  -  |
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 
    key_id = 'key_id_example' # str | 

    try:
        # Get API Key
        api_response = api_instance.get_client_key(account_id, key_id)
        print("The response of OrganizationApi->get_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_client_key: %s\n" % e)
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # List API Keys
        api_response = api_instance.get_client_key_list(account_id)
        print("The response of OrganizationApi->get_client_key_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_client_key_list: %s\n" % e)
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 
    role_id = 'role_id_example' # str | 

    try:
        # Get Role
        api_response = api_instance.get_role(account_id, role_id)
        print("The response of OrganizationApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_role: %s\n" % e)
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # List Roles
        api_response = api_instance.get_roles_for_account(account_id)
        print("The response of OrganizationApi->get_roles_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_roles_for_account: %s\n" % e)
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

# **get_user**
> UserResponse get_user(account_id, user_id)

Get User

Get a specific user for a particular organization

### Example

```python
import time
import os
import katanemo_sdk
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Get User
        api_response = api_instance.get_user(account_id, user_id)
        print("The response of OrganizationApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | user belonging to provided account ID |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_for_account**
> List[UserResponse] get_users_for_account(account_id)

List Users

Returns a list of all users belonging to provided organization ID

### Example

```python
import time
import os
import katanemo_sdk
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # List Users
        api_response = api_instance.get_users_for_account(account_id)
        print("The response of OrganizationApi->get_users_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_users_for_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**List[UserResponse]**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | users belonging to provided account ID |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_info**
> update_account_info(account_id, update_organization_request)

Update Organization

Returns status code for successful or failed update.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.update_organization_request import UpdateOrganizationRequest
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 
    update_organization_request = katanemo_sdk.UpdateOrganizationRequest() # UpdateOrganizationRequest | Update account object

    try:
        # Update Organization
        api_instance.update_account_info(account_id, update_organization_request)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_account_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **update_organization_request** | [**UpdateOrganizationRequest**](UpdateOrganizationRequest.md)| Update account object | 

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
**200** | Successfully updated organization |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 
    role_id = 'role_id_example' # str | 
    role_request = katanemo_sdk.RoleRequest() # RoleRequest | Role object that is being updated.

    try:
        # Update Role
        api_response = api_instance.update_role(account_id, role_id, role_request)
        print("The response of OrganizationApi->update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_role: %s\n" % e)
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

# **update_user**
> UserResponse update_user(user_id, account_id, user_request)

Update user

Updates a User account

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.user_request import UserRequest
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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    user_id = 'user_id_example' # str | 
    account_id = 'account_id_example' # str | 
    user_request = katanemo_sdk.UserRequest() # UserRequest | User information

    try:
        # Update user
        api_response = api_instance.update_user(user_id, account_id, user_request)
        print("The response of OrganizationApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **account_id** | **str**|  | 
 **user_request** | [**UserRequest**](UserRequest.md)| User information | 

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
**200** | User |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_account_domain**
> verify_account_domain(account_id)

Verify Domain

Triggers the domain verification flow. If TXT record is created and has the correct verification code, the domain is verified.

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
    api_instance = katanemo_sdk.OrganizationApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Verify Domain
        api_instance.verify_account_domain(account_id)
    except Exception as e:
        print("Exception when calling OrganizationApi->verify_account_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

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
**200** | Domain verified |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

