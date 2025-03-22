# InlineResponse200401ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | The server&#39;s SSH port. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200401_result_data import InlineResponse200401ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200401ResultData from a JSON string
inline_response200401_result_data_instance = InlineResponse200401ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200401ResultData.to_json())

# convert the object into a dict
inline_response200401_result_data_dict = inline_response200401_result_data_instance.to_dict()
# create an instance of InlineResponse200401ResultData from a dict
inline_response200401_result_data_from_dict = InlineResponse200401ResultData.from_dict(inline_response200401_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


