# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Tenant name | 
**service_id** | **str** | Service ID which this account subscribed to | [optional] 
**user_id** | **str** | User name (email) | [optional] 
**is_admin** | **bool** | is the user an admin? | [optional] 
**is_active** | **bool** | Is the user active yet? | [optional] 
**token** | **str** | User token | [optional] 
**tags** | **Dict[str, List[str]]** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from katanemo_sdk.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


