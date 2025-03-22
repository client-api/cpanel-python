# InlineResponse20059ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_id** | **int** | random integer that the system uses to work with and around a browser&#39;s caching mechanism. An eight-digit integer. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20059_result_data import InlineResponse20059ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20059ResultData from a JSON string
inline_response20059_result_data_instance = InlineResponse20059ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20059ResultData.to_json())

# convert the object into a dict
inline_response20059_result_data_dict = inline_response20059_result_data_instance.to_dict()
# create an instance of InlineResponse20059ResultData from a dict
inline_response20059_result_data_from_dict = InlineResponse20059ResultData.from_dict(inline_response20059_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


