# NotFoundException


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 

## Example

```python
from katanemo_identity.models.not_found_exception import NotFoundException

# TODO update the JSON string below
json = "{}"
# create an instance of NotFoundException from a JSON string
not_found_exception_instance = NotFoundException.from_json(json)
# print the JSON string representation of the object
print NotFoundException.to_json()

# convert the object into a dict
not_found_exception_dict = not_found_exception_instance.to_dict()
# create an instance of NotFoundException from a dict
not_found_exception_form_dict = not_found_exception.from_dict(not_found_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


