# InlineResponse20075ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared** | **int** | Whether the global address book is enabled. * &#x60;1&#x60; — Enabled. * &#x60;0&#x60; — **Not** enabled. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20075_result_data import InlineResponse20075ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20075ResultData from a JSON string
inline_response20075_result_data_instance = InlineResponse20075ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20075ResultData.to_json())

# convert the object into a dict
inline_response20075_result_data_dict = inline_response20075_result_data_instance.to_dict()
# create an instance of InlineResponse20075ResultData from a dict
inline_response20075_result_data_from_dict = InlineResponse20075ResultData.from_dict(inline_response20075_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


