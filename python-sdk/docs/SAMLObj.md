# SAMLObj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** |  | [optional] 
**id_provider** | **str** |  | 
**default_role_id** | **str** |  | 
**login_link** | **str** |  | [optional] 
**metadata_link** | **str** |  | [optional] 
**acs_link** | **str** |  | [optional] 
**audience_link** | **str** |  | [optional] 
**attribute_role_mappings** | [**List[AttributeRoleMapping]**](AttributeRoleMapping.md) |  | [optional] 
**root_url** | **str** |  | [optional] 
**account_id** | **str** |  | 
**service_id** | **str** |  | 

## Example

```python
from katanemo_sdk.models.saml_obj import SAMLObj

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLObj from a JSON string
saml_obj_instance = SAMLObj.from_json(json)
# print the JSON string representation of the object
print SAMLObj.to_json()

# convert the object into a dict
saml_obj_dict = saml_obj_instance.to_dict()
# create an instance of SAMLObj from a dict
saml_obj_form_dict = saml_obj.from_dict(saml_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


