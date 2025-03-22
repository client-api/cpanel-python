# InlineResponse200241ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charset** | **str** | The file&#39;s new character set. | [optional] 
**content** | **str** | The file&#39;s content. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200241_result_data import InlineResponse200241ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200241ResultData from a JSON string
inline_response200241_result_data_instance = InlineResponse200241ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200241ResultData.to_json())

# convert the object into a dict
inline_response200241_result_data_dict = inline_response200241_result_data_instance.to_dict()
# create an instance of InlineResponse200241ResultData from a dict
inline_response200241_result_data_from_dict = InlineResponse200241ResultData.from_dict(inline_response200241_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


