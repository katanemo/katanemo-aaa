# GetTagsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_name** | **str** |  | 
**resource_id** | **str** |  | 
**account_id** | **str** |  | 

## Example

```python
from katanemo_identity.models.get_tags_request import GetTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagsRequest from a JSON string
get_tags_request_instance = GetTagsRequest.from_json(json)
# print the JSON string representation of the object
print GetTagsRequest.to_json()

# convert the object into a dict
get_tags_request_dict = get_tags_request_instance.to_dict()
# create an instance of GetTagsRequest from a dict
get_tags_request_form_dict = get_tags_request.from_dict(get_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


