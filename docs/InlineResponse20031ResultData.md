# InlineResponse20031ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The sender&#39;s email address. | [optional] 
**queuefile** | **str** | The message&#39;s unique ID. | [optional] 
**subject** | **str** | The message&#39;s subject. | [optional] 
**time** | **int** | The message&#39;s creation time. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20031_result_data import InlineResponse20031ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20031ResultData from a JSON string
inline_response20031_result_data_instance = InlineResponse20031ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20031ResultData.to_json())

# convert the object into a dict
inline_response20031_result_data_dict = inline_response20031_result_data_instance.to_dict()
# create an instance of InlineResponse20031ResultData from a dict
inline_response20031_result_data_from_dict = InlineResponse20031ResultData.from_dict(inline_response20031_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


