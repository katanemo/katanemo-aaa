# InitArcResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue_url** | **str** |  | [optional] 
**key_id** | **str** |  | [optional] 
**key_secret** | **str** |  | [optional] 
**session_token** | **str** |  | [optional] 
**expiration** | **int** |  | [optional] 

## Example

```python
from katanemo_sdk.models.init_arc_response import InitArcResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InitArcResponse from a JSON string
init_arc_response_instance = InitArcResponse.from_json(json)
# print the JSON string representation of the object
print InitArcResponse.to_json()

# convert the object into a dict
init_arc_response_dict = init_arc_response_instance.to_dict()
# create an instance of InitArcResponse from a dict
init_arc_response_form_dict = init_arc_response.from_dict(init_arc_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


