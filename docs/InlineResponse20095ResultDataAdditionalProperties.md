# InlineResponse20095ResultDataAdditionalProperties

An object containing the domain's DS record information.  **Note:**  The return's name is the domain's name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**InlineResponse20095ResultDataAdditionalPropertiesKeys**](InlineResponse20095ResultDataAdditionalPropertiesKeys.md) |  | [optional] 
**nsec_details** | [**InlineResponse20095ResultDataAdditionalPropertiesNsecDetails**](InlineResponse20095ResultDataAdditionalPropertiesNsecDetails.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20095_result_data_additional_properties import InlineResponse20095ResultDataAdditionalProperties

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20095ResultDataAdditionalProperties from a JSON string
inline_response20095_result_data_additional_properties_instance = InlineResponse20095ResultDataAdditionalProperties.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20095ResultDataAdditionalProperties.to_json())

# convert the object into a dict
inline_response20095_result_data_additional_properties_dict = inline_response20095_result_data_additional_properties_instance.to_dict()
# create an instance of InlineResponse20095ResultDataAdditionalProperties from a dict
inline_response20095_result_data_additional_properties_from_dict = InlineResponse20095ResultDataAdditionalProperties.from_dict(inline_response20095_result_data_additional_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


