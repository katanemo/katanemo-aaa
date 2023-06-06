# katanemo_sdk.model.update_service_request.UpdateServiceRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Service Name | [optional] 
**description** | str,  | str,  | Service Description | [optional] 
**redirectUrl** | str,  | str,  | Redirect URL after a successful login. | [optional] 
**apiSpecFile** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | openapi service json or yaml file | [optional] 
**[authExclusionPaths](#authExclusionPaths)** | list, tuple,  | tuple,  | List of paths for which we do not require authentication | [optional] 
**displayName** | str,  | str,  | Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
**logoUrl** | str,  | str,  | The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
**detailsImageUrl** | str,  | str,  | The URL of image showing details about the service to be displayed on the sign-up page. | [optional] 
**termsUrl** | str,  | str,  | The URL for the terms of the service | [optional] 
**privacyUrl** | str,  | str,  | The URL for the privacy of the service | [optional] 
**docsUrl** | str,  | str,  | The URL for the documentatio of the service | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# authExclusionPaths

List of paths for which we do not require authentication

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of paths for which we do not require authentication | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

