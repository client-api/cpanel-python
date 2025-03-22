# InlineResponse20092ResultDataEnabled

An object containing information about the domains for which the system enabled DNSSEC.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**InlineResponse20092ResultDataEnabledAdditionalProperties**](InlineResponse20092ResultDataEnabledAdditionalProperties.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20092_result_data_enabled import InlineResponse20092ResultDataEnabled

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20092ResultDataEnabled from a JSON string
inline_response20092_result_data_enabled_instance = InlineResponse20092ResultDataEnabled.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20092ResultDataEnabled.to_json())

# convert the object into a dict
inline_response20092_result_data_enabled_dict = inline_response20092_result_data_enabled_instance.to_dict()
# create an instance of InlineResponse20092ResultDataEnabled from a dict
inline_response20092_result_data_enabled_from_dict = InlineResponse20092ResultDataEnabled.from_dict(inline_response20092_result_data_enabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


