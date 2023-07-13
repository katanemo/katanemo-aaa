# BadRequestException


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 

## Example

```python
from katanemo_identity.models.bad_request_exception import BadRequestException

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestException from a JSON string
bad_request_exception_instance = BadRequestException.from_json(json)
# print the JSON string representation of the object
print BadRequestException.to_json()

# convert the object into a dict
bad_request_exception_dict = bad_request_exception_instance.to_dict()
# create an instance of BadRequestException from a dict
bad_request_exception_form_dict = bad_request_exception.from_dict(bad_request_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


