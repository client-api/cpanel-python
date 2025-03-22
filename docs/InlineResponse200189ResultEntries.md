# InlineResponse200189ResultEntries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The mail exchanger&#39;s domain. | [optional] 
**entrycount** | **int** | The mail exchanger&#39;s order in the list of priorities. For example, the mail exchanger with the highest priority returns &#x60;1&#x60;, and the next highest priority returns &#x60;2&#x60;. | [optional] 
**mx** | **str** | The mail exchanger&#39;s name. | [optional] 
**priority** | **int** | The mail exchanger&#39;s [priority value](https://go.cpanel.net/whmdocsEditMXEntry). | [optional] 
**row** | **str** | Whether the mail exchanger is an odd or an even entry. * &#x60;even&#x60; * &#x60;odd&#x60; | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200189_result_entries import InlineResponse200189ResultEntries

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200189ResultEntries from a JSON string
inline_response200189_result_entries_instance = InlineResponse200189ResultEntries.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200189ResultEntries.to_json())

# convert the object into a dict
inline_response200189_result_entries_dict = inline_response200189_result_entries_instance.to_dict()
# create an instance of InlineResponse200189ResultEntries from a dict
inline_response200189_result_entries_from_dict = InlineResponse200189ResultEntries.from_dict(inline_response200189_result_entries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


