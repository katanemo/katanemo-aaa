# InternalServerErrorException


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 

## Example

```python
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException

# TODO update the JSON string below
json = "{}"
# create an instance of InternalServerErrorException from a JSON string
internal_server_error_exception_instance = InternalServerErrorException.from_json(json)
# print the JSON string representation of the object
print InternalServerErrorException.to_json()

# convert the object into a dict
internal_server_error_exception_dict = internal_server_error_exception_instance.to_dict()
# create an instance of InternalServerErrorException from a dict
internal_server_error_exception_form_dict = internal_server_error_exception.from_dict(internal_server_error_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


