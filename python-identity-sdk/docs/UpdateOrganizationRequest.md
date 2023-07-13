# UpdateOrganizationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Organization&#39;s account name to be dupated. | 

## Example

```python
from katanemo_identity.models.update_organization_request import UpdateOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationRequest from a JSON string
update_organization_request_instance = UpdateOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print UpdateOrganizationRequest.to_json()

# convert the object into a dict
update_organization_request_dict = update_organization_request_instance.to_dict()
# create an instance of UpdateOrganizationRequest from a dict
update_organization_request_form_dict = update_organization_request.from_dict(update_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


