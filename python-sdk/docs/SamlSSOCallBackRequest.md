# SamlSSOCallBackRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saml_response** | **str** | SAML response returned by the SAML IDP | [optional] 

## Example

```python
from katanemo_sdk.models.saml_sso_call_back_request import SamlSSOCallBackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SamlSSOCallBackRequest from a JSON string
saml_sso_call_back_request_instance = SamlSSOCallBackRequest.from_json(json)
# print the JSON string representation of the object
print SamlSSOCallBackRequest.to_json()

# convert the object into a dict
saml_sso_call_back_request_dict = saml_sso_call_back_request_instance.to_dict()
# create an instance of SamlSSOCallBackRequest from a dict
saml_sso_call_back_request_form_dict = saml_sso_call_back_request.from_dict(saml_sso_call_back_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


