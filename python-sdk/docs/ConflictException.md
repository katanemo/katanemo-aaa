# ConflictException


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 

## Example

```python
from katanemo_sdk.models.conflict_exception import ConflictException

# TODO update the JSON string below
json = "{}"
# create an instance of ConflictException from a JSON string
conflict_exception_instance = ConflictException.from_json(json)
# print the JSON string representation of the object
print ConflictException.to_json()

# convert the object into a dict
conflict_exception_dict = conflict_exception_instance.to_dict()
# create an instance of ConflictException from a dict
conflict_exception_form_dict = conflict_exception.from_dict(conflict_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


