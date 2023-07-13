# AttributeRoleMapping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | 
**value** | **str** |  | 
**role_id** | **str** |  | 

## Example

```python
from katanemo_identity.models.attribute_role_mapping import AttributeRoleMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeRoleMapping from a JSON string
attribute_role_mapping_instance = AttributeRoleMapping.from_json(json)
# print the JSON string representation of the object
print AttributeRoleMapping.to_json()

# convert the object into a dict
attribute_role_mapping_dict = attribute_role_mapping_instance.to_dict()
# create an instance of AttributeRoleMapping from a dict
attribute_role_mapping_form_dict = attribute_role_mapping.from_dict(attribute_role_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


