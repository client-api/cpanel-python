# InlineResponse200101ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[InlineResponse200101ResultDataChildren]**](InlineResponse200101ResultDataChildren.md) | Subdirectories and their indexing information.  **Note:**  The function returns an object for each subdirectory in a directory. | [optional] 
**current** | [**InlineResponse200101ResultDataCurrent**](InlineResponse200101ResultDataCurrent.md) |  | [optional] 
**home** | [**InlineResponse200101ResultDataHome**](InlineResponse200101ResultDataHome.md) |  | [optional] 
**parent** | [**InlineResponse200101ResultDataParent**](InlineResponse200101ResultDataParent.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200101_result_data import InlineResponse200101ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200101ResultData from a JSON string
inline_response200101_result_data_instance = InlineResponse200101ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200101ResultData.to_json())

# convert the object into a dict
inline_response200101_result_data_dict = inline_response200101_result_data_instance.to_dict()
# create an instance of InlineResponse200101ResultData from a dict
inline_response200101_result_data_from_dict = InlineResponse200101ResultData.from_dict(inline_response200101_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


