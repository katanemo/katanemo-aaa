# OktaObj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_name** | **str** | Okta organization name | 
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
**connection_id** | **str** |  | [optional] 

## Example

```python
from katanemo_sdk.models.okta_obj import OktaObj

# TODO update the JSON string below
json = "{}"
# create an instance of OktaObj from a JSON string
okta_obj_instance = OktaObj.from_json(json)
# print the JSON string representation of the object
print OktaObj.to_json()

# convert the object into a dict
okta_obj_dict = okta_obj_instance.to_dict()
# create an instance of OktaObj from a dict
okta_obj_form_dict = okta_obj.from_dict(okta_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


