# InlineResponse200283ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The account&#39;s name. | [optional] 
**account_owner** | **str** | The account&#39;s owner. | [optional] 
**documentroot** | **str** | The virtual host&#39;s document root. | [optional] 
**homedir** | **str** | The virtual host&#39;s home directory. | [optional] 
**main_domain** | **int** | Whether the virtual host is the primary domain.  **Note:**  * &#x60;1&#x60; - The primary domain * &#x60;0&#x60; - **Not** the primary domain | [optional] 
**php_fpm** | **int** | Whether FPM is enabled on the virtual host.  * &#x60;1&#x60; - PHP-FPM enabled. * &#x60;0&#x60; - PHP-FPM **not** enabled. | [optional] 
**php_fpm_pool_parms** | [**InlineResponse200283ResultPhpFpmPoolParms**](InlineResponse200283ResultPhpFpmPoolParms.md) |  | [optional] 
**phpversion_source** | [**List[InlineResponse200283ResultPhpversionSource]**](InlineResponse200283ResultPhpversionSource.md) | How the virtual host determines its PHP version. | [optional] 
**version** | **str** | The virtual host&#39;s PHP version. * &#x60;ea-php72&#x60; * &#x60;ea-php73&#x60; * &#x60;ea-php74&#x60; * Any custom PHP package name. | [optional] 
**vhost** | **str** | The virtual host&#39;s name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200283_result_data import InlineResponse200283ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200283ResultData from a JSON string
inline_response200283_result_data_instance = InlineResponse200283ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200283ResultData.to_json())

# convert the object into a dict
inline_response200283_result_data_dict = inline_response200283_result_data_instance.to_dict()
# create an instance of InlineResponse200283ResultData from a dict
inline_response200283_result_data_from_dict = InlineResponse200283ResultData.from_dict(inline_response200283_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


