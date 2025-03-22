# InlineResponse20022ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_auto_whitelist** | **int** | Whether whitelisting is enabled. * 1 - Enabled. * 0 - Disabled. | [optional] 
**from_addresses** | **str** | The email addresses that send emails from the account. A comma-separated list of email addresses. | [optional] 
**from_name** | **str** | The name of the person who owns the email account. | [optional] 
**queue_days** | **int** | The number of days that the system retains log files and queued messages. | [optional] 
**spam_score** | **float** | The account&#39;s [Apache SpamAssassin](https://go.cpanel.net/cpaneldocsSpamFilters) threshold score. | [optional] 
**whitelist_by_association** | **int** | Whether the system whitelisted the email addresses in a message&#39;s &#x60;To&#x60; and &#x60;From&#x60; sections, including carbon-copied (CC) recipients. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20022_result_data import InlineResponse20022ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20022ResultData from a JSON string
inline_response20022_result_data_instance = InlineResponse20022ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20022ResultData.to_json())

# convert the object into a dict
inline_response20022_result_data_dict = inline_response20022_result_data_instance.to_dict()
# create an instance of InlineResponse20022ResultData from a dict
inline_response20022_result_data_from_dict = InlineResponse20022ResultData.from_dict(inline_response20022_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


