# katanemo_sdk.DefaultApi

All URIs are relative to *https://api.us-west-2.katanemo.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_role_to_principal**](DefaultApi.md#assign_role_to_principal) | **POST** /assignrole | Assign role to an identity principal
[**assume_role**](DefaultApi.md#assume_role) | **POST** /assumeRole | Creates a token with requested roleId
[**confirm_user**](DefaultApi.md#confirm_user) | **GET** /confirmUser/{confirmationCode} | Confirm that the user belongs to the organization (email) they signed-up with. Used by Katanemo to verify developers signing-up for its 3xA service and for service developers on-boarding their customers (subscribers)
[**create_client_key**](DefaultApi.md#create_client_key) | **POST** /org/{accountId}/keys | Creates a new client key
[**create_oidcc_onnection**](DefaultApi.md#create_oidcc_onnection) | **POST** /org/{accountId}/sso-connections/oidc | Creates a new OIDC connection
[**create_role**](DefaultApi.md#create_role) | **POST** /org/{accountId}/role | Creates a new Role
[**create_saml_connection**](DefaultApi.md#create_saml_connection) | **POST** /org/{accountId}/sso-connections/saml | Creates a new SAML connection
[**create_saml_connection_mapping**](DefaultApi.md#create_saml_connection_mapping) | **POST** /org/{accountId}/sso-connections/saml/{connectionId}/mapAttributeToRoles | Creates a new attribute mapping for a SAML connection
[**create_service**](DefaultApi.md#create_service) | **POST** /service | Create a Katanemo Service object.
[**create_tags**](DefaultApi.md#create_tags) | **POST** /service/{serviceId}/tags | Add tags (key/value pair) to a particular resource that is created for a service against an organization account id
[**create_user_for_account**](DefaultApi.md#create_user_for_account) | **POST** /org/{accountId}/user | Creates a new User account tied to the specified organization
[**delete_client_key**](DefaultApi.md#delete_client_key) | **DELETE** /org/{accountId}/key/{keyId} | delete a client key
[**delete_oidc_connection**](DefaultApi.md#delete_oidc_connection) | **DELETE** /org/{accountId}/sso-connections/oidc/{connectionId} | Deletes an OIDC connection
[**delete_service**](DefaultApi.md#delete_service) | **DELETE** /service/{serviceId} | Deletes a service with service ID. Note the delete operation is a \&quot;soft\&quot; delete where by organizations can&#39;t access your service. Requires bearer token authorization.
[**get_account_info**](DefaultApi.md#get_account_info) | **GET** /org/{accountId} | Returns an object with information regarding an account
[**get_account_organization**](DefaultApi.md#get_account_organization) | **GET** /org | Returns an object with information regarding an account which is present in the token
[**get_audit_logs**](DefaultApi.md#get_audit_logs) | **GET** /audit-logs/service/{serviceId}/account/{accountId} | Returns list of log entries for a service and account
[**get_client_key**](DefaultApi.md#get_client_key) | **GET** /org/{accountId}/key/{keyId} | Get details of client key
[**get_client_key_list**](DefaultApi.md#get_client_key_list) | **GET** /org/{accountId}/keys | Get list of all client keys
[**get_default_service**](DefaultApi.md#get_default_service) | **GET** /service/3xA | Get details about Katanemo&#39;s AAA SaaS service. Katanemo is powered by Katanemo, and our 3xA service uses the same core identity and authorization capabilities that we offer SaaS (API) developers
[**get_developer_public_keys**](DefaultApi.md#get_developer_public_keys) | **GET** /service/{serviceId}/.well-known/jwks.json | Gets public key that can be used to verify jwt token issued by Katanemo. This API does not require bearer authorizationn if service is public
[**get_healthz**](DefaultApi.md#get_healthz) | **GET** /healthz | Returns service health
[**get_o_auth_token**](DefaultApi.md#get_o_auth_token) | **POST** /oauth/token | get token for client id / secret / code
[**get_oidc_connection**](DefaultApi.md#get_oidc_connection) | **GET** /org/{accountId}/sso-connections/oidc/{connectionId} | Retrieves an OIDC connection
[**get_oidc_connections_for_account**](DefaultApi.md#get_oidc_connections_for_account) | **GET** /org/{accountId}/sso-connections/oidc | Returns a list of all OIDC connections belonging to provided account ID
[**get_password_policy**](DefaultApi.md#get_password_policy) | **GET** /set-password/{serviceId} | Gets the password policy (length, characters, etc), to help the user set the correct password
[**get_role**](DefaultApi.md#get_role) | **GET** /org/{accountId}/role/{roleId} | Gets a role
[**get_roles_for_account**](DefaultApi.md#get_roles_for_account) | **GET** /org/{accountId}/role | Returns a list of all roles belonging to provided account ID
[**get_roles_for_service**](DefaultApi.md#get_roles_for_service) | **GET** /arc/{serviceId}/role | 
[**get_saml_connection**](DefaultApi.md#get_saml_connection) | **GET** /org/{accountId}/sso-connections/saml/{connectionId} | Retreive a SAML connection
[**get_saml_connections_for_account**](DefaultApi.md#get_saml_connections_for_account) | **GET** /org/{accountId}/sso-connections/saml | Returns a list of all SAML connections belonging to provided account ID
[**get_service**](DefaultApi.md#get_service) | **GET** /service/{serviceId} | Gets a service with service ID
[**get_short_term_token**](DefaultApi.md#get_short_term_token) | **POST** /token | Returns a short-lived token for client key/secret pair. Tokens contain claims that identify what a principal can or cannot do.
[**get_tags_for_resource**](DefaultApi.md#get_tags_for_resource) | **GET** /service/{serviceId}/tags | Gets tags for a particular resource
[**get_tags_for_service**](DefaultApi.md#get_tags_for_service) | **GET** /arc/{serviceId}/tags | 
[**get_user**](DefaultApi.md#get_user) | **GET** /org/{accountId}/user/{userId} | 
[**get_users_for_account**](DefaultApi.md#get_users_for_account) | **GET** /org/{accountId}/user | Returns a list of all users belonging to provided account ID
[**init_arc_client**](DefaultApi.md#init_arc_client) | **GET** /arc/{serviceId}/init | 
[**list_services_by_developer**](DefaultApi.md#list_services_by_developer) | **GET** /service | List services that belong to a particular developer. Requires bearer token authorization
[**login**](DefaultApi.md#login) | **POST** /login/{serviceId} | Login to any katanemo service with email and password
[**login_init**](DefaultApi.md#login_init) | **POST** /login-init/{serviceId} | Login-init helps developers determine if the user should be presented a SAML/SSO workflow or a user/password sign-in experience.
[**o_idc_login_trigger**](DefaultApi.md#o_idc_login_trigger) | **GET** /org/{accountId}/sso-connections/oidc/{connectionId}/login-trigger | Triggers okta signin flow
[**oidc_sso_call_back**](DefaultApi.md#oidc_sso_call_back) | **GET** /org/{accountId}/sso-connections/oidc/{connectionId}/sso-callback | Handle OIDC SSO login callback
[**s_aml_login_trigger**](DefaultApi.md#s_aml_login_trigger) | **GET** /org/{accountId}/sso-connections/saml/{connectionId}/login-trigger | Triggers SAML SSO signin flow
[**saml_sso_call_back**](DefaultApi.md#saml_sso_call_back) | **POST** /org/{accountId}/sso-connections/saml/{connectionId}/sso-callback/saml/acs | Handle SAML login callback with SAML assertion. It can be passed as query parameter or payload.
[**service_signup**](DefaultApi.md#service_signup) | **POST** /sign-up/{serviceId} | Onborad customers to a particular SaaS service managed by Katanemo
[**set_password**](DefaultApi.md#set_password) | **POST** /set-password/{serviceId} | Set password after user verification.
[**update_oidc_connection**](DefaultApi.md#update_oidc_connection) | **PUT** /org/{accountId}/sso-connections/oidc/{connectionId} | Updates a OIDC connection
[**update_role**](DefaultApi.md#update_role) | **PUT** /org/{accountId}/role/{roleId} | Updates role
[**update_saml_connection**](DefaultApi.md#update_saml_connection) | **PUT** /org/{accountId}/sso-connections/saml/{connectionId} | Updates a SAML connection
[**update_service**](DefaultApi.md#update_service) | **PUT** /service/{serviceId} | Update a Service. Requires bearer token authorization
[**update_user**](DefaultApi.md#update_user) | **PUT** /org/{accountId}/user/{userId} | Updates a user


# **assign_role_to_principal**
> User assign_role_to_principal(assign_role_obj)

Assign role to an identity principal

Assign role to an identity principal

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.assign_role_obj import AssignRoleObj
from katanemo_sdk.models.user import User
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    assign_role_obj = katanemo_sdk.AssignRoleObj() # AssignRoleObj | Role assignment

    try:
        # Assign role to an identity principal
        api_response = api_instance.assign_role_to_principal(assign_role_obj)
        print("The response of DefaultApi->assign_role_to_principal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->assign_role_to_principal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_role_obj** | [**AssignRoleObj**](AssignRoleObj.md)| Role assignment | 

### Return type

[**User**](User.md)

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

Creates a token with requested roleId

Creates a token with requested roleId

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.assume_role_obj import AssumeRoleObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    assume_role_obj = katanemo_sdk.AssumeRoleObj() # AssumeRoleObj | Role assignment

    try:
        # Creates a token with requested roleId
        api_response = api_instance.assume_role(assume_role_obj)
        print("The response of DefaultApi->assume_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->assume_role: %s\n" % e)
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

# **confirm_user**
> UserConfirmationResponse confirm_user(confirmation_code)

Confirm that the user belongs to the organization (email) they signed-up with. Used by Katanemo to verify developers signing-up for its 3xA service and for service developers on-boarding their customers (subscribers)

Verify user in the signup flow (clicking email link), serviceId indicates user is being confirmed for.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.user_confirmation_response import UserConfirmationResponse
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    confirmation_code = 'confirmation_code_example' # str | 

    try:
        # Confirm that the user belongs to the organization (email) they signed-up with. Used by Katanemo to verify developers signing-up for its 3xA service and for service developers on-boarding their customers (subscribers)
        api_response = api_instance.confirm_user(confirmation_code)
        print("The response of DefaultApi->confirm_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->confirm_user: %s\n" % e)
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

# **create_client_key**
> ClientKeyResponse create_client_key(account_id, client_key_request)

Creates a new client key

Creates a new client key

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.client_key_request import ClientKeyRequest
from katanemo_sdk.models.client_key_response import ClientKeyResponse
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    client_key_request = katanemo_sdk.ClientKeyRequest() # ClientKeyRequest | 

    try:
        # Creates a new client key
        api_response = api_instance.create_client_key(account_id, client_key_request)
        print("The response of DefaultApi->create_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_client_key: %s\n" % e)
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

# **create_oidcc_onnection**
> OIDCObj create_oidcc_onnection(account_id, oidc_obj)

Creates a new OIDC connection

Creates a new OIDC connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.oidc_obj import OIDCObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    oidc_obj = katanemo_sdk.OIDCObj() # OIDCObj | ODIC connection attributes

    try:
        # Creates a new OIDC connection
        api_response = api_instance.create_oidcc_onnection(account_id, oidc_obj)
        print("The response of DefaultApi->create_oidcc_onnection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_oidcc_onnection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **oidc_obj** | [**OIDCObj**](OIDCObj.md)| ODIC connection attributes | 

### Return type

[**OIDCObj**](OIDCObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OIDCObj |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> Role create_role(account_id, role)

Creates a new Role

Creates a new Role

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.role import Role
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    role = katanemo_sdk.Role() # Role | Role to add to the system

    try:
        # Creates a new Role
        api_response = api_instance.create_role(account_id, role)
        print("The response of DefaultApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **role** | [**Role**](Role.md)| Role to add to the system | 

### Return type

[**Role**](Role.md)

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

# **create_saml_connection**
> SAMLObj create_saml_connection(account_id, saml_obj)

Creates a new SAML connection

Creates a new SAML connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.saml_obj import SAMLObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    saml_obj = katanemo_sdk.SAMLObj() # SAMLObj | SAML connection attributes

    try:
        # Creates a new SAML connection
        api_response = api_instance.create_saml_connection(account_id, saml_obj)
        print("The response of DefaultApi->create_saml_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_saml_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **saml_obj** | [**SAMLObj**](SAMLObj.md)| SAML connection attributes | 

### Return type

[**SAMLObj**](SAMLObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SAMLObj |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_saml_connection_mapping**
> SAMLObj create_saml_connection_mapping(account_id, connection_id, attribute_role_mapping)

Creates a new attribute mapping for a SAML connection

Creates a new attribute mapping for a SAML connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.attribute_role_mapping import AttributeRoleMapping
from katanemo_sdk.models.saml_obj import SAMLObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 
    attribute_role_mapping = katanemo_sdk.AttributeRoleMapping() # AttributeRoleMapping | SAML user attributes to role mapping

    try:
        # Creates a new attribute mapping for a SAML connection
        api_response = api_instance.create_saml_connection_mapping(account_id, connection_id, attribute_role_mapping)
        print("The response of DefaultApi->create_saml_connection_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_saml_connection_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **connection_id** | **str**|  | 
 **attribute_role_mapping** | [**AttributeRoleMapping**](AttributeRoleMapping.md)| SAML user attributes to role mapping | 

### Return type

[**SAMLObj**](SAMLObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SAMLObj |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service**
> ServiceResponseObj create_service(name, description, redirect_url, api_spec_file, display_name=display_name, logo_url=logo_url, terms_url=terms_url, privacy_url=privacy_url, docs_url=docs_url)

Create a Katanemo Service object.

Create a Service in Katanemo. Once a service is created Katanemo powers rich enterprise identity and authorization capabilities on behalf of SaaS (API) Developers

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.service_response_obj import ServiceResponseObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    name = 'name_example' # str | Service Name
    description = 'description_example' # str | Service Description
    redirect_url = 'redirect_url_example' # str | Redirect URL after a successful login.
    api_spec_file = None # bytearray | openapi service json or yaml file
    display_name = 'display_name_example' # str | Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages (optional)
    logo_url = 'logo_url_example' # str | The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages (optional)
    terms_url = 'terms_url_example' # str | The URL for the terms of the service (optional)
    privacy_url = 'privacy_url_example' # str | The URL for the privacy of the service (optional)
    docs_url = 'docs_url_example' # str | The URL for the documentatio of the service (optional)

    try:
        # Create a Katanemo Service object.
        api_response = api_instance.create_service(name, description, redirect_url, api_spec_file, display_name=display_name, logo_url=logo_url, terms_url=terms_url, privacy_url=privacy_url, docs_url=docs_url)
        print("The response of DefaultApi->create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Service Name | 
 **description** | **str**| Service Description | 
 **redirect_url** | **str**| Redirect URL after a successful login. | 
 **api_spec_file** | **bytearray**| openapi service json or yaml file | 
 **display_name** | **str**| Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
 **logo_url** | **str**| The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
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

Add tags (key/value pair) to a particular resource that is created for a service against an organization account id

Add tags (key/value pair) to a particular resource that is created for a service against an organization account id.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.tags import Tags
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 
    tags = katanemo_sdk.Tags() # Tags | Tags and resource id

    try:
        # Add tags (key/value pair) to a particular resource that is created for a service against an organization account id
        api_response = api_instance.create_tags(service_id, tags)
        print("The response of DefaultApi->create_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_tags: %s\n" % e)
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

# **create_user_for_account**
> User create_user_for_account(account_id, user)

Creates a new User account tied to the specified organization

Creates a new User and triggers an email verification workflow, followed by set-password

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.user import User
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    user = katanemo_sdk.User() # User | User information

    try:
        # Creates a new User account tied to the specified organization
        api_response = api_instance.create_user_for_account(account_id, user)
        print("The response of DefaultApi->create_user_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_user_for_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **user** | [**User**](User.md)| User information | 

### Return type

[**User**](User.md)

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

delete a client key

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    key_id = 'key_id_example' # str | 

    try:
        # delete a client key
        api_response = api_instance.delete_client_key(account_id, key_id)
        print("The response of DefaultApi->delete_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_client_key: %s\n" % e)
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

# **delete_oidc_connection**
> delete_oidc_connection(account_id, connection_id)

Deletes an OIDC connection

Deletes an OIDC connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 

    try:
        # Deletes an OIDC connection
        api_instance.delete_oidc_connection(account_id, connection_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_oidc_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **connection_id** | **str**|  | 

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
**200** | Deletion successful. |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service**
> delete_service(service_id)

Deletes a service with service ID. Note the delete operation is a \"soft\" delete where by organizations can't access your service. Requires bearer token authorization.

Deletes a service. Note the delete operation is a \"soft\" delete where by organizations can't access your service. Requires bearer token authorization.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 

    try:
        # Deletes a service with service ID. Note the delete operation is a \"soft\" delete where by organizations can't access your service. Requires bearer token authorization.
        api_instance.delete_service(service_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_service: %s\n" % e)
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

# **get_account_info**
> Organization get_account_info(account_id)

Returns an object with information regarding an account

Returns an object with information regarding an account

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.organization import Organization
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Returns an object with information regarding an account
        api_response = api_instance.get_account_info(account_id)
        print("The response of DefaultApi->get_account_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_account_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**Organization**](Organization.md)

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
> Organization get_account_organization()

Returns an object with information regarding an account which is present in the token

Returns an object with information regarding an account which is present in the token

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.organization import Organization
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)

    try:
        # Returns an object with information regarding an account which is present in the token
        api_response = api_instance.get_account_organization()
        print("The response of DefaultApi->get_account_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_account_organization: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Organization**](Organization.md)

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

# **get_audit_logs**
> List[AuditLogEntry] get_audit_logs(service_id, account_id, start_time, end_time)

Returns list of log entries for a service and account

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.audit_log_entry import AuditLogEntry
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 
    account_id = 'account_id_example' # str | 
    start_time = 'start_time_example' # str | Start time of log entries
    end_time = 'end_time_example' # str | End time of log entries

    try:
        # Returns list of log entries for a service and account
        api_response = api_instance.get_audit_logs(service_id, account_id, start_time, end_time)
        print("The response of DefaultApi->get_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_audit_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **account_id** | **str**|  | 
 **start_time** | **str**| Start time of log entries | 
 **end_time** | **str**| End time of log entries | 

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

# **get_client_key**
> ClientKeyObject get_client_key(account_id, key_id)

Get details of client key

Get details of client key

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.client_key_object import ClientKeyObject
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    key_id = 'key_id_example' # str | 

    try:
        # Get details of client key
        api_response = api_instance.get_client_key(account_id, key_id)
        print("The response of DefaultApi->get_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_client_key: %s\n" % e)
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

Get list of all client keys

Get list of all client keys

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.client_key_object import ClientKeyObject
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Get list of all client keys
        api_response = api_instance.get_client_key_list(account_id)
        print("The response of DefaultApi->get_client_key_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_client_key_list: %s\n" % e)
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

# **get_default_service**
> ServiceResponseObj get_default_service()

Get details about Katanemo's AAA SaaS service. Katanemo is powered by Katanemo, and our 3xA service uses the same core identity and authorization capabilities that we offer SaaS (API) developers

Gets Katanemo AAA service object

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.service_response_obj import ServiceResponseObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)

    try:
        # Get details about Katanemo's AAA SaaS service. Katanemo is powered by Katanemo, and our 3xA service uses the same core identity and authorization capabilities that we offer SaaS (API) developers
        api_response = api_instance.get_default_service()
        print("The response of DefaultApi->get_default_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_default_service: %s\n" % e)
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

Gets public key that can be used to verify jwt token issued by Katanemo. This API does not require bearer authorizationn if service is public

Gets public key that can be used to verify jwt token issued by Katanemo. This API does not require bearer authorization

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.get_developer_public_keys200_response import GetDeveloperPublicKeys200Response
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 

    try:
        # Gets public key that can be used to verify jwt token issued by Katanemo. This API does not require bearer authorizationn if service is public
        api_response = api_instance.get_developer_public_keys(service_id)
        print("The response of DefaultApi->get_developer_public_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_developer_public_keys: %s\n" % e)
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

# **get_healthz**
> str get_healthz()

Returns service health

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)

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

# **get_o_auth_token**
> OAuthTokenResponse get_o_auth_token(o_auth_token_request)

get token for client id / secret / code

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.o_auth_token_request import OAuthTokenRequest
from katanemo_sdk.models.o_auth_token_response import OAuthTokenResponse
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    o_auth_token_request = katanemo_sdk.OAuthTokenRequest() # OAuthTokenRequest | 

    try:
        # get token for client id / secret / code
        api_response = api_instance.get_o_auth_token(o_auth_token_request)
        print("The response of DefaultApi->get_o_auth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_o_auth_token: %s\n" % e)
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

# **get_oidc_connection**
> OIDCObj get_oidc_connection(account_id, connection_id)

Retrieves an OIDC connection

Retrieves an OIDC connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.oidc_obj import OIDCObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 

    try:
        # Retrieves an OIDC connection
        api_response = api_instance.get_oidc_connection(account_id, connection_id)
        print("The response of DefaultApi->get_oidc_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_oidc_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **connection_id** | **str**|  | 

### Return type

[**OIDCObj**](OIDCObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OIDCObj |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oidc_connections_for_account**
> List[OIDCObj] get_oidc_connections_for_account(account_id)

Returns a list of all OIDC connections belonging to provided account ID

Returns a list of all OIDC connections belonging to provided account ID

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.oidc_obj import OIDCObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Returns a list of all OIDC connections belonging to provided account ID
        api_response = api_instance.get_oidc_connections_for_account(account_id)
        print("The response of DefaultApi->get_oidc_connections_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_oidc_connections_for_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**List[OIDCObj]**](OIDCObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OIDC connections belonging to provided account ID |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_policy**
> PasswordPolicy get_password_policy(service_id)

Gets the password policy (length, characters, etc), to help the user set the correct password

Gets the password policy (length, characters, etc), to help the user set the correct password

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.password_policy import PasswordPolicy
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 

    try:
        # Gets the password policy (length, characters, etc), to help the user set the correct password
        api_response = api_instance.get_password_policy(service_id)
        print("The response of DefaultApi->get_password_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_password_policy: %s\n" % e)
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

# **get_role**
> Role get_role(account_id, role_id)

Gets a role

Gets a role

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.role import Role
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    role_id = 'role_id_example' # str | 

    try:
        # Gets a role
        api_response = api_instance.get_role(account_id, role_id)
        print("The response of DefaultApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

[**Role**](Role.md)

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
> List[Role] get_roles_for_account(account_id)

Returns a list of all roles belonging to provided account ID

Returns a list of all roles belonging to provided account ID

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.role import Role
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Returns a list of all roles belonging to provided account ID
        api_response = api_instance.get_roles_for_account(account_id)
        print("The response of DefaultApi->get_roles_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_roles_for_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**List[Role]**](Role.md)

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

# **get_roles_for_service**
> List[Role] get_roles_for_service(service_id, limit=limit)



### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.role import Role
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.get_roles_for_service(service_id, limit=limit)
        print("The response of DefaultApi->get_roles_for_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_roles_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**List[Role]**](Role.md)

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

# **get_saml_connection**
> SAMLObj get_saml_connection(account_id, connection_id)

Retreive a SAML connection

Retreive a SAML connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.saml_obj import SAMLObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 

    try:
        # Retreive a SAML connection
        api_response = api_instance.get_saml_connection(account_id, connection_id)
        print("The response of DefaultApi->get_saml_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_saml_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **connection_id** | **str**|  | 

### Return type

[**SAMLObj**](SAMLObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SAMLObj |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saml_connections_for_account**
> List[SAMLObj] get_saml_connections_for_account(account_id)

Returns a list of all SAML connections belonging to provided account ID

Returns a list of all SAML connections belonging to provided account ID

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.saml_obj import SAMLObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Returns a list of all SAML connections belonging to provided account ID
        api_response = api_instance.get_saml_connections_for_account(account_id)
        print("The response of DefaultApi->get_saml_connections_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_saml_connections_for_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**List[SAMLObj]**](SAMLObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SAML connections belonging to provided account ID |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> ServiceResponseObj get_service(service_id)

Gets a service with service ID

Gets a service. The principal token must be present in the bearer header to retrieve the service details, unless the service is public

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.service_response_obj import ServiceResponseObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 

    try:
        # Gets a service with service ID
        api_response = api_instance.get_service(service_id)
        print("The response of DefaultApi->get_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_service: %s\n" % e)
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

# **get_short_term_token**
> TokenResponse get_short_term_token(token_request)

Returns a short-lived token for client key/secret pair. Tokens contain claims that identify what a principal can or cannot do.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.token_request import TokenRequest
from katanemo_sdk.models.token_response import TokenResponse
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    token_request = katanemo_sdk.TokenRequest() # TokenRequest | 

    try:
        # Returns a short-lived token for client key/secret pair. Tokens contain claims that identify what a principal can or cannot do.
        api_response = api_instance.get_short_term_token(token_request)
        print("The response of DefaultApi->get_short_term_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_short_term_token: %s\n" % e)
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

Gets tags for a particular resource

Gets tags object associated with a resource

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.get_tags_request import GetTagsRequest
from katanemo_sdk.models.tags import Tags
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 
    get_tags_request = katanemo_sdk.GetTagsRequest() # GetTagsRequest | Tags and resource id

    try:
        # Gets tags for a particular resource
        api_response = api_instance.get_tags_for_resource(service_id, get_tags_request)
        print("The response of DefaultApi->get_tags_for_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tags_for_resource: %s\n" % e)
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

# **get_tags_for_service**
> List[Tags] get_tags_for_service(service_id, limit=limit)



### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.tags import Tags
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.get_tags_for_service(service_id, limit=limit)
        print("The response of DefaultApi->get_tags_for_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tags_for_service: %s\n" % e)
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

# **get_user**
> User get_user(account_id, user_id)



### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.user import User
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.get_user(account_id, user_id)
        print("The response of DefaultApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**User**](User.md)

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
> List[User] get_users_for_account(account_id)

Returns a list of all users belonging to provided account ID

Returns a list of all users belonging to provided account ID

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.user import User
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Returns a list of all users belonging to provided account ID
        api_response = api_instance.get_users_for_account(account_id)
        print("The response of DefaultApi->get_users_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_users_for_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**List[User]**](User.md)

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

# **init_arc_client**
> List[InitArcResponse] init_arc_client(service_id)



### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.init_arc_response import InitArcResponse
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 

    try:
        api_response = api_instance.init_arc_client(service_id)
        print("The response of DefaultApi->init_arc_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->init_arc_client: %s\n" % e)
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

# **list_services_by_developer**
> List[ServiceResponseObj] list_services_by_developer()

List services that belong to a particular developer. Requires bearer token authorization

List services that belong to a particular developer. Requires bearer token authorization

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.service_response_obj import ServiceResponseObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)

    try:
        # List services that belong to a particular developer. Requires bearer token authorization
        api_response = api_instance.list_services_by_developer()
        print("The response of DefaultApi->list_services_by_developer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_services_by_developer: %s\n" % e)
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

# **login**
> LoginToken login(service_id, login_with_password_request)

Login to any katanemo service with email and password

Login to any katanemo service. serviceId indicates service user is logging in to.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.login_token import LoginToken
from katanemo_sdk.models.login_with_password_request import LoginWithPasswordRequest
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 
    login_with_password_request = katanemo_sdk.LoginWithPasswordRequest() # LoginWithPasswordRequest | Login info of a user

    try:
        # Login to any katanemo service with email and password
        api_response = api_instance.login(service_id, login_with_password_request)
        print("The response of DefaultApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->login: %s\n" % e)
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

Login-init helps developers determine if the user should be presented a SAML/SSO workflow or a user/password sign-in experience.

Login-init helps developers determine if the user should be presented a SAML/SSO workflow or a user/password sign-in experience.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.initial_login_request import InitialLoginRequest
from katanemo_sdk.models.initial_login_response import InitialLoginResponse
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 
    initial_login_request = katanemo_sdk.InitialLoginRequest() # InitialLoginRequest | Login info (email) of the user

    try:
        # Login-init helps developers determine if the user should be presented a SAML/SSO workflow or a user/password sign-in experience.
        api_response = api_instance.login_init(service_id, initial_login_request)
        print("The response of DefaultApi->login_init:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->login_init: %s\n" % e)
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

# **o_idc_login_trigger**
> Error o_idc_login_trigger(connection_id, account_id)

Triggers okta signin flow

Triggers OIDC login for a particular connection. Account can have multiple OIDC connections. It redirects to the login URL corresponding to a particular connection.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.error import Error
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    connection_id = 'connection_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Triggers okta signin flow
        api_response = api_instance.o_idc_login_trigger(connection_id, account_id)
        print("The response of DefaultApi->o_idc_login_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->o_idc_login_trigger: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_sso_call_back**
> Error oidc_sso_call_back(account_id, connection_id, code, state)

Handle OIDC SSO login callback

Handles OIDC login callback

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.error import Error
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 
    code = 'code_example' # str | Authorization code returned by the OIDC provider
    state = 'state_example' # str | Authorization code returned by the OIDC provider

    try:
        # Handle OIDC SSO login callback
        api_response = api_instance.oidc_sso_call_back(account_id, connection_id, code, state)
        print("The response of DefaultApi->oidc_sso_call_back:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->oidc_sso_call_back: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **connection_id** | **str**|  | 
 **code** | **str**| Authorization code returned by the OIDC provider | 
 **state** | **str**| Authorization code returned by the OIDC provider | 

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to default page for developer after succesful login. |  * Location - Redirect URL of landing page after successful login. <br>  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_aml_login_trigger**
> Error s_aml_login_trigger(connection_id, account_id)

Triggers SAML SSO signin flow

Triggers SAML login for a particular connection. Account can have multiple SAML connections. It redirects to the login URL corresponding to a particular connection.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.error import Error
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    connection_id = 'connection_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Triggers SAML SSO signin flow
        api_response = api_instance.s_aml_login_trigger(connection_id, account_id)
        print("The response of DefaultApi->s_aml_login_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->s_aml_login_trigger: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **saml_sso_call_back**
> Error saml_sso_call_back(account_id, connection_id, saml_response=saml_response, saml_response2=saml_response2)

Handle SAML login callback with SAML assertion. It can be passed as query parameter or payload.

Handle SAML login callback with SAML assertion. It can be passed as query parameter or payload.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.error import Error
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 
    saml_response = 'saml_response_example' # str | SAML response returned by the SAML IDP (optional)
    saml_response2 = 'saml_response_example' # str | SAML response returned by the SAML IDP (optional)

    try:
        # Handle SAML login callback with SAML assertion. It can be passed as query parameter or payload.
        api_response = api_instance.saml_sso_call_back(account_id, connection_id, saml_response=saml_response, saml_response2=saml_response2)
        print("The response of DefaultApi->saml_sso_call_back:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->saml_sso_call_back: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **connection_id** | **str**|  | 
 **saml_response** | **str**| SAML response returned by the SAML IDP | [optional] 
 **saml_response2** | **str**| SAML response returned by the SAML IDP | [optional] 

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to default page for developer after succesful login. |  * Location - Redirect URL of landing page after successful login. <br>  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_signup**
> SignupResponse service_signup(service_id, signup_request)

Onborad customers to a particular SaaS service managed by Katanemo

Onborad customers to a particular SaaS service managed by Katanemo. Generates email verification workflows and creates an organization for the customer subscribing to this particular service

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.signup_request import SignupRequest
from katanemo_sdk.models.signup_response import SignupResponse
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 
    signup_request = katanemo_sdk.SignupRequest() # SignupRequest | Signup Info of the service developer or a service subscriber

    try:
        # Onborad customers to a particular SaaS service managed by Katanemo
        api_response = api_instance.service_signup(service_id, signup_request)
        print("The response of DefaultApi->service_signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->service_signup: %s\n" % e)
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

Set password after user verification.

Set password of user after verficiation for specific service.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.set_password_request import SetPasswordRequest
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 
    set_password_request = katanemo_sdk.SetPasswordRequest() # SetPasswordRequest | Set password info

    try:
        # Set password after user verification.
        api_instance.set_password(service_id, set_password_request)
    except Exception as e:
        print("Exception when calling DefaultApi->set_password: %s\n" % e)
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

# **update_oidc_connection**
> OIDCObj update_oidc_connection(account_id, connection_id, oidc_obj)

Updates a OIDC connection

Updates a OIDC connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.oidc_obj import OIDCObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 
    oidc_obj = katanemo_sdk.OIDCObj() # OIDCObj | OIDC connection attributes

    try:
        # Updates a OIDC connection
        api_response = api_instance.update_oidc_connection(account_id, connection_id, oidc_obj)
        print("The response of DefaultApi->update_oidc_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_oidc_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **connection_id** | **str**|  | 
 **oidc_obj** | [**OIDCObj**](OIDCObj.md)| OIDC connection attributes | 

### Return type

[**OIDCObj**](OIDCObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SAMLObj |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> Role update_role(account_id, role_id, role)

Updates role

Update role

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.role import Role
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    role_id = 'role_id_example' # str | 
    role = katanemo_sdk.Role() # Role | Role object that is being updated.

    try:
        # Updates role
        api_response = api_instance.update_role(account_id, role_id, role)
        print("The response of DefaultApi->update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **role_id** | **str**|  | 
 **role** | [**Role**](Role.md)| Role object that is being updated. | 

### Return type

[**Role**](Role.md)

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

# **update_saml_connection**
> SAMLObj update_saml_connection(account_id, connection_id, saml_obj)

Updates a SAML connection

Updates a SAML connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.saml_obj import SAMLObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 
    saml_obj = katanemo_sdk.SAMLObj() # SAMLObj | SAML connection attributes

    try:
        # Updates a SAML connection
        api_response = api_instance.update_saml_connection(account_id, connection_id, saml_obj)
        print("The response of DefaultApi->update_saml_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_saml_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **connection_id** | **str**|  | 
 **saml_obj** | [**SAMLObj**](SAMLObj.md)| SAML connection attributes | 

### Return type

[**SAMLObj**](SAMLObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SAMLObj |  -  |
**400** | Bad Request Exception |  -  |
**401** | Unauthorized Exception |  -  |
**409** | Conflict Exception |  -  |
**429** | Too Many Requests Exception |  -  |
**500** | Internal Server Error |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service**
> ServiceResponseObj update_service(service_id, name=name, description=description, redirect_url=redirect_url, api_spec_file=api_spec_file, display_name=display_name, logo_url=logo_url, terms_url=terms_url, privacy_url=privacy_url, docs_url=docs_url)

Update a Service. Requires bearer token authorization

Update Service. Requires bearer token authorization

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.service_response_obj import ServiceResponseObj
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    service_id = 'service_id_example' # str | 
    name = 'name_example' # str | Service Name (optional)
    description = 'description_example' # str | Service Description (optional)
    redirect_url = 'redirect_url_example' # str | Redirect URL after a successful login. (optional)
    api_spec_file = None # bytearray | openapi service json or yaml file (optional)
    display_name = 'display_name_example' # str | Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages (optional)
    logo_url = 'logo_url_example' # str | The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages (optional)
    terms_url = 'terms_url_example' # str | The URL for the terms of the service (optional)
    privacy_url = 'privacy_url_example' # str | The URL for the privacy of the service (optional)
    docs_url = 'docs_url_example' # str | The URL for the documentatio of the service (optional)

    try:
        # Update a Service. Requires bearer token authorization
        api_response = api_instance.update_service(service_id, name=name, description=description, redirect_url=redirect_url, api_spec_file=api_spec_file, display_name=display_name, logo_url=logo_url, terms_url=terms_url, privacy_url=privacy_url, docs_url=docs_url)
        print("The response of DefaultApi->update_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **name** | **str**| Service Name | [optional] 
 **description** | **str**| Service Description | [optional] 
 **redirect_url** | **str**| Redirect URL after a successful login. | [optional] 
 **api_spec_file** | **bytearray**| openapi service json or yaml file | [optional] 
 **display_name** | **str**| Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
 **logo_url** | **str**| The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
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

# **update_user**
> User update_user(user_id, account_id, user)

Updates a user

Updates a User account

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.user import User
from katanemo_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.us-west-2.katanemo.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.us-west-2.katanemo.dev"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 
    account_id = 'account_id_example' # str | 
    user = katanemo_sdk.User() # User | User information

    try:
        # Updates a user
        api_response = api_instance.update_user(user_id, account_id, user)
        print("The response of DefaultApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **account_id** | **str**|  | 
 **user** | [**User**](User.md)| User information | 

### Return type

[**User**](User.md)

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

