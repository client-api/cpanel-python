# InlineResponse20053ResultDataInnerValueValue

The name of this property is the collection id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_color** | **str** | For calendars only: The color to use for calendar events. | [optional] 
**description** | **str** | The description of the collection. | [optional] 
**displayname** | **str** | The name of the collection. | [optional] 
**protected** | **int** | If this value is &#x60;1&#x60;, then the collection cannot be deleted through the API. | [optional] 
**type** | **str** | The type of the collection. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20053_result_data_inner_value_value import InlineResponse20053ResultDataInnerValueValue

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20053ResultDataInnerValueValue from a JSON string
inline_response20053_result_data_inner_value_value_instance = InlineResponse20053ResultDataInnerValueValue.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20053ResultDataInnerValueValue.to_json())

# convert the object into a dict
inline_response20053_result_data_inner_value_value_dict = inline_response20053_result_data_inner_value_value_instance.to_dict()
# create an instance of InlineResponse20053ResultDataInnerValueValue from a dict
inline_response20053_result_data_inner_value_value_from_dict = InlineResponse20053ResultDataInnerValueValue.from_dict(inline_response20053_result_data_inner_value_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


