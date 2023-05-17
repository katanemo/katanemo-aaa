# ClientKeyResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from katanemo_sdk.models.client_key_response import ClientKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientKeyResponse from a JSON string
client_key_response_instance = ClientKeyResponse.from_json(json)
# print the JSON string representation of the object
print ClientKeyResponse.to_json()

# convert the object into a dict
client_key_response_dict = client_key_response_instance.to_dict()
# create an instance of ClientKeyResponse from a dict
client_key_response_form_dict = client_key_response.from_dict(client_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


