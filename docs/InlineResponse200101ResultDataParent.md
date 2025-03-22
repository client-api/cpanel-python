# InlineResponse200101ResultDataParent

The current directory’s parent directory and its indexing information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The parent directory&#39;s absolute path. | [optional] 
**state** | [**InlineResponse200101ResultDataParentState**](InlineResponse200101ResultDataParentState.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200101_result_data_parent import InlineResponse200101ResultDataParent

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200101ResultDataParent from a JSON string
inline_response200101_result_data_parent_instance = InlineResponse200101ResultDataParent.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200101ResultDataParent.to_json())

# convert the object into a dict
inline_response200101_result_data_parent_dict = inline_response200101_result_data_parent_instance.to_dict()
# create an instance of InlineResponse200101ResultDataParent from a dict
inline_response200101_result_data_parent_from_dict = InlineResponse200101ResultDataParent.from_dict(inline_response200101_result_data_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


