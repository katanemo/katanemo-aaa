# SetPasswordRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | Email address of the user. | 
**session** | **str** | Session information of the user from confirm user respoonse. | 
**password** | **str** | Password of the user for the user to be used in future. | 

## Example

```python
from katanemo_identity.models.set_password_request import SetPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetPasswordRequest from a JSON string
set_password_request_instance = SetPasswordRequest.from_json(json)
# print the JSON string representation of the object
print SetPasswordRequest.to_json()

# convert the object into a dict
set_password_request_dict = set_password_request_instance.to_dict()
# create an instance of SetPasswordRequest from a dict
set_password_request_form_dict = set_password_request.from_dict(set_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


