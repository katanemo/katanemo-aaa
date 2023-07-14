# AssumeRoleObj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_id** | **str** |  | 
**role_id** | **str** |  | 

## Example

```python
from katanemo_identity.models.assume_role_obj import AssumeRoleObj

# TODO update the JSON string below
json = "{}"
# create an instance of AssumeRoleObj from a JSON string
assume_role_obj_instance = AssumeRoleObj.from_json(json)
# print the JSON string representation of the object
print AssumeRoleObj.to_json()

# convert the object into a dict
assume_role_obj_dict = assume_role_obj_instance.to_dict()
# create an instance of AssumeRoleObj from a dict
assume_role_obj_form_dict = assume_role_obj.from_dict(assume_role_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


