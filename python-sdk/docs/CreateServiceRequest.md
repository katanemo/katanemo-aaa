# CreateServiceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Service Name | 
**description** | **str** | Service Description | [optional] 
**redirect_url** | **str** | Redirect URL after a successful login. | 
**api_spec_file** | **bytearray** | openapi service json or yaml file | 
**auth_exclusion_paths** | **List[str]** | List of paths for which we do not require authentication | [optional] 
**display_name** | **str** | Display name of the service/company used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
**logo_url** | **str** | The URL for the service/company Logo used in the Sign up, Login, Logout and other relevant branding pages | [optional] 
**details_image_url** | **str** | The URL of image showing details about the service to be displayed on the sign-up page. | [optional] 
**terms_url** | **str** | The URL for the terms of the service | [optional] 
**privacy_url** | **str** | The URL for the privacy of the service | [optional] 
**docs_url** | **str** | The URL for the documentation of the service | [optional] 

## Example

```python
from katanemo_sdk.models.create_service_request import CreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServiceRequest from a JSON string
create_service_request_instance = CreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print CreateServiceRequest.to_json()

# convert the object into a dict
create_service_request_dict = create_service_request_instance.to_dict()
# create an instance of CreateServiceRequest from a dict
create_service_request_form_dict = create_service_request.from_dict(create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


