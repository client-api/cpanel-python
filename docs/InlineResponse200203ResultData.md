# InlineResponse200203ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The filter&#39;s email address. The function only returns this value if it created a user-level filter. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200203_result_data import InlineResponse200203ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200203ResultData from a JSON string
inline_response200203_result_data_instance = InlineResponse200203ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200203ResultData.to_json())

# convert the object into a dict
inline_response200203_result_data_dict = inline_response200203_result_data_instance.to_dict()
# create an instance of InlineResponse200203ResultData from a dict
inline_response200203_result_data_from_dict = InlineResponse200203ResultData.from_dict(inline_response200203_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


