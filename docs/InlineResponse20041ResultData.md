# InlineResponse20041ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | A whitelisted email address. | [optional] 
**failed** | **str** | The system failed to whitelist the message.  * &#x60;1&#x60; — The function failed to whitelist the message. This is the only possible value.  **Note:**  The function only returns this property if it failed to whitelist the message. | [optional] [default to '1']
**matches** | **List[str]** | An array of message files that the system whitelisted.  **Note:**  The function **only** returns this value if it whitelists the message. | [optional] 
**operator** | **str** | The action that the system performed. | [optional] [default to 'whitelist']
**reason** | **str** | The reason the function skipped the message during whitelisting. The &#x60;reason&#x60; property is returned only if the function failed to whitelist the message. | [optional] 
**warning** | **int** | Whether the system experienced issues when it whitelisted the message.  * &#x60;1&#x60; — There was an issue whitelisting the message. This is the only possible value.  **Note:**  The function only returns this property if it failed to whitelist the message. | [optional] [default to 1]

## Example

```python
from clientapi_cpanel.models.inline_response20041_result_data import InlineResponse20041ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20041ResultData from a JSON string
inline_response20041_result_data_instance = InlineResponse20041ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20041ResultData.to_json())

# convert the object into a dict
inline_response20041_result_data_dict = inline_response20041_result_data_instance.to_dict()
# create an instance of InlineResponse20041ResultData from a dict
inline_response20041_result_data_from_dict = InlineResponse20041ResultData.from_dict(inline_response20041_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


