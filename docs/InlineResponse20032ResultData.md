# InlineResponse20032ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address for which the system processed an email message. | [optional] 
**failed** | **int** | Whether the system failed to process the message.  * &#x60;1&#x60; - The function failed to process the message. This is the only possible value.  **Note:**  The function only returns this value if it fails to process the message. | [optional] 
**matches** | **List[str]** | An array of email messages that the system processed. | [optional] 
**operator** | **str** | The operation that the system performed. * &#x60;deliver&#x60; - Delivered a specific message. * &#x60;deliverall&#x60; - Delivered all messages from a sender. * &#x60;delete&#x60; - Deleted a message. * &#x60;deleteall&#x60; - Deleted all messages from a sender. * &#x60;blacklist&#x60; - Blacklisted the sender of an email message. * &#x60;whitelist&#x60; - Whitelisted the sender of an email message. * &#x60;ignore&#x60; - Ignored email messages from a sender.  **Note:**  The function only returns this value if it successfully processes the message. | [optional] 
**reason** | **str** | A message about the failure or the warning.  **Note:**  The function only returns this value if it fails to processes the message or experiences issues when it processes the message. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20032_result_data import InlineResponse20032ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20032ResultData from a JSON string
inline_response20032_result_data_instance = InlineResponse20032ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20032ResultData.to_json())

# convert the object into a dict
inline_response20032_result_data_dict = inline_response20032_result_data_instance.to_dict()
# create an instance of InlineResponse20032ResultData from a dict
inline_response20032_result_data_from_dict = InlineResponse20032ResultData.from_dict(inline_response20032_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


