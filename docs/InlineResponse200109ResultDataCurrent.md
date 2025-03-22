# InlineResponse200109ResultDataCurrent

The user's current directory and its leech protection information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The current directory&#39;s absolute file path. | [optional] 
**state** | [**InlineResponse200109ResultDataCurrentState**](InlineResponse200109ResultDataCurrentState.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200109_result_data_current import InlineResponse200109ResultDataCurrent

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200109ResultDataCurrent from a JSON string
inline_response200109_result_data_current_instance = InlineResponse200109ResultDataCurrent.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200109ResultDataCurrent.to_json())

# convert the object into a dict
inline_response200109_result_data_current_dict = inline_response200109_result_data_current_instance.to_dict()
# create an instance of InlineResponse200109ResultDataCurrent from a dict
inline_response200109_result_data_current_from_dict = InlineResponse200109ResultDataCurrent.from_dict(inline_response200109_result_data_current_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


