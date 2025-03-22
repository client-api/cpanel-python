# InlineResponse200101ResultDataChildren


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The subdirectory&#39;s absolute path. | [optional] 
**state** | [**InlineResponse200101ResultDataState**](InlineResponse200101ResultDataState.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200101_result_data_children import InlineResponse200101ResultDataChildren

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200101ResultDataChildren from a JSON string
inline_response200101_result_data_children_instance = InlineResponse200101ResultDataChildren.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200101ResultDataChildren.to_json())

# convert the object into a dict
inline_response200101_result_data_children_dict = inline_response200101_result_data_children_instance.to_dict()
# create an instance of InlineResponse200101ResultDataChildren from a dict
inline_response200101_result_data_children_from_dict = InlineResponse200101ResultDataChildren.from_dict(inline_response200101_result_data_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


