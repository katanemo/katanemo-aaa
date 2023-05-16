# Organization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**name** | **str** |  | 
**admin_account** | **str** |  | 
**users_count** | **int** |  | [optional] 
**roles_count** | **int** |  | [optional] 
**oidc_connections_count** | **int** |  | [optional] 
**saml_connections_count** | **int** |  | [optional] 
**launched_services** | **List[str]** |  | [optional] 
**subscribed_services** | **List[str]** |  | [optional] 
**subscribers** | **List[str]** |  | [optional] 

## Example

```python
from katanemo_sdk.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print Organization.to_json()

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_form_dict = organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


