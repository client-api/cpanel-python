# InlineResponse200295ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | The archive file&#39;s name. | [optional] 
**mtime** | **int** | The archive file&#39;s last modified date. | [optional] 
**path** | **str** | The archive file&#39;s path. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200295_result_data import InlineResponse200295ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200295ResultData from a JSON string
inline_response200295_result_data_instance = InlineResponse200295ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200295ResultData.to_json())

# convert the object into a dict
inline_response200295_result_data_dict = inline_response200295_result_data_instance.to_dict()
# create an instance of InlineResponse200295ResultData from a dict
inline_response200295_result_data_from_dict = InlineResponse200295ResultData.from_dict(inline_response200295_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


