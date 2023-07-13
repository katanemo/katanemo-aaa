# UserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Organization Identifier for a SaaS customer | 
**service_id** | **str** | Service which this account subscribed to | [optional] 
**user_id** | **str** | Email | [optional] 
**is_admin** | **bool** | is the user an admin? | [optional] 
**is_active** | **bool** | Is the user active yet? | [optional] 
**token** | **str** | User token | [optional] 
**tags** | **Dict[str, List[str]]** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from katanemo_identity.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print UserResponse.to_json()

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_form_dict = user_response.from_dict(user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


