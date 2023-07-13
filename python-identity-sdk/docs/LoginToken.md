# LoginToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Login Token | 

## Example

```python
from katanemo_identity.models.login_token import LoginToken

# TODO update the JSON string below
json = "{}"
# create an instance of LoginToken from a JSON string
login_token_instance = LoginToken.from_json(json)
# print the JSON string representation of the object
print LoginToken.to_json()

# convert the object into a dict
login_token_dict = login_token_instance.to_dict()
# create an instance of LoginToken from a dict
login_token_form_dict = login_token.from_dict(login_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


