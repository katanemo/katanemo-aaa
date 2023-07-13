# UserConfirmationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session** | **str** | Session info in response to confirm user. This session can be used to set password. | 
**account_id** | **str** | returns the account id for the organization that subscribed to the service. | 
**email_address** | **str** | returns the email address of the user signing up. | 
**service_id** | **str** | returns the service id for which user subscribed to. | 

## Example

```python
from katanemo_identity.models.user_confirmation_response import UserConfirmationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserConfirmationResponse from a JSON string
user_confirmation_response_instance = UserConfirmationResponse.from_json(json)
# print the JSON string representation of the object
print UserConfirmationResponse.to_json()

# convert the object into a dict
user_confirmation_response_dict = user_confirmation_response_instance.to_dict()
# create an instance of UserConfirmationResponse from a dict
user_confirmation_response_form_dict = user_confirmation_response.from_dict(user_confirmation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


