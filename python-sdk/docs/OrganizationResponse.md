# OrganizationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**name** | **str** |  | 
**admin_account** | **str** |  | 
**domain_verification_code** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**domain_verified** | **bool** |  | [optional] 
**users_count** | **int** |  | [optional] 
**roles_count** | **int** |  | [optional] 
**oidc_connections_count** | **int** |  | [optional] 
**saml_connections_count** | **int** |  | [optional] 
**default_connection** | **str** |  | [optional] 
**default_connection_type** | **str** |  | [optional] 
**launched_services** | **List[str]** |  | [optional] 
**subscribed_services** | **List[str]** |  | [optional] 
**subscribers** | **List[str]** |  | [optional] 

## Example

```python
from katanemo_sdk.models.organization_response import OrganizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationResponse from a JSON string
organization_response_instance = OrganizationResponse.from_json(json)
# print the JSON string representation of the object
print OrganizationResponse.to_json()

# convert the object into a dict
organization_response_dict = organization_response_instance.to_dict()
# create an instance of OrganizationResponse from a dict
organization_response_form_dict = organization_response.from_dict(organization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


