# AuthorizationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Authorization Token | 
**path** | **str** | Authorization path | 
**http_method** | **str** | Authorization HTTP Method (GET, POST, PUT, PATCH, DELETE) | 
**request_body** | **str** | Requst body in json format | [optional] 

## Example

```python
from katanemo_auth_sdk.models.authorization_request import AuthorizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationRequest from a JSON string
authorization_request_instance = AuthorizationRequest.from_json(json)
# print the JSON string representation of the object
print AuthorizationRequest.to_json()

# convert the object into a dict
authorization_request_dict = authorization_request_instance.to_dict()
# create an instance of AuthorizationRequest from a dict
authorization_request_form_dict = authorization_request.from_dict(authorization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


