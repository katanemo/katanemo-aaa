# PasswordPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_legnth** | **int** | The minimum length of the password in the policy that you have set. This value can&#39;t be less than 6. | 
**required_numbers** | **bool** | In the password policy that you have set, refers to whether you have required users to use at least one number in their password. | 
**require_symbols** | **bool** | In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password. | 
**require_upper_case** | **bool** | In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password. | 
**require_lower_case** | **bool** | In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password. | 

## Example

```python
from katanemo_sdk.models.password_policy import PasswordPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicy from a JSON string
password_policy_instance = PasswordPolicy.from_json(json)
# print the JSON string representation of the object
print PasswordPolicy.to_json()

# convert the object into a dict
password_policy_dict = password_policy_instance.to_dict()
# create an instance of PasswordPolicy from a dict
password_policy_form_dict = password_policy.from_dict(password_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


