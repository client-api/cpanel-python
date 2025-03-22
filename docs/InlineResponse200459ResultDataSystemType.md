# InlineResponse200459ResultDataSystemType

The monitoring template used for the system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the system type. | [optional] [default to 'Website']
**id** | **object** | The system&#39;s type ID number. | [optional] 
**fixed_components** | **bool** | Whether the system components are immutable.   * &#x60;true&#x60; - The components are immutable.   * &#x60;false&#x60; - The components are not immutable.. | [optional] [default to True]

## Example

```python
from clientapi_cpanel.models.inline_response200459_result_data_system_type import InlineResponse200459ResultDataSystemType

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200459ResultDataSystemType from a JSON string
inline_response200459_result_data_system_type_instance = InlineResponse200459ResultDataSystemType.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200459ResultDataSystemType.to_json())

# convert the object into a dict
inline_response200459_result_data_system_type_dict = inline_response200459_result_data_system_type_instance.to_dict()
# create an instance of InlineResponse200459ResultDataSystemType from a dict
inline_response200459_result_data_system_type_from_dict = InlineResponse200459ResultDataSystemType.from_dict(inline_response200459_result_data_system_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


