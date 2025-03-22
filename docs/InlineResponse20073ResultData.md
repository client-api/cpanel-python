# InlineResponse20073ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared** | **int** | Whether the global address book is shared. * 1 — Shared. * 0 — **Not** shared. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20073_result_data import InlineResponse20073ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20073ResultData from a JSON string
inline_response20073_result_data_instance = InlineResponse20073ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20073ResultData.to_json())

# convert the object into a dict
inline_response20073_result_data_dict = inline_response20073_result_data_instance.to_dict()
# create an instance of InlineResponse20073ResultData from a dict
inline_response20073_result_data_from_dict = InlineResponse20073ResultData.from_dict(inline_response20073_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


