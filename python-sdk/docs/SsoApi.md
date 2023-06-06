# katanemo_sdk.SsoApi

All URIs are relative to *https://api.katanemo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_oidcc_onnection**](SsoApi.md#create_oidcc_onnection) | **POST** /org/{accountId}/sso-connections/oidc | Creates OIDC connection
[**create_saml_connection**](SsoApi.md#create_saml_connection) | **POST** /org/{accountId}/sso-connections/saml | Creates SAML connection
[**create_saml_connection_mapping**](SsoApi.md#create_saml_connection_mapping) | **POST** /org/{accountId}/sso-connections/saml/{connectionId}/mapAttributeToRoles | MAP SAML Attributes
[**delete_oidc_connection**](SsoApi.md#delete_oidc_connection) | **DELETE** /org/{accountId}/sso-connections/oidc/{connectionId} | Delete OIDC connection
[**get_oidc_connection**](SsoApi.md#get_oidc_connection) | **GET** /org/{accountId}/sso-connections/oidc/{connectionId} | Get OIDC connection
[**get_oidc_connections_for_account**](SsoApi.md#get_oidc_connections_for_account) | **GET** /org/{accountId}/sso-connections/oidc | List OIDC Connections
[**get_saml_connection**](SsoApi.md#get_saml_connection) | **GET** /org/{accountId}/sso-connections/saml/{connectionId} | Get connection
[**get_saml_connections_for_account**](SsoApi.md#get_saml_connections_for_account) | **GET** /org/{accountId}/sso-connections/saml | List SAML Connections
[**o_idc_login_trigger**](SsoApi.md#o_idc_login_trigger) | **GET** /org/{accountId}/sso-connections/oidc/{connectionId}/login-trigger | Trigger OIDC SSO
[**oidc_sso_call_back**](SsoApi.md#oidc_sso_call_back) | **GET** /org/{accountId}/sso-connections/oidc/{connectionId}/sso-callback | OIDC Callback
[**s_aml_login_trigger**](SsoApi.md#s_aml_login_trigger) | **GET** /org/{accountId}/sso-connections/saml/{connectionId}/login-trigger | Triggers SAML SSO
[**saml_sso_call_back**](SsoApi.md#saml_sso_call_back) | **POST** /org/{accountId}/sso-connections/saml/{connectionId}/sso-callback/saml/acs | SAML Callback
[**update_oidc_connection**](SsoApi.md#update_oidc_connection) | **PUT** /org/{accountId}/sso-connections/oidc/{connectionId} | Update OIDC connection
[**update_saml_connection**](SsoApi.md#update_saml_connection) | **PUT** /org/{accountId}/sso-connections/saml/{connectionId} | Update SAML connection


# **create_oidcc_onnection**
> OIDCObj create_oidcc_onnection(account_id, oidc_obj)

Creates OIDC connection

Creates a new OIDC connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.oidc_obj import OIDCObj
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
    api_instance = katanemo_sdk.SsoApi(api_client)
    account_id = 'account_id_example' # str | 
    oidc_obj = katanemo_sdk.OIDCObj() # OIDCObj | ODIC connection attributes

    try:
        # Creates OIDC connection
        api_response = api_instance.create_oidcc_onnection(account_id, oidc_obj)
        print("The response of SsoApi->create_oidcc_onnection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->create_oidcc_onnection: %s\n" % e)
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

# **create_saml_connection**
> SAMLObj create_saml_connection(account_id, saml_obj)

Creates SAML connection

Creates a new SAML connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.saml_obj import SAMLObj
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
    api_instance = katanemo_sdk.SsoApi(api_client)
    account_id = 'account_id_example' # str | 
    saml_obj = katanemo_sdk.SAMLObj() # SAMLObj | SAML connection attributes

    try:
        # Creates SAML connection
        api_response = api_instance.create_saml_connection(account_id, saml_obj)
        print("The response of SsoApi->create_saml_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->create_saml_connection: %s\n" % e)
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

MAP SAML Attributes

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

# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.SsoApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 
    attribute_role_mapping = katanemo_sdk.AttributeRoleMapping() # AttributeRoleMapping | SAML user attributes to role mapping

    try:
        # MAP SAML Attributes
        api_response = api_instance.create_saml_connection_mapping(account_id, connection_id, attribute_role_mapping)
        print("The response of SsoApi->create_saml_connection_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->create_saml_connection_mapping: %s\n" % e)
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

# **delete_oidc_connection**
> delete_oidc_connection(account_id, connection_id)

Delete OIDC connection

Delete an OIDC connection

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
    api_instance = katanemo_sdk.SsoApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 

    try:
        # Delete OIDC connection
        api_instance.delete_oidc_connection(account_id, connection_id)
    except Exception as e:
        print("Exception when calling SsoApi->delete_oidc_connection: %s\n" % e)
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

# **get_oidc_connection**
> OIDCObj get_oidc_connection(account_id, connection_id)

Get OIDC connection

Get details of an OIDC connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.oidc_obj import OIDCObj
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
    api_instance = katanemo_sdk.SsoApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 

    try:
        # Get OIDC connection
        api_response = api_instance.get_oidc_connection(account_id, connection_id)
        print("The response of SsoApi->get_oidc_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->get_oidc_connection: %s\n" % e)
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

List OIDC Connections

Returns a list of all OIDC connections belonging to provided organization

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.oidc_obj import OIDCObj
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
    api_instance = katanemo_sdk.SsoApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # List OIDC Connections
        api_response = api_instance.get_oidc_connections_for_account(account_id)
        print("The response of SsoApi->get_oidc_connections_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->get_oidc_connections_for_account: %s\n" % e)
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

# **get_saml_connection**
> SAMLObj get_saml_connection(account_id, connection_id)

Get connection

Retreive a SAML connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.saml_obj import SAMLObj
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
    api_instance = katanemo_sdk.SsoApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 

    try:
        # Get connection
        api_response = api_instance.get_saml_connection(account_id, connection_id)
        print("The response of SsoApi->get_saml_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->get_saml_connection: %s\n" % e)
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

List SAML Connections

Returns a list of all SAML connections belonging to provided organization

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.saml_obj import SAMLObj
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
    api_instance = katanemo_sdk.SsoApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # List SAML Connections
        api_response = api_instance.get_saml_connections_for_account(account_id)
        print("The response of SsoApi->get_saml_connections_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->get_saml_connections_for_account: %s\n" % e)
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

# **o_idc_login_trigger**
> Error o_idc_login_trigger(connection_id, account_id)

Trigger OIDC SSO

Triggers SSO for a particular OIDC connection. This would be initiated by the developer from applicatoon code

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.error import Error
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
    api_instance = katanemo_sdk.SsoApi(api_client)
    connection_id = 'connection_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Trigger OIDC SSO
        api_response = api_instance.o_idc_login_trigger(connection_id, account_id)
        print("The response of SsoApi->o_idc_login_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->o_idc_login_trigger: %s\n" % e)
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

OIDC Callback

Handles OIDC login callback

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.error import Error
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
    api_instance = katanemo_sdk.SsoApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 
    code = 'code_example' # str | Authorization code returned by the OIDC provider
    state = 'state_example' # str | Authorization code returned by the OIDC provider

    try:
        # OIDC Callback
        api_response = api_instance.oidc_sso_call_back(account_id, connection_id, code, state)
        print("The response of SsoApi->oidc_sso_call_back:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->oidc_sso_call_back: %s\n" % e)
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

Triggers SAML SSO

Triggers SAML login for a particular connection. Account can have multiple SAML connections. It redirects to the login URL corresponding to a particular connection.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.error import Error
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
    api_instance = katanemo_sdk.SsoApi(api_client)
    connection_id = 'connection_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Triggers SAML SSO
        api_response = api_instance.s_aml_login_trigger(connection_id, account_id)
        print("The response of SsoApi->s_aml_login_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->s_aml_login_trigger: %s\n" % e)
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

SAML Callback

Handle SAML login callback with SAML assertion. It can be passed as query parameter or payload.

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.error import Error
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
    api_instance = katanemo_sdk.SsoApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 
    saml_response = 'saml_response_example' # str | SAML response returned by the SAML IDP (optional)
    saml_response2 = 'saml_response_example' # str | SAML response returned by the SAML IDP (optional)

    try:
        # SAML Callback
        api_response = api_instance.saml_sso_call_back(account_id, connection_id, saml_response=saml_response, saml_response2=saml_response2)
        print("The response of SsoApi->saml_sso_call_back:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->saml_sso_call_back: %s\n" % e)
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

# **update_oidc_connection**
> OIDCObj update_oidc_connection(account_id, connection_id, oidc_obj)

Update OIDC connection

Updates a OIDC connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.oidc_obj import OIDCObj
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
    api_instance = katanemo_sdk.SsoApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 
    oidc_obj = katanemo_sdk.OIDCObj() # OIDCObj | OIDC connection attributes

    try:
        # Update OIDC connection
        api_response = api_instance.update_oidc_connection(account_id, connection_id, oidc_obj)
        print("The response of SsoApi->update_oidc_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->update_oidc_connection: %s\n" % e)
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

# **update_saml_connection**
> SAMLObj update_saml_connection(account_id, connection_id, saml_obj)

Update SAML connection

Updates a SAML connection

### Example

```python
import time
import os
import katanemo_sdk
from katanemo_sdk.models.saml_obj import SAMLObj
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
    api_instance = katanemo_sdk.SsoApi(api_client)
    account_id = 'account_id_example' # str | 
    connection_id = 'connection_id_example' # str | 
    saml_obj = katanemo_sdk.SAMLObj() # SAMLObj | SAML connection attributes

    try:
        # Update SAML connection
        api_response = api_instance.update_saml_connection(account_id, connection_id, saml_obj)
        print("The response of SsoApi->update_saml_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoApi->update_saml_connection: %s\n" % e)
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

