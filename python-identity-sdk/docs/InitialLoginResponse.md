# InitialLoginResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso_enabled** | **bool** | Determines if sso is enabled or not | 
**sso_redirect_url** | **str** | If sso is enabled then have to make call to sso endpoint for authentication | [optional] 

## Example

```python
from katanemo_identity.models.initial_login_response import InitialLoginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InitialLoginResponse from a JSON string
initial_login_response_instance = InitialLoginResponse.from_json(json)
# print the JSON string representation of the object
print InitialLoginResponse.to_json()

# convert the object into a dict
initial_login_response_dict = initial_login_response_instance.to_dict()
# create an instance of InitialLoginResponse from a dict
initial_login_response_form_dict = initial_login_response.from_dict(initial_login_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


