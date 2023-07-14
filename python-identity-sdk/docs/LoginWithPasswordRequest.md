# LoginWithPasswordRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | Email address of the developer account&#39;s user | 
**password** | **str** | Password of the user | 
**skip_redirect** | **bool** | By default login will redirect to service redirect URL, if this parameter is set as true then response will be returned. | [optional] 
**state** | **str** | Optional state parameter. | [optional] 

## Example

```python
from katanemo_identity.models.login_with_password_request import LoginWithPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoginWithPasswordRequest from a JSON string
login_with_password_request_instance = LoginWithPasswordRequest.from_json(json)
# print the JSON string representation of the object
print LoginWithPasswordRequest.to_json()

# convert the object into a dict
login_with_password_request_dict = login_with_password_request_instance.to_dict()
# create an instance of LoginWithPasswordRequest from a dict
login_with_password_request_form_dict = login_with_password_request.from_dict(login_with_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


