# InlineResponse20029ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The ignored email message&#39;s sender. | [optional] 
**failed** | **int** | Whether the system failed to ignore the messages.  * &#x60;1&#x60; - Failed to ignore the message.  * &#x60;1&#x60; - Failed to ignore the message.  * &#x60;1&#x60; - Failed to ignore the message.  * &#x60;1&#x60; - Failed to ignore the message.  * &#x60;1&#x60; - Failed to ignore the message.  **Note:**   The function only returns this value if it experiences issues when it ignores the message. | [optional] 
**matches** | **List[str]** | An array containing ignored message files. | [optional] 
**operator** | **str** | The operation that the system performed.  * &#x60;ignore&#x60; — The system ignored this email message. | [optional] 
**reason** | **str** | A message that describes the failure or the warning.  **Note:**   The function only returns this value if it doesn&#39;t ignore the message or experiences issues when it ignores the message.  | [optional] 
**warning** | **int** | Whether the system experienced issues when it ignored the message.  * &#x60;1&#x60; — The system encountered a problem.  **Note:**   The function only returns this value if it experiences issues when it ignores the message. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20029_result_data import InlineResponse20029ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20029ResultData from a JSON string
inline_response20029_result_data_instance = InlineResponse20029ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20029ResultData.to_json())

# convert the object into a dict
inline_response20029_result_data_dict = inline_response20029_result_data_instance.to_dict()
# create an instance of InlineResponse20029ResultData from a dict
inline_response20029_result_data_from_dict = InlineResponse20029ResultData.from_dict(inline_response20029_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


