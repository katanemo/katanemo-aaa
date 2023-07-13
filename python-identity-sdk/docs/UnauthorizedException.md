# UnauthorizedException


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 

## Example

```python
from katanemo_identity.models.unauthorized_exception import UnauthorizedException

# TODO update the JSON string below
json = "{}"
# create an instance of UnauthorizedException from a JSON string
unauthorized_exception_instance = UnauthorizedException.from_json(json)
# print the JSON string representation of the object
print UnauthorizedException.to_json()

# convert the object into a dict
unauthorized_exception_dict = unauthorized_exception_instance.to_dict()
# create an instance of UnauthorizedException from a dict
unauthorized_exception_form_dict = unauthorized_exception.from_dict(unauthorized_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


