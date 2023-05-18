# OIDCObj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oidc_config_endpoint** | **str** | OIDC configuration URL | 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**nonce** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**authorization_endpoint** | **str** |  | [optional] 
**token_endpoint** | **str** |  | [optional] 
**user_info_endpoint** | **str** |  | [optional] 
**issuer_endpoint** | **str** |  | [optional] 
**jwks_endpoint** | **str** |  | [optional] 
**connection_id** | **str** |  | [optional] 

## Example

```python
from katanemo_sdk.models.oidc_obj import OIDCObj

# TODO update the JSON string below
json = "{}"
# create an instance of OIDCObj from a JSON string
oidc_obj_instance = OIDCObj.from_json(json)
# print the JSON string representation of the object
print OIDCObj.to_json()

# convert the object into a dict
oidc_obj_dict = oidc_obj_instance.to_dict()
# create an instance of OIDCObj from a dict
oidc_obj_form_dict = oidc_obj.from_dict(oidc_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


