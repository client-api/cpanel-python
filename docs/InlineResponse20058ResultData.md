# InlineResponse20058ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_id** | **int** | An eight-digit random integer that the system uses to work around a browser&#39;s caching mechanism. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20058_result_data import InlineResponse20058ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20058ResultData from a JSON string
inline_response20058_result_data_instance = InlineResponse20058ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20058ResultData.to_json())

# convert the object into a dict
inline_response20058_result_data_dict = inline_response20058_result_data_instance.to_dict()
# create an instance of InlineResponse20058ResultData from a dict
inline_response20058_result_data_from_dict = InlineResponse20058ResultData.from_dict(inline_response20058_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


