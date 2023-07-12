# OAuthTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_token** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**token_type** | **str** |  | [optional] 

## Example

```python
from katanemo_identity.models.o_auth_token_response import OAuthTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthTokenResponse from a JSON string
o_auth_token_response_instance = OAuthTokenResponse.from_json(json)
# print the JSON string representation of the object
print OAuthTokenResponse.to_json()

# convert the object into a dict
o_auth_token_response_dict = o_auth_token_response_instance.to_dict()
# create an instance of OAuthTokenResponse from a dict
o_auth_token_response_form_dict = o_auth_token_response.from_dict(o_auth_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


