# AssignRoleObj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_id** | **str** |  | 
**role_id** | **str** |  | 

## Example

```python
from katanemo_sdk.models.assign_role_obj import AssignRoleObj

# TODO update the JSON string below
json = "{}"
# create an instance of AssignRoleObj from a JSON string
assign_role_obj_instance = AssignRoleObj.from_json(json)
# print the JSON string representation of the object
print AssignRoleObj.to_json()

# convert the object into a dict
assign_role_obj_dict = assign_role_obj_instance.to_dict()
# create an instance of AssignRoleObj from a dict
assign_role_obj_form_dict = assign_role_obj.from_dict(assign_role_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


