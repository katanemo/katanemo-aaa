# katanemo_sdk.model.saml_obj.SAMLObj

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accountId** | str,  | str,  |  | 
**idProvider** | str,  | str,  |  | 
**serviceId** | str,  | str,  |  | 
**defaultRoleId** | str,  | str,  |  | 
**connectionId** | str,  | str,  |  | [optional] 
**state** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**loginLink** | str,  | str,  |  | [optional] 
**metadataLink** | str,  | str,  |  | [optional] 
**acsLink** | str,  | str,  |  | [optional] 
**audienceLink** | str,  | str,  |  | [optional] 
**[attributeRoleMappings](#attributeRoleMappings)** | list, tuple,  | tuple,  |  | [optional] 
**rootURL** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attributeRoleMappings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AttributeRoleMapping**](AttributeRoleMapping.md) | [**AttributeRoleMapping**](AttributeRoleMapping.md) | [**AttributeRoleMapping**](AttributeRoleMapping.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

