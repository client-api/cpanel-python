# InlineResponse200109ResultDataParent

The parent directory of the current directory and its leech protection information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The parent directory&#39;s absolute directory path. | [optional] 
**state** | [**InlineResponse200109ResultDataParentState**](InlineResponse200109ResultDataParentState.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200109_result_data_parent import InlineResponse200109ResultDataParent

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200109ResultDataParent from a JSON string
inline_response200109_result_data_parent_instance = InlineResponse200109ResultDataParent.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200109ResultDataParent.to_json())

# convert the object into a dict
inline_response200109_result_data_parent_dict = inline_response200109_result_data_parent_instance.to_dict()
# create an instance of InlineResponse200109ResultDataParent from a dict
inline_response200109_result_data_parent_from_dict = InlineResponse200109ResultDataParent.from_dict(inline_response200109_result_data_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


