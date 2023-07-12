# OAuthTokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from katanemo_identity.models.o_auth_token_request import OAuthTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthTokenRequest from a JSON string
o_auth_token_request_instance = OAuthTokenRequest.from_json(json)
# print the JSON string representation of the object
print OAuthTokenRequest.to_json()

# convert the object into a dict
o_auth_token_request_dict = o_auth_token_request_instance.to_dict()
# create an instance of OAuthTokenRequest from a dict
o_auth_token_request_form_dict = o_auth_token_request.from_dict(o_auth_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


