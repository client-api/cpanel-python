# InlineResponse20026ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | The date for which the system returned the log. | [optional] 
**lines** | **List[str]** | An array of lines from the log file. If the log file doesn&#39;t exist or if no log lines exist in the file, the function returns an empty array. | [optional] 
**path** | **str** | The log file&#39;s filepath. If the log file doesn&#39;t exist, the function returns an empty string. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20026_result_data import InlineResponse20026ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20026ResultData from a JSON string
inline_response20026_result_data_instance = InlineResponse20026ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20026ResultData.to_json())

# convert the object into a dict
inline_response20026_result_data_dict = inline_response20026_result_data_instance.to_dict()
# create an instance of InlineResponse20026ResultData from a dict
inline_response20026_result_data_from_dict = InlineResponse20026ResultData.from_dict(inline_response20026_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


