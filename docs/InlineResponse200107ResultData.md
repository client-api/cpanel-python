# InlineResponse200107ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[InlineResponse200107ResultDataChildren]**](InlineResponse200107ResultDataChildren.md) | An array of objects containing subdirectories and their privacy information.  **Note:**  The function returns an object for each subdirectory in a directory. | [optional] 
**current** | [**InlineResponse200107ResultDataCurrent**](InlineResponse200107ResultDataCurrent.md) |  | [optional] 
**home** | [**InlineResponse200107ResultDataHome**](InlineResponse200107ResultDataHome.md) |  | [optional] 
**parent** | [**InlineResponse200107ResultDataParent**](InlineResponse200107ResultDataParent.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200107_result_data import InlineResponse200107ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200107ResultData from a JSON string
inline_response200107_result_data_instance = InlineResponse200107ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200107ResultData.to_json())

# convert the object into a dict
inline_response200107_result_data_dict = inline_response200107_result_data_instance.to_dict()
# create an instance of InlineResponse200107ResultData from a dict
inline_response200107_result_data_from_dict = InlineResponse200107ResultData.from_dict(inline_response200107_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


