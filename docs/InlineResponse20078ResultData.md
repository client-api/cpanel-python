# InlineResponse20078ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dcv_string** | **str** | The expected value of the queried DNS record. | [optional] 
**domain** | **str** | The domain that the system verified. | [optional] 
**failure_reason** | **str** | A message that contains the reason why the DCV check failed.  **Note:**    If the server fails to update the DNS zone, the system returns this value. | [optional] 
**query_results** | **List[str]** | The strings that the DNS query returned. This array may be empty.  **Note:**   If the server fails to update the DNS zone, the system returns the &#x60;failure_reason&#x60; value. | [optional] 
**succeeded** | **int** | Whether the DCV check succeeded. - &#x60;1&#x60; - At least one of the &#x60;query_results&#x60; values equals the &#x60;dcv_string&#x60; value. - &#x60;0&#x60; - None of the &#x60;query_results&#x60; values equal the &#x60;dcv_string&#x60; value. | [optional] 
**zone** | **str** | The altered and queried DNS zone name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20078_result_data import InlineResponse20078ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20078ResultData from a JSON string
inline_response20078_result_data_instance = InlineResponse20078ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20078ResultData.to_json())

# convert the object into a dict
inline_response20078_result_data_dict = inline_response20078_result_data_instance.to_dict()
# create an instance of InlineResponse20078ResultData from a dict
inline_response20078_result_data_from_dict = InlineResponse20078ResultData.from_dict(inline_response20078_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


