# InlineResponse200107ResultDataParent

The parent directory of the current directory and its privacy information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The parent directory&#39;s absolute directory path. | [optional] 
**state** | [**InlineResponse200107ResultDataParentState**](InlineResponse200107ResultDataParentState.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200107_result_data_parent import InlineResponse200107ResultDataParent

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200107ResultDataParent from a JSON string
inline_response200107_result_data_parent_instance = InlineResponse200107ResultDataParent.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200107ResultDataParent.to_json())

# convert the object into a dict
inline_response200107_result_data_parent_dict = inline_response200107_result_data_parent_instance.to_dict()
# create an instance of InlineResponse200107ResultDataParent from a dict
inline_response200107_result_data_parent_from_dict = InlineResponse200107ResultDataParent.from_dict(inline_response200107_result_data_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


