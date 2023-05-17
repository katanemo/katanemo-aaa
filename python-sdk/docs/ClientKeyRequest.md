# ClientKeyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_role_id** | **str** |  | 
**client_name** | **str** |  | 

## Example

```python
from katanemo_sdk.models.client_key_request import ClientKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClientKeyRequest from a JSON string
client_key_request_instance = ClientKeyRequest.from_json(json)
# print the JSON string representation of the object
print ClientKeyRequest.to_json()

# convert the object into a dict
client_key_request_dict = client_key_request_instance.to_dict()
# create an instance of ClientKeyRequest from a dict
client_key_request_form_dict = client_key_request.from_dict(client_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


