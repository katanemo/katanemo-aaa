# OIDCPublicKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** | key id | [optional] 
**alg** | **str** | Key algorithm | [optional] 
**e** | **str** | RSA exponent | [optional] 
**n** | **str** | RSA modulus | [optional] 
**use** | **str** | key usage | [optional] 
**kty** | **str** | key type | [optional] 

## Example

```python
from katanemo_sdk.models.oidc_public_key import OIDCPublicKey

# TODO update the JSON string below
json = "{}"
# create an instance of OIDCPublicKey from a JSON string
oidc_public_key_instance = OIDCPublicKey.from_json(json)
# print the JSON string representation of the object
print OIDCPublicKey.to_json()

# convert the object into a dict
oidc_public_key_dict = oidc_public_key_instance.to_dict()
# create an instance of OIDCPublicKey from a dict
oidc_public_key_form_dict = oidc_public_key.from_dict(oidc_public_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


