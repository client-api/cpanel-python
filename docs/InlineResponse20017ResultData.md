# InlineResponse20017ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address that sent the blacklisted message. | [optional] 
**failed** | **int** | Whether the system failed to blacklist the message.  **Note:**   The function only returns this value if it doesn&#39;t blacklist the message. | [optional] 
**matches** | **List[str]** | An array of messages that the system deleted. | [optional] 
**operator** | **str** | The action that the function performed. | [optional] 
**reason** | **str** | A message about the failure or the warning.  **Note:**   The function only returns this value if it doesn&#39;t delete the message or experiences issues when it deletes the message. | [optional] 
**warning** | **int** | Whether the system experienced issues when it blacklisted the message.  **Note:**   The function only returns this value if it doesn&#39;t blacklist the message. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20017_result_data import InlineResponse20017ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20017ResultData from a JSON string
inline_response20017_result_data_instance = InlineResponse20017ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20017ResultData.to_json())

# convert the object into a dict
inline_response20017_result_data_dict = inline_response20017_result_data_instance.to_dict()
# create an instance of InlineResponse20017ResultData from a dict
inline_response20017_result_data_from_dict = InlineResponse20017ResultData.from_dict(inline_response20017_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


