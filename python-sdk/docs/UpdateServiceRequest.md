# UpdateServiceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Service Name | [optional] 
**description** | **str** | Service Description | [optional] 
**redirect_url** | **str** | Redirect URL after a successful login. | [optional] 
**api_spec_file** | **bytearray** | openapi service json or yaml file | [optional] 
**auth_exclusion_paths** | **List[str]** | List of paths for which we do not require authentication | [optional] 
**display_name** | **str** | Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
**logo_url** | **str** | The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
**details_image_url** | **str** | The URL of image showing details about the service to be displayed on the sign-up page. | [optional] 
**terms_url** | **str** | The URL for the terms of the service | [optional] 
**privacy_url** | **str** | The URL for the privacy of the service | [optional] 
**docs_url** | **str** | The URL for the documentatio of the service | [optional] 

## Example

```python
from katanemo_sdk.models.update_service_request import UpdateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServiceRequest from a JSON string
update_service_request_instance = UpdateServiceRequest.from_json(json)
# print the JSON string representation of the object
print UpdateServiceRequest.to_json()

# convert the object into a dict
update_service_request_dict = update_service_request_instance.to_dict()
# create an instance of UpdateServiceRequest from a dict
update_service_request_form_dict = update_service_request.from_dict(update_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


