# MarketProviderProductMetaData


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

## Example

```python
from clientapi_cpanel.models.market_provider_product_meta_data import MarketProviderProductMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of MarketProviderProductMetaData from a JSON string
market_provider_product_meta_data_instance = MarketProviderProductMetaData.from_json(json)
# print the JSON string representation of the object
print(MarketProviderProductMetaData.to_json())

# convert the object into a dict
market_provider_product_meta_data_dict = market_provider_product_meta_data_instance.to_dict()
# create an instance of MarketProviderProductMetaData from a dict
market_provider_product_meta_data_from_dict = MarketProviderProductMetaData.from_dict(market_provider_product_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


