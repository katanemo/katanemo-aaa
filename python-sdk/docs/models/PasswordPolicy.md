# katanemo_sdk.model.password_policy.PasswordPolicy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**requireSymbols** | bool,  | BoolClass,  | In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password. | 
**requiredNumbers** | bool,  | BoolClass,  | In the password policy that you have set, refers to whether you have required users to use at least one number in their password. | 
**requireLowerCase** | bool,  | BoolClass,  | In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password. | 
**minimumLegnth** | decimal.Decimal, int,  | decimal.Decimal,  | The minimum length of the password in the policy that you have set. This value can&#x27;t be less than 6. | value must be a 32 bit integer
**requireUpperCase** | bool,  | BoolClass,  | In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

