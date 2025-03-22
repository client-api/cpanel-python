# InlineResponse200109ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[InlineResponse200109ResultDataChildren]**](InlineResponse200109ResultDataChildren.md) | A list of subdirectories and their leech protection information.  **Note:**  The function returns a list for each subdirectory in a directory. | [optional] 
**current** | [**InlineResponse200109ResultDataCurrent**](InlineResponse200109ResultDataCurrent.md) |  | [optional] 
**home** | [**InlineResponse200109ResultDataHome**](InlineResponse200109ResultDataHome.md) |  | [optional] 
**parent** | [**InlineResponse200109ResultDataParent**](InlineResponse200109ResultDataParent.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200109_result_data import InlineResponse200109ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200109ResultData from a JSON string
inline_response200109_result_data_instance = InlineResponse200109ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200109ResultData.to_json())

# convert the object into a dict
inline_response200109_result_data_dict = inline_response200109_result_data_instance.to_dict()
# create an instance of InlineResponse200109ResultData from a dict
inline_response200109_result_data_from_dict = InlineResponse200109ResultData.from_dict(inline_response200109_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


