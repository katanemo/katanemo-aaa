# GetDeveloperPublicKeys200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[OIDCPublicKey]**](OIDCPublicKey.md) |  | [optional] 

## Example

```python
from katanemo_identity.models.get_developer_public_keys200_response import GetDeveloperPublicKeys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeveloperPublicKeys200Response from a JSON string
get_developer_public_keys200_response_instance = GetDeveloperPublicKeys200Response.from_json(json)
# print the JSON string representation of the object
print GetDeveloperPublicKeys200Response.to_json()

# convert the object into a dict
get_developer_public_keys200_response_dict = get_developer_public_keys200_response_instance.to_dict()
# create an instance of GetDeveloperPublicKeys200Response from a dict
get_developer_public_keys200_response_form_dict = get_developer_public_keys200_response.from_dict(get_developer_public_keys200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


