# InlineResponse20044ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_group_order** | **Dict[str, int]** | An object that defines the default order of applications in cPanel. | [optional] 
**grouporder** | **List[str]** | A list of group IDs, in the order in which the groups appear. | [optional] 
**groups** | [**List[InlineResponse20044ResultDataGroups]**](InlineResponse20044ResultDataGroups.md) | Information about each group in the cPanel interface. | [optional] 
**implements** | **Dict[str, str]** | An object mapping the &#x60;implements&#x60; names to Appkey values for applications in cPanel.  For example, use this mapping to determine that the &#x60;implements&#x60; value &#x60;SSL_TLS_Status&#x60; maps to the Appkey value &#x60;tls_status&#x60;.  **Note:**  * The Appkey for an application can be found in the &#x60;key&#x60; attribute elsewhere in the API response. * The &#x60;implements&#x60; for an application can be found in the &#x60;implements&#x60; attribute elsewhere in the API response. * For more information about Appkey values, read our [Guide to cPanel Interface Customization - Appkeys](https://go.cpanel.net/paper-lantern-theme-guide-to-cpanel-interface-customization-appkeys) documentation. | [optional] 
**index** | **Dict[str, List[int]]** | The applications and the order in which they appear in the cPanel interface. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20044_result_data import InlineResponse20044ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20044ResultData from a JSON string
inline_response20044_result_data_instance = InlineResponse20044ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20044ResultData.to_json())

# convert the object into a dict
inline_response20044_result_data_dict = inline_response20044_result_data_instance.to_dict()
# create an instance of InlineResponse20044ResultData from a dict
inline_response20044_result_data_from_dict = InlineResponse20044ResultData.from_dict(inline_response20044_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


