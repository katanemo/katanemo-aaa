# InitialLoginRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | Email address of the developer account&#39;s user | 

## Example

```python
from katanemo_sdk.models.initial_login_request import InitialLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InitialLoginRequest from a JSON string
initial_login_request_instance = InitialLoginRequest.from_json(json)
# print the JSON string representation of the object
print InitialLoginRequest.to_json()

# convert the object into a dict
initial_login_request_dict = initial_login_request_instance.to_dict()
# create an instance of InitialLoginRequest from a dict
initial_login_request_form_dict = initial_login_request.from_dict(initial_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


