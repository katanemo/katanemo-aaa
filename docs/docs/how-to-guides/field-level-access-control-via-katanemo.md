---
sidebar_position: 5
---

# How to Configure Field-Level Access Control (and filtering) via Katanemo Roles?


Katanemo allows you (a subscriber of a service) to easily construct Roles via OpenAPI semantics (RESTful paths and http methods) that limit operations for a user/machine. This approach requires _little to no learning curve_ in establishing simple yet powerful authorization rules for consuming a service.

Using the same OpenAPI approach, Katanemo also allows you to construct field-level access controls. This is useful if you want certain users or machines to only operate on particular fields of a resource. For example, the following policy allows you to do a PUT operation on the _metadata_ OR _nodeGroups.maxSize_ fields of the cluster resource.



```yaml
 allow:
  apis:
   - PUT:/cluster/{clusterId}:[metadata, nodeGroups.maxSize]
  where: $resourceTags:cluster = 'dev' AND $resourceTags:namespace IN ('NS1', 'NS2) 
```


In the above example if the user tries to PUT on the following path /cluster/1234 with parameters other than _metadata_ OR _nodeGroups.maxSize _the request will be denied by Katanemo’s authorizer. _Note,_ nodeGroups.maxSize is a nested field in this case, which means the presence of any other nested field in nodeGroups will also fail the authorization request. Note, the cluster resource must be defined along with its resource (nested) fields in the OpenAPI spec.

Similarly, the following policy allows a user or machine to GET Patient resource data only via the identifier and email fields specified in the query parameters of a GET call


```yaml
 allow: 
   apis:
    - GET:/patient:[identifier, email]
```


In the above example if a user tries to GET /patient with request parameters other than _identifier or email_ the request will be denied by Katanemo. Note, _identifier _and _email_ must be defined as “_in: query” _OpenAPI parameters on the Patient resource, else you won’t be able to create the Role policy successfully.



_Filtering (coming soon)_

Similarly, if you want to filter fields from responses, you can use Katanemo’s filterResponseAPI that uses Role policies to filter fields on your behalf. For example, the following policy filters out fields metadata.name, vpc.subnets.* and secretsEncryption.keyARN fields in the GET response for a cluster resource.


```yaml
filter:
   GET:/cluster/{clusterId}:[metadata.name, vpc.subnets.*, secretsEncryption.keyARN]
```


Before the response is sent to the client, you simply call Katanemo’s filterResponse API with the auth token received in the request, and Katanemo’s ARC will filter fields based on the Role’s filter policy, and return the final response object that should be sent upstream to the client/user. You can optionally send in a “mask=&lt;string-value-8>” parameter to the filterResponseAPI call and instead of filtering out the fields altogether, it will mask the field values with &lt;string-value-8> so that clients experience doesn’t break inadvertently if the presence of the field name is expected in the response.

_Note_: The filterResponse API is stateless. So if you support a paginated API, then you must call filterResponse every time you want to filter results back to the caller for a paginated API call.

_Note_: Today, Katanemo allows you to construct field-level access control (and filtering) policies via a allow-list approach. If there is a use case that warrants us supporting blocklists, then please send feedback to [feedback@Katanemo.com](mailto:feedback@katanemo.com).

