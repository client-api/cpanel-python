# InlineResponse200240ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_charset** | **str** | The file&#39;s character set. | [optional] 
**path** | **str** | The path to the file. | [optional] 
**to_charset** | **str** | The file&#39;s new character set. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200240_result_data import InlineResponse200240ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200240ResultData from a JSON string
inline_response200240_result_data_instance = InlineResponse200240ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200240ResultData.to_json())

# convert the object into a dict
inline_response200240_result_data_dict = inline_response200240_result_data_instance.to_dict()
# create an instance of InlineResponse200240ResultData from a dict
inline_response200240_result_data_from_dict = InlineResponse200240ResultData.from_dict(inline_response200240_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


