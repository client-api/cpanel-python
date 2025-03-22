# InlineResponse20094ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The security key&#39;s domain. | [optional] 
**key_content** | **str** | The content of the key, which includes the algorithm. | [optional] 
**key_id** | **int** | The security key&#39;s ID. | [optional] 
**key_tag** | **int** | The security key&#39;s internal identifier. | [optional] 
**key_type** | **str** | The security key&#39;s signing type.  * &#x60;CSK&#x60; - Combined Signing Key. * &#x60;KSK&#x60; - Key Signing Key. * &#x60;ZSK&#x60; - Zone Signing Key. | [optional] 
**success** | **int** | Whether the function succeeded.  * &#x60;1&#x60; - The function succeeded. * &#x60;0&#x60; - The function failed. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20094_result_data import InlineResponse20094ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20094ResultData from a JSON string
inline_response20094_result_data_instance = InlineResponse20094ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20094ResultData.to_json())

# convert the object into a dict
inline_response20094_result_data_dict = inline_response20094_result_data_instance.to_dict()
# create an instance of InlineResponse20094ResultData from a dict
inline_response20094_result_data_from_dict = InlineResponse20094ResultData.from_dict(inline_response20094_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


