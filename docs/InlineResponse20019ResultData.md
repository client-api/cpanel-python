# InlineResponse20019ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The delivered email message&#39;s sender. | [optional] 
**failed** | **int** | Whether the system could not deliver the message.  **Note:**   * The function only returns this value if it doesn&#39;t deliver the message.  * &#x60;1&#x60; is the only possible value. | [optional] 
**matches** | **List[str]** | A list of delivered email messages. | [optional] 
**operator** | **str** | The action that the function performed.  * &#x60;deliver&#x60; * &#x60;deliverall&#x60; | [optional] 
**reason** | **str** | A message about the failure or the warning.  **Note:**  The function only returns this value if it doesn&#39;t delete the message or experiences issues when it deletes the message. | [optional] 
**warning** | **int** | Whether the system experienced issues when it delivered the message.  **Note:**   * The function only returns this value if it experiences issues when it delivers the message.  * &#x60;1&#x60; is the only possible value. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20019_result_data import InlineResponse20019ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20019ResultData from a JSON string
inline_response20019_result_data_instance = InlineResponse20019ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20019ResultData.to_json())

# convert the object into a dict
inline_response20019_result_data_dict = inline_response20019_result_data_instance.to_dict()
# create an instance of InlineResponse20019ResultData from a dict
inline_response20019_result_data_from_dict = InlineResponse20019ResultData.from_dict(inline_response20019_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


