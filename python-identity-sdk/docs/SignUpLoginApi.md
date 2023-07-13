# katanemo_identity.SignUpLoginApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_user**](SignUpLoginApi.md#confirm_user) | **GET** /confirmUser/{confirmationCode} | Confirm User
[**get_password_policy**](SignUpLoginApi.md#get_password_policy) | **GET** /set-password/{serviceId} | Get password policy
[**login**](SignUpLoginApi.md#login) | **POST** /login/{serviceId} | Login (Password)
[**login_init**](SignUpLoginApi.md#login_init) | **POST** /login-init/{serviceId} | Login-init (SSO vs. Password)
[**service_signup**](SignUpLoginApi.md#service_signup) | **POST** /sign-up/{serviceId} | Sign-up for Service
[**set_password**](SignUpLoginApi.md#set_password) | **POST** /set-password/{serviceId} | Set Password


# **confirm_user**
> UserConfirmationResponse confirm_user(confirmation_code)

Confirm User

Confirm that the user belongs to the organization (email) they signed-up with. Used by Katanemo to verify developers signing-up for its 3xA service and for service developers on-boarding their customers (subscribers)

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.user_confirmation_response import UserConfirmationResponse
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
    api_instance = katanemo_identity.SignUpLoginApi(api_client)
    confirmation_code = 'confirmation_code_example' # str | 

    try:
        # Confirm User
        api_response = api_instance.confirm_user(confirmation_code)
        print("The response of SignUpLoginApi->confirm_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignUpLoginApi->confirm_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirmation_code** | **str**|  | 

### Return type

[**UserConfirmationResponse**](UserConfirmationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The first user (email) has been subscribed to a particular service and an organization id has been created |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_policy**
> PasswordPolicy get_password_policy(service_id)

Get password policy

Gets the password policy (length, characters, etc), to help the user set the correct password

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.password_policy import PasswordPolicy
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
    api_instance = katanemo_identity.SignUpLoginApi(api_client)
    service_id = 'service_id_example' # str | 

    try:
        # Get password policy
        api_response = api_instance.get_password_policy(service_id)
        print("The response of SignUpLoginApi->get_password_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignUpLoginApi->get_password_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**PasswordPolicy**](PasswordPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns the password stregnth needed to successful set password |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> LoginToken login(service_id, login_with_password_request)

Login (Password)

Login to any katanemo service. serviceId indicates service user is logging in to.

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.login_token import LoginToken
from katanemo_identity.models.login_with_password_request import LoginWithPasswordRequest
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
    api_instance = katanemo_identity.SignUpLoginApi(api_client)
    service_id = 'service_id_example' # str | 
    login_with_password_request = katanemo_identity.LoginWithPasswordRequest() # LoginWithPasswordRequest | Login info of a user

    try:
        # Login (Password)
        api_response = api_instance.login(service_id, login_with_password_request)
        print("The response of SignUpLoginApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignUpLoginApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **login_with_password_request** | [**LoginWithPasswordRequest**](LoginWithPasswordRequest.md)| Login info of a user | 

### Return type

[**LoginToken**](LoginToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to default page for developer after succesful login. |  * Location - Redirect URL of landing page after successful login. <br>  |
**200** | Returns login token in a response object if skipRedirect is set to true. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_init**
> InitialLoginResponse login_init(service_id, initial_login_request)

Login-init (SSO vs. Password)

Login-init helps developers determine if the user should be presented a SAML/SSO workflow or a user/password sign-in experience.

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.initial_login_request import InitialLoginRequest
from katanemo_identity.models.initial_login_response import InitialLoginResponse
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
    api_instance = katanemo_identity.SignUpLoginApi(api_client)
    service_id = 'service_id_example' # str | 
    initial_login_request = katanemo_identity.InitialLoginRequest() # InitialLoginRequest | Login info (email) of the user

    try:
        # Login-init (SSO vs. Password)
        api_response = api_instance.login_init(service_id, initial_login_request)
        print("The response of SignUpLoginApi->login_init:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignUpLoginApi->login_init: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **initial_login_request** | [**InitialLoginRequest**](InitialLoginRequest.md)| Login info (email) of the user | 

### Return type

[**InitialLoginResponse**](InitialLoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This API is used to determine if the user should login via an email/password combination or if the UI should redirect the user to the Idp for SSO |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_signup**
> SignupResponse service_signup(service_id, signup_request)

Sign-up for Service

Onborad customers to a particular SaaS service managed by Katanemo. Generates email verification workflows and creates an organization for the customer subscribing to this particular service

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.signup_request import SignupRequest
from katanemo_identity.models.signup_response import SignupResponse
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
    api_instance = katanemo_identity.SignUpLoginApi(api_client)
    service_id = 'service_id_example' # str | 
    signup_request = katanemo_identity.SignupRequest() # SignupRequest | Signup Info of the service developer or a service subscriber

    try:
        # Sign-up for Service
        api_response = api_instance.service_signup(service_id, signup_request)
        print("The response of SignUpLoginApi->service_signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignUpLoginApi->service_signup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **signup_request** | [**SignupRequest**](SignupRequest.md)| Signup Info of the service developer or a service subscriber | 

### Return type

[**SignupResponse**](SignupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signup is successful. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_password**
> set_password(service_id, set_password_request)

Set Password

Allows the user to set password after verficiation via a session token.

### Example

```python
import time
import os
import katanemo_identity
from katanemo_identity.models.set_password_request import SetPasswordRequest
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
    api_instance = katanemo_identity.SignUpLoginApi(api_client)
    service_id = 'service_id_example' # str | 
    set_password_request = katanemo_identity.SetPasswordRequest() # SetPasswordRequest | Set password info

    try:
        # Set Password
        api_instance.set_password(service_id, set_password_request)
    except Exception as e:
        print("Exception when calling SignUpLoginApi->set_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **set_password_request** | [**SetPasswordRequest**](SetPasswordRequest.md)| Set password info | 

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
**200** | Settting pasword for user is successful. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

