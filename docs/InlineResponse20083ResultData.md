# InlineResponse20083ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **int** | Whether &#x60;ALIAS&#x60; records are available.  * &#x60;1&#x60; - Available. * &#x60;0&#x60; - Not available.  When &#x60;ALIAS&#x60; records are enabled, they may work in API calls that accept &#x60;A&#x60; and &#x60;AAAA&#x60; records. However, the &#x60;ALIAS&#x60; record must use a fully qualified domain name (FQDN) rather than an IP address. | [optional] 
**aname** | **int** | Whether &#x60;ANAME&#x60; records are available.  * &#x60;1&#x60; - Available. * &#x60;0&#x60; - Not available.  **NOTE:**  The &#x60;aname&#x60; value is always set to false (i.e. Not available). The &#x60;ANAME&#x60; record is currently not supported. It is included for completeness and future proofing. | [optional] 
**resolver** | **str** | The value (if any) of the running PDNS’s &#x60;resolver&#x60; setting. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20083_result_data import InlineResponse20083ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20083ResultData from a JSON string
inline_response20083_result_data_instance = InlineResponse20083ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20083ResultData.to_json())

# convert the object into a dict
inline_response20083_result_data_dict = inline_response20083_result_data_instance.to_dict()
# create an instance of InlineResponse20083ResultData from a dict
inline_response20083_result_data_from_dict = InlineResponse20083ResultData.from_dict(inline_response20083_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


