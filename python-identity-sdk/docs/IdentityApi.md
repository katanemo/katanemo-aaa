# katanemo_identity.IdentityApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_key**](IdentityApi.md#create_client_key) | **POST** /org/{accountId}/keys | Create API Key
[**create_user_for_account**](IdentityApi.md#create_user_for_account) | **POST** /org/{accountId}/user | Invite User
[**delete_client_key**](IdentityApi.md#delete_client_key) | **DELETE** /org/{accountId}/key/{keyId} | Delete API Key
[**get_client_key**](IdentityApi.md#get_client_key) | **GET** /org/{accountId}/key/{keyId} | Get API Key
[**get_client_key_list**](IdentityApi.md#get_client_key_list) | **GET** /org/{accountId}/keys | List API Keys
[**get_user**](IdentityApi.md#get_user) | **GET** /org/{accountId}/user/{userId} | Get User
[**get_users_for_account**](IdentityApi.md#get_users_for_account) | **GET** /org/{accountId}/user | List Users
[**update_user**](IdentityApi.md#update_user) | **PUT** /org/{accountId}/user/{userId} | Update user


# **create_client_key**
> ClientKeyResponse create_client_key(account_id, client_key_request)

Create API Key

Creates a new client key for accessing a developers APIs

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.client_key_request import ClientKeyRequest
from katanemo_identity.models.client_key_response import ClientKeyResponse
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
    api_instance = katanemo_identity.IdentityApi(api_client)
    account_id = 'account_id_example' # str | 
    client_key_request = katanemo_identity.ClientKeyRequest() # ClientKeyRequest | 

    try:
        # Create API Key
        api_response = api_instance.create_client_key(account_id, client_key_request)
        print("The response of IdentityApi->create_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->create_client_key: %s\n" % e)
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

# **create_user_for_account**
> UserResponse create_user_for_account(account_id, user_request)

Invite User

Creates a new User and triggers an email verification workflow, followed by set-password

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.user_request import UserRequest
from katanemo_identity.models.user_response import UserResponse
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
    api_instance = katanemo_identity.IdentityApi(api_client)
    account_id = 'account_id_example' # str | 
    user_request = katanemo_identity.UserRequest() # UserRequest | User information

    try:
        # Invite User
        api_response = api_instance.create_user_for_account(account_id, user_request)
        print("The response of IdentityApi->create_user_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->create_user_for_account: %s\n" % e)
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
    api_instance = katanemo_identity.IdentityApi(api_client)
    account_id = 'account_id_example' # str | 
    key_id = 'key_id_example' # str | 

    try:
        # Delete API Key
        api_response = api_instance.delete_client_key(account_id, key_id)
        print("The response of IdentityApi->delete_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->delete_client_key: %s\n" % e)
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
import katanemo_identity
from katanemo_identity.models.client_key_object import ClientKeyObject
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
    api_instance = katanemo_identity.IdentityApi(api_client)
    account_id = 'account_id_example' # str | 
    key_id = 'key_id_example' # str | 

    try:
        # Get API Key
        api_response = api_instance.get_client_key(account_id, key_id)
        print("The response of IdentityApi->get_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->get_client_key: %s\n" % e)
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
import katanemo_identity
from katanemo_identity.models.client_key_object import ClientKeyObject
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
    api_instance = katanemo_identity.IdentityApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # List API Keys
        api_response = api_instance.get_client_key_list(account_id)
        print("The response of IdentityApi->get_client_key_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->get_client_key_list: %s\n" % e)
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

# **get_user**
> UserResponse get_user(account_id, user_id)

Get User

Get a specific user for a particular organization

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.user_response import UserResponse
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
    api_instance = katanemo_identity.IdentityApi(api_client)
    account_id = 'account_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Get User
        api_response = api_instance.get_user(account_id, user_id)
        print("The response of IdentityApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->get_user: %s\n" % e)
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
import katanemo_identity
from katanemo_identity.models.user_response import UserResponse
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
    api_instance = katanemo_identity.IdentityApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # List Users
        api_response = api_instance.get_users_for_account(account_id)
        print("The response of IdentityApi->get_users_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->get_users_for_account: %s\n" % e)
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

# **update_user**
> UserResponse update_user(user_id, account_id, user_request)

Update user

Updates a User account

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.user_request import UserRequest
from katanemo_identity.models.user_response import UserResponse
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
    api_instance = katanemo_identity.IdentityApi(api_client)
    user_id = 'user_id_example' # str | 
    account_id = 'account_id_example' # str | 
    user_request = katanemo_identity.UserRequest() # UserRequest | User information

    try:
        # Update user
        api_response = api_instance.update_user(user_id, account_id, user_request)
        print("The response of IdentityApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->update_user: %s\n" % e)
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

