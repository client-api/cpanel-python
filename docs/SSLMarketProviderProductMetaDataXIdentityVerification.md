# SSLMarketProviderProductMetaDataXIdentityVerification

Defines a schema for identity verification information for OV and EV certificates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The display name of the property. | [optional] 
**name** | **str** | The name of the property. | [optional] 

## Example

```python
from clientapi_cpanel.models.ssl_market_provider_product_meta_data_x_identity_verification import SSLMarketProviderProductMetaDataXIdentityVerification

# TODO update the JSON string below
json = "{}"
# create an instance of SSLMarketProviderProductMetaDataXIdentityVerification from a JSON string
ssl_market_provider_product_meta_data_x_identity_verification_instance = SSLMarketProviderProductMetaDataXIdentityVerification.from_json(json)
# print the JSON string representation of the object
print(SSLMarketProviderProductMetaDataXIdentityVerification.to_json())

# convert the object into a dict
ssl_market_provider_product_meta_data_x_identity_verification_dict = ssl_market_provider_product_meta_data_x_identity_verification_instance.to_dict()
# create an instance of SSLMarketProviderProductMetaDataXIdentityVerification from a dict
ssl_market_provider_product_meta_data_x_identity_verification_from_dict = SSLMarketProviderProductMetaDataXIdentityVerification.from_dict(ssl_market_provider_product_meta_data_x_identity_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


