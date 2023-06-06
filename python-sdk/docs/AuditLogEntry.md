# AuditLogEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | 
**account_id** | **str** |  | 
**service_id** | **str** |  | 
**path** | **str** |  | 
**operation** | **str** |  | 
**principal** | **str** |  | 
**authentication_code** | **int** |  | 
**authorization_code** | **int** |  | 

## Example

```python
from katanemo_sdk.models.audit_log_entry import AuditLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntry from a JSON string
audit_log_entry_instance = AuditLogEntry.from_json(json)
# print the JSON string representation of the object
print AuditLogEntry.to_json()

# convert the object into a dict
audit_log_entry_dict = audit_log_entry_instance.to_dict()
# create an instance of AuditLogEntry from a dict
audit_log_entry_form_dict = audit_log_entry.from_dict(audit_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


