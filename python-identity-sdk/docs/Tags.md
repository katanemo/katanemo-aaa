# Tags


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id_path** | **str** |  | [optional] 
**name** | **str** |  | 
**resource_id** | **str** |  | 
**account_id** | **str** |  | [optional] 
**tags** | **Dict[str, List[str]]** |  | 

## Example

```python
from katanemo_identity.models.tags import Tags

# TODO update the JSON string below
json = "{}"
# create an instance of Tags from a JSON string
tags_instance = Tags.from_json(json)
# print the JSON string representation of the object
print Tags.to_json()

# convert the object into a dict
tags_dict = tags_instance.to_dict()
# create an instance of Tags from a dict
tags_form_dict = tags.from_dict(tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


