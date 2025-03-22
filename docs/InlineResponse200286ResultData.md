# InlineResponse200286ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paths** | [**List[InlineResponse200286ResultDataPaths]**](InlineResponse200286ResultDataPaths.md) | An array of objects of &#x60;php.ini&#x60; file information. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200286_result_data import InlineResponse200286ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200286ResultData from a JSON string
inline_response200286_result_data_instance = InlineResponse200286ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200286ResultData.to_json())

# convert the object into a dict
inline_response200286_result_data_dict = inline_response200286_result_data_instance.to_dict()
# create an instance of InlineResponse200286ResultData from a dict
inline_response200286_result_data_from_dict = InlineResponse200286ResultData.from_dict(inline_response200286_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


