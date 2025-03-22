# MarketProviderProductMetaDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_name** | **str** | The provider&#39;s base name. | [optional] 
**billing_type** | **str** | The provider&#39;s billing type | [optional] 
**description** | **str** | The product&#39;s description. | [optional] 
**display_name** | **str** | The product&#39;s display name. | [optional] 
**enabled** | **int** | Whether the product is enabled in the cPanel Market. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Not enabled. | [optional] 
**icon** | **str** | The product&#39;s display icon. | [optional] 
**icon_mime_type** | **str** | The icon&#39;s file type. | [optional] 
**license_term** | **int** | The providers license term | [optional] 
**max_users** | **int** | The maximum number of users. | [optional] 
**maximum_server_price** | **float** | The maximum price that the system will allow for the product. | [optional] 
**minimum_server_price** | **float** | The minimum price that the system will allow for the product. | [optional] 
**price** | **float** | The product&#39;s price. | [optional] 
**price_unit** | **str** | The currency code of the product&#39;s price. | [optional] 
**product** | **str** | The product name. | [optional] 
**product_category** | **str** | The product&#39;s category. | [optional] 
**product_group** | **str** | The product&#39;s group. | [optional] 
**product_id** | **int** | The product&#39;s ID. | [optional] 
**provider_display_name** | **str** | The cPanel Market provider&#39;s display name.  **Note:**  The &#x60;_DISPLAY_NAME&#x60; attribute in the cPanel Market provider module contains this value. | [optional] 
**provider_name** | **str** | The cPanel Market provider&#39;s name. | [optional] 
**recommended** | **int** | Whether the product is recommended. * &#x60;1&#x60; — We recommend the product. * &#x60;0&#x60; — We do not recommend the product. | [optional] 
**requires_ip** | **int** | Whether the product requires an IP address. * &#x60;1&#x60; — Requires an IP. * &#x60;0&#x60; — Does **not** require an IP. | [optional] 
**x_certificate_term** | **List[str]** | An array that indicates the length of time and unit of time that the product secures for. | [optional] 
**x_identity_verification** | [**SSLMarketProviderProductMetaDataXIdentityVerification**](SSLMarketProviderProductMetaDataXIdentityVerification.md) |  | [optional] 
**x_max_http_redirects** | **int** | The maximum number of HTTP redirections that the provider allows during a Domain Control Validation (DCV) check of the domain or domains in the certificate. | [optional] 
**x_payment_trigger** | **str** | Indicates whether the provider charges immediately or when they issue the Secure Sockets Layer (SSL) certificate.  * &#x60;checkout&#x60; — Collect payment and finalize immediately after checkout. Any failures to issue the certificate must prompt a separate refund. * &#x60;issuance&#x60; — Collect payment when the provider issues the certificate to the user.  **Note:**  For more information, read the _For certificate orders_ section of our [Guide to cPanel Market Provider Modules](https://go.cpanel.net/featureshowcasemarket) documentation. | [optional] 
**x_price_per_domain** | **float** | The product&#39;s price per domain. | [optional] 
**x_price_per_domain_maximum** | **float** | The maximum &#x60;x_price_per_domain&#x60; value. | [optional] 
**x_price_per_domain_minimum** | **float** | The minimum &#x60;x_price_per_domain&#x60; value. | [optional] 
**x_price_per_wildcard_domain** | **float** | The price per domain for a wildcard certificate. | [optional] 
**x_price_per_wildcard_domain_maximum** | **float** | The maximum &#x60;x_prive_per_wildcard_domain&#x60; value. | [optional] 
**x_price_per_wildcard_domain_minimum** | **float** | The minimum &#x60;x_prive_per_wildcard_domain&#x60; value. | [optional] 
**x_ssl_per_domain_pricing** | **int** | Whether the provider uses per-domain pricing for this certificate. * &#x60;1&#x60; — Uses per-domain pricing. * &#x60;0&#x60; — Does **not** use per-domain pricing. | [optional] 
**x_supports_dns_dcv** | **int** | Whether this product supports DNS-based DCV. * &#x60;1&#x60; — Supports DNS DCV. * &#x60;0&#x60; — Does &#x60;not&#x60; support DNS DCV. | [optional] 
**x_validation_type** | **str** | The validation type. | [optional] 
**x_warn_after** | **int** | A length of time, in seconds, after which the cPanel interface warns the user that a problem may exist with the order. The warning suggests that they contact the cPanel Market provider&#39;s support contact. | [optional] 
**x_wildcard_parent_domain_free** | **int** | Indicates if a wildcard domain includes its parent domain. For example, &#x60;*.example.com&#x60; would include the &#x60;example.com&#x60; parent domain.  * &#x60;1&#x60; — The domain does include its parent domain. * &#x60;0&#x60; — The domain does **not** include its parent domain. | [optional] 

## Example

```python
from clientapi_cpanel.models.market_provider_product_meta_data_type import MarketProviderProductMetaDataType

# TODO update the JSON string below
json = "{}"
# create an instance of MarketProviderProductMetaDataType from a JSON string
market_provider_product_meta_data_type_instance = MarketProviderProductMetaDataType.from_json(json)
# print the JSON string representation of the object
print(MarketProviderProductMetaDataType.to_json())

# convert the object into a dict
market_provider_product_meta_data_type_dict = market_provider_product_meta_data_type_instance.to_dict()
# create an instance of MarketProviderProductMetaDataType from a dict
market_provider_product_meta_data_type_from_dict = MarketProviderProductMetaDataType.from_dict(market_provider_product_meta_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


