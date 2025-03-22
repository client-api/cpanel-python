# InlineResponse20051ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared** | **int** | Whether the sharing succeeded. * &#x60;1&#x60; — Shared. * &#x60;0&#x60; — **Not** shared. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20051_result_data import InlineResponse20051ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20051ResultData from a JSON string
inline_response20051_result_data_instance = InlineResponse20051ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20051ResultData.to_json())

# convert the object into a dict
inline_response20051_result_data_dict = inline_response20051_result_data_instance.to_dict()
# create an instance of InlineResponse20051ResultData from a dict
inline_response20051_result_data_from_dict = InlineResponse20051ResultData.from_dict(inline_response20051_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


