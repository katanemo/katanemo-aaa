# ClientKeyObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**client_name** | **str** |  | [optional] 
**client_key_id** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from katanemo_sdk.models.client_key_object import ClientKeyObject

# TODO update the JSON string below
json = "{}"
# create an instance of ClientKeyObject from a JSON string
client_key_object_instance = ClientKeyObject.from_json(json)
# print the JSON string representation of the object
print ClientKeyObject.to_json()

# convert the object into a dict
client_key_object_dict = client_key_object_instance.to_dict()
# create an instance of ClientKeyObject from a dict
client_key_object_form_dict = client_key_object.from_dict(client_key_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


