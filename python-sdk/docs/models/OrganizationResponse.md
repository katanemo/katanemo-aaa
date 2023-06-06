# katanemo_sdk.model.organization_response.OrganizationResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accountId** | str,  | str,  |  | 
**adminAccount** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**domainVerificationCode** | str,  | str,  |  | [optional] 
**domain** | str,  | str,  |  | [optional] 
**domainVerified** | bool,  | BoolClass,  |  | [optional] 
**usersCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**rolesCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**oidcConnectionsCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**samlConnectionsCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**defaultConnection** | str,  | str,  |  | [optional] 
**defaultConnectionType** | str,  | str,  |  | [optional] 
**[launchedServices](#launchedServices)** | list, tuple,  | tuple,  |  | [optional] 
**[subscribedServices](#subscribedServices)** | list, tuple,  | tuple,  |  | [optional] 
**[subscribers](#subscribers)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# launchedServices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# subscribedServices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# subscribers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

