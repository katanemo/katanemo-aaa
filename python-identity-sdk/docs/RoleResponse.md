# RoleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AccountId | [optional] 
**role_id** | **str** | Role Id | [optional] 
**rolename** | **str** | Role name | [optional] 
**description** | **str** | Role description | [optional] 
**service_id** | **str** | ID of the service | [optional] 
**policy** | [**Policy**](Policy.md) |  | [optional] 
**version** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**created_at** | **int** |  | [optional] 

## Example

```python
from katanemo_identity.models.role_response import RoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleResponse from a JSON string
role_response_instance = RoleResponse.from_json(json)
# print the JSON string representation of the object
print RoleResponse.to_json()

# convert the object into a dict
role_response_dict = role_response_instance.to_dict()
# create an instance of RoleResponse from a dict
role_response_form_dict = role_response.from_dict(role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


