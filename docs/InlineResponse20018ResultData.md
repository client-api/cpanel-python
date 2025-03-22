# InlineResponse20018ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The deleted email message&#39;s sender. | [optional] 
**failed** | **int** | Whether the system failed to delete the messages.  **Note:**  The function only returns this value if it doesn&#39;t delete the message. | [optional] 
**matches** | **List[str]** | An array of messages that the system deleted. | [optional] 
**operator** | **str** | The operation that the system performed. | [optional] 
**reason** | **str** | A message about the failure or the warning.  **Note:**  The function only returns this value if it doesn&#39;t delete the message or experiences issues when it deletes the message. | [optional] 
**warning** | **int** | Whether the system experienced issues when it deleted the message.  **Note:**  The function only returns this value if it experiences issues when it deletes the message. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20018_result_data import InlineResponse20018ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20018ResultData from a JSON string
inline_response20018_result_data_instance = InlineResponse20018ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20018ResultData.to_json())

# convert the object into a dict
inline_response20018_result_data_dict = inline_response20018_result_data_instance.to_dict()
# create an instance of InlineResponse20018ResultData from a dict
inline_response20018_result_data_from_dict = InlineResponse20018ResultData.from_dict(inline_response20018_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


