# Policy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_content** | **str** | Policy rules for allowing API paths, it can be defined as json or yaml format. | 

## Example

```python
from katanemo_identity.models.policy import Policy

# TODO update the JSON string below
json = "{}"
# create an instance of Policy from a JSON string
policy_instance = Policy.from_json(json)
# print the JSON string representation of the object
print Policy.to_json()

# convert the object into a dict
policy_dict = policy_instance.to_dict()
# create an instance of Policy from a dict
policy_form_dict = policy.from_dict(policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


