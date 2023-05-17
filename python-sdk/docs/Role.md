# Role


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AccountId | [optional] 
**role_id** | **str** | Role Id | [optional] 
**rolename** | **str** | Role name | [optional] 
**service_id** | **str** | ID of the service | [optional] 
**policy** | [**Policy**](Policy.md) |  | [optional] 
**version** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**created_at** | **int** |  | [optional] 

## Example

```python
from katanemo_sdk.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print Role.to_json()

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_form_dict = role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


