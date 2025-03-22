# InlineResponse200107ResultDataChildren


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The subdirectory&#39;s directory path. | [optional] 
**state** | [**InlineResponse200107ResultDataState**](InlineResponse200107ResultDataState.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200107_result_data_children import InlineResponse200107ResultDataChildren

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200107ResultDataChildren from a JSON string
inline_response200107_result_data_children_instance = InlineResponse200107ResultDataChildren.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200107ResultDataChildren.to_json())

# convert the object into a dict
inline_response200107_result_data_children_dict = inline_response200107_result_data_children_instance.to_dict()
# create an instance of InlineResponse200107ResultDataChildren from a dict
inline_response200107_result_data_children_from_dict = InlineResponse200107ResultDataChildren.from_dict(inline_response200107_result_data_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


