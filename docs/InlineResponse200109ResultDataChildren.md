# InlineResponse200109ResultDataChildren


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The subdirectory&#39;s absolute directory path. | [optional] 
**state** | [**InlineResponse200109ResultDataState**](InlineResponse200109ResultDataState.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200109_result_data_children import InlineResponse200109ResultDataChildren

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200109ResultDataChildren from a JSON string
inline_response200109_result_data_children_instance = InlineResponse200109ResultDataChildren.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200109ResultDataChildren.to_json())

# convert the object into a dict
inline_response200109_result_data_children_dict = inline_response200109_result_data_children_instance.to_dict()
# create an instance of InlineResponse200109ResultDataChildren from a dict
inline_response200109_result_data_children_from_dict = InlineResponse200109ResultDataChildren.from_dict(inline_response200109_result_data_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


