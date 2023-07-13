# UserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Tenant name | 
**user_id** | **str** | email address of the user | [optional] 
**tags** | **Dict[str, List[str]]** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from katanemo_identity.models.user_request import UserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRequest from a JSON string
user_request_instance = UserRequest.from_json(json)
# print the JSON string representation of the object
print UserRequest.to_json()

# convert the object into a dict
user_request_dict = user_request_instance.to_dict()
# create an instance of UserRequest from a dict
user_request_form_dict = user_request.from_dict(user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


